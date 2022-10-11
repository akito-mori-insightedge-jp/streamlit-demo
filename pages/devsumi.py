# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import inspect
import textwrap
import time
import numpy as np
from utils import show_code

def devsumi():
    #progress_bar = st.sidebar.progress(0)
    #status_text = st.sidebar.empty()
    #last_rows = np.random.randn(1, 1)
    #chart = st.line_chart(last_rows)

    #progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    #st.button("Re-run")
    st.video("https://www.youtube.com/watch?v=eWNOaEbxhd4")


st.set_page_config(page_title="ComputerVision Demo", page_icon="")
st.markdown("# ComputerVision Demo")
st.sidebar.header("Demo")
st.write(
    """あああ"""
)

devsumi()

#show_code(plotting_demo)
