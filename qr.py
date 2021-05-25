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
    
        
def go_premium(state, premium_page):
    qr = Image.open('qr_gpay.jpeg')
    #premium_page = st.empty()
    with premium_page.beta_container():
        st.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> Upgrade to premium now </p>', unsafe_allow_html=True)
        l,m,r = st.beta_columns((4,3,4))
        m.image(qr, use_column_width=1)
        col1,col2,col3 = st.beta_columns((1,6,1))
        col2.markdown('<p style= "text-align: center; font-family:Courier New;"> Enjoy all premium features at just <span style ="font-weight:bold;"> Rs. 99 </span> a month.<br> Mention your username while paying. </p>', unsafe_allow_html=True)
        col11,col12,col13 = st.beta_columns((1,6,1)) 
        paid = col12.checkbox("I have made the required transaction to enjoy premium features")
        
        lb,mb,rb = st.beta_columns((4,3,4))
        if paid:
            state.paid = True
        if not paid:
            state.paid = False
        proceed = mb.button("Upgrade my account")
        
    return proceed 

def confirm_pay(state, confirm):
    #confirm = st.empty()
    with confirm.beta_container():
        st.markdown('<p> <br><br><br></p>', unsafe_allow_html=True)
        l,m,r = st.beta_columns((4,6,4))
        transID = m.text_input("Just enter your Transaction ID")
        upgrade = m.checkbox("I Confirm")
        if transID != "":
            state.transID = True
        col1,col2,col3,col4 = st.beta_columns((1,0.1,2,1))
        col2.empty()  
        col11,col12,col13 = st.beta_columns((1,6,1)) 
        col12.empty()
        lb,mb,rb = st.beta_columns((4,3,4))
        mb.empty()
        if upgrade and transID == '':
            col3.success("Please enter Transaction ID")
            st.stop()
    return upgrade , transID


def thankyou(state, thanks):
    #thanks = st.empty()
    with thanks.beta_container():
        st.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> <br><br><br> Welcome to our Premiere club <br></p>', unsafe_allow_html=True)
        l,m,r = st.beta_columns((1,6,1))
        m.markdown('<p style= "text-align: center; font-family:Courier New;"> We will update your account status within 2-4  hrs.<br><br><br> </p>', unsafe_allow_html=True)
        m.empty()
        col1, col2, col3 = st.beta_columns((1,6,1))
        col2.markdown('<p style ="text-align:center;"> Uncheck Premium to close <p>',unsafe_allow_html= True)
      