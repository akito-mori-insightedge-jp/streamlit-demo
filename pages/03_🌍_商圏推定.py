import os
import sys
import streamlit as st
import inspect
import textwrap
import time
import numpy as np
import pandas as pd
import pickle
import requests
import streamlit.components.v1 as stc
import yaml
import cv2

def prepro(im):
    
    immask = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    lower = np.array([20, 4, 200])           # 抽出する色の下限(BGR)
    upper = np.array([30, 50 ,255])        # 抽出する色の上限(BGR)
    immask = cv2.inRange(immask, lower, upper)

    #輪郭抽出
    contours,hierarchy = cv2.findContours(immask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    im_con = im.copy()

    cv2.drawContours(im_con, contours, -1, (255,0,0), 1)

    Areas=[];rank=[]
    for i, contour in enumerate(contours):
        # 面積
        area = cv2.contourArea(contour)
        area = area / 1000
        Areas.append(area)

    idices = pd.DataFrame(Areas).reset_index().sort_values(0,ascending=False).index

    #大きいのを赤く
    for idx,r in enumerate(idices):
        if idx<5:
            cv2.drawContours(im_con, contours[r:r+1], -1, (0,0,255), 1)       
            # 輪郭の重心
            M = cv2.moments(contours[r:r+1][0])
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])  

            #輪郭（境界）の長さ
            cv2.putText(im_con, str('{:.1f}'.format(Areas[r])), (cx, cy),
                        cv2.FONT_HERSHEY_PLAIN, # フォントタイプ
                        1, # 文字サイズ
                        (0, 0, 0), # 文字色：白(255, 255, 255)　黒(0, 0, 0)
                        2, # 文字太さ
                        cv2.LINE_AA)

    cv2.imwrite('result.png', im_con)    
        
    

def pred():
    
    tab1, tab2 = st.tabs(["場所の指定", "結果"])
    with tab1:
        col1, col2 = st.columns(2)

        #lat = st.text_input("lat",value = "35.68517826190777")
        #long = st.text_input("lat",value = "139.7528236934712")
        lat = col1.slider("latitude",20.5,21.5,step = 0.01,value = 21.0)
        long =col2.slider("longitude",105.0,106.0,step = 0.01,value = 105.83)

        stc.html("""
        <iframe width="640" height="640" style="border:0" loading="lazy" src="https://www.google.com/maps/embed/v1/view?&key={}&zoom=17&center={},{}"></iframe>
        """.format(map_key,lat,long),width=640, height=640, scrolling=False)
        
        
    with tab2:
        url="""https://maps.googleapis.com/maps/api/staticmap?key={}&center={},{}&zoom=17&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&style=feature:administrative%7Celement:geometry%7Cvisibility:off&style=feature:administrative.land_parcel%7Cvisibility:off&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:poi%7Cvisibility:off&style=feature:road%7Cvisibility:off&style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:transit%7Cvisibility:off&size=640x640
    """.format(map_key,lat,long)
        response = requests.get(url)

        arr = np.frombuffer(response.content, dtype=np.uint8)
        im = cv2.imdecode(arr, flags=cv2.IMREAD_COLOR)
    
        prepro(im)
        st.write("""出店余地のある、大きめの商業ビルをピックアップ。""")
        st.image("result.png")


    
if os.path.exists("../key.ini"):
    with open("../key.ini", 'r') as yml:
        settings = yaml.load(yml, Loader=yaml.SafeLoader)
    map_key = settings["map_key"]
else:
    map_key = st.secrets["map_key"]

    
st.set_page_config(page_title="map demo", page_icon="🏘")
st.markdown("# 商圏予測 デモ")

st.write(
    """地図内の商業エリアを分析します。"""
)

pred()
