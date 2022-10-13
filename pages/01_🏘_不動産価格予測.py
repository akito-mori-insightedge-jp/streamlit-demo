import streamlit as st
import inspect
import textwrap
import time
import numpy as np
import pandas as pd
import pickle
import catboost
#import sklearn
import models.realestate.realestate_cands as ref

columns = [
        "市区町村名",
        "最寄駅：距離（分）",
        "間取り",
        "面積（㎡）",
        "建築年",
        "都市計画",
        "建ぺい率（％）",
        "容積率（％）",
        "取引時点",
        "改装",
        "place_idx",
        "distance",
    ]

def pred(model,address,scaler):
  
    col1, col2, col3 = st.columns(3)
    
    # col1
    with col1:
        市区町村名 = st.selectbox("市区町村名:", ref.市区町村_cands)
        間取り = st.selectbox("間取り", ref.間取り_cands)
        容積率 = st.slider("容積率（％）",50,1000,step = 10,value=50)
        
    # col2
    with col2:
        最寄駅距離 = st.slider("最寄駅：距離（分）",0,29,value=10)
        建築年 = st.slider("建築年",1950,2022,step = 1,value=2022)
        取引時点 = st.slider("取引時点",2015,2021,step = 1,value=2021)
    
    # col3
    with col3:
        面積 = col3.slider("面積（㎡）",10,250,step = 5,value=50)
        建ぺい率 = col3.select_slider("建ぺい率（％）",[30, 40, 50, 60, 80],value=50)
        改装 = col3.radio("改装",['改装済', '未改装'])

    distance = address[address["住所"] == 市区町村名]["distance"].values[0]
    place_idx = address[address["住所"] == 市区町村名]["place_idx"].values[0]
    place = address[address["住所"] == 市区町村名]["市区町村名"].values[0]
    
    都市計画 =  "第１種住居地域"
    #都市計画 =  st.selectbox("都市計画", ref.都市計画_cands,value="第１種住居地域")
    
    pred = [[place, 最寄駅距離, 間取り, 面積, 建築年, 都市計画, 建ぺい率, 容積率, 取引時点, 改装, place_idx, distance]]
    scaling_columns = ["最寄駅：距離（分）", "面積（㎡）", "建築年", "建ぺい率（％）", "容積率（％）", "distance"]
    pred = pd.DataFrame(pred, columns=columns)
    pred.loc[:, scaling_columns] = scaler.transform(pred.loc[:, scaling_columns])

    st.metric("選択した条件の予測価格", str(int(model.predict(pred)[0] / 10000))+"万円")
    
    
st.set_page_config(page_title="不動産価格予測", page_icon="🏘")
st.markdown("# 不動産価格予測 デモ")
#st.sidebar.header("Demo")
st.write(
    """設定した条件に基づき、不動産取引価格の予測値を計算します。"""
)

def loads():
    model = pickle.load(open("models/realestate/case1_model.pkl", "rb"))
    address = pd.read_csv("models/realestate/address_master.csv")
    scaler = pickle.load(open("models/realestate/scaler.pkl", "rb"))
    return model,address,scaler

with st.spinner("モデルを読み込んでいます。。。"):
    model,address,scaler = loads()

pred(model,address,scaler)

#show_code(plotting_demo)
