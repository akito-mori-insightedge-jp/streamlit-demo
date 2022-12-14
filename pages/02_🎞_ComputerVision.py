import streamlit as st
import inspect
import textwrap
import time
import numpy as np

st.set_page_config(page_title="ComputerVision Demo", page_icon="đ")
st.markdown("# ComputerVision Demo")
#st.sidebar.header("ComputerVision Demo")
st.write(
    """įģåčĒč­įŗģã§čŠąãŽããŋã¨ããĻæēåããããŽ"""
)

# contents
tab1, tab2, tab3 = st.tabs(["å¨åēĢæ°æ¤åē", "įæ¤įĨ", "æĨčŋæ¤įĨ"])

# tab1
tab1.write(
    """éčĻååãŽå¨åēĢæ°ãå¸¸ãĢæ¤åēããĻãæŦ åãé˛æ­ĸãããã"""
)
tab1.markdown("""
              - äģãĢããå¨åēĢæ°ãŽææĄãĢã¯ãæ§ããĒåãįĩãŋããã
                  - ééč¨ã§éããæ¸ŦåŽããåæ°ãææĄããã
                  - č˛ãŽæ§æãčĻãĻãæŖãįŠēããĻããããææĄããã
              """)
tab1.video("https://youtu.be/RdZtctqcI70")

# tab2
tab2.write(
    """įĢįŊå ąįĨå¨ã§ã¯æ¤åēã§ããĒããããĒãįãå°ãĒããŋã¤ããŽįĢįŊãæ¤åēããã"""
)

tab2.markdown("""
              - ææŗãŽé¸æčĸã¯ããã¤ãå­å¨
                  - įãįãį´æĨæ¤åēãã
                  - äŊãããŽį°å¸¸ãæ¤åēãã(Demo)
              """)

#tab2.video("https://www.youtube.com/shorts/s_9Iswp5M9w")
with tab2.container():
    tab2.video("data/smoke_predicted.mp4")

# tab3
tab3.write(
    """
    čščļįå˛¸æãĢãå°čšãããĒãããæ¤åēãããã
    
    ããĸã¨ããĻã¯ãčščļãŽæ¤įĨåãŗãæĨčŋãŽæ¤įĨãį¨æã
    """
)

tab3.video("https://youtu.be/12UHNXZvE7w")
