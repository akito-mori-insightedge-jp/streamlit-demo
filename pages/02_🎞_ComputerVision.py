import streamlit as st
import inspect
import textwrap
import time
import numpy as np

st.set_page_config(page_title="ComputerVision Demo", page_icon="🎞")
st.markdown("# ComputerVision Demo")
#st.sidebar.header("ComputerVision Demo")
st.write(
    """画像認識系で話のネタとして準備したもの"""
)

# contents
tab1, tab2, tab3 = st.tabs(["在庫数検出", "煙検知", "接近検知"])

# tab1
tab1.write(
    """重要商品の在庫数を常に検出して、欠品を防止したい。"""
)
tab1.markdown("""
              - 他にも、在庫数の把握には、様々な取り組みがある
                  - 重量計で重さを測定し、個数を把握する。
                  - 色の構成を見て、棚が空いているかを把握する。
              """)
tab1.video("https://youtu.be/RdZtctqcI70")

# tab2
tab2.write(
    """火災報知器では検出できないような、煙が少ないタイプの火災を検出したい"""
)

tab2.markdown("""
              - 手法の選択肢はいくつか存在
                  - 炎や煙を直接検出する
                  - 何らかの異常を検出する(Demo)
              """)

#tab2.video("https://www.youtube.com/shorts/s_9Iswp5M9w")
with tab2.container():
    tab2.video("data/smoke_predicted.mp4")

# tab3
tab3.write(
    """
    船舶着岸時に、小船がいないかを検出したい。
    
    デモとしては、船舶の検知及び、接近の検知を用意。
    """
)

tab3.video("https://youtu.be/12UHNXZvE7w")
