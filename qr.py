# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:14:43 2021

@author: robin
"""

import streamlit as st 
from PIL import Image

def pop_qr():
    qr = Image.open('qr_gpay.jpeg')
    with st.beta_container():
        st.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> almost there . . </p>', unsafe_allow_html=True)
        l,m,r = st.beta_columns((4,3,4))
        m.image(qr, use_column_width=1)
        col1,col2,col3 = st.beta_columns((2,5,2))
        col2.markdown('<p style= "text-align: center; font-family:Courier New;"> Pay a token of Rs. 1 to activate your account. Mention your username while paying. Upon payment, account will be activated within 2-4 hours </p>', unsafe_allow_html=True)
        col2.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> Happy Trading ! </p>', unsafe_allow_html=True)
        
