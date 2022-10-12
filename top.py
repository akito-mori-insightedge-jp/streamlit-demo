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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Top Page",
        page_icon="IE",
    )

    st.write("# デモ　置き場")

    st.sidebar.success("Select a demo above.")

    st.markdown(
    """
        これまでに作成したデモや資料、動画を掲載しています。
        左のサイドバーから興味のあるコンテンツを選択してください。
    """
    )


if __name__ == "__main__":
    run()
