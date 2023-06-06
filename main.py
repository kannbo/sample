import streamlit as st
import pandas as pd
import numpy as np
a=[""]
b=[""]
st.title("hello")
text=st.text_input("入力","hello")
st.markdown(text)
a.append(text)
b=""
for i in a:
  b=b+i+"\n"
st.markdown(b)
