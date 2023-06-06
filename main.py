import streamlit as st
import pandas as pd
import numpy as np
a=[""]
b=[""]
st.title("hello")
text=st.text_area("入力","hello",5,10)
st.markdown(text)
a.append(text)
b=""
for i in a:
  b=b+i+"\n"
st.markdown(b)
