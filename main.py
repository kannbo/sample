import streamlit as st
import pandas as pd
import numpy as np
a=[""]
b={}
st.title("hello")
text=st.text_area("入力","hello",5,1000)
if st.button("hello"):
    st.markdown(eval(text,globals(),b))
    a.append(text)
b=""
for i in a:
  b=b+i+"\n"
st.markdown(b)
