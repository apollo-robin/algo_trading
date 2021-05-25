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
    
        
def go_premium(state):
    qr = Image.open('qr_gpay.jpeg')
    premium_page = st.empty()
    with premium_page.beta_container():
        st.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> Upgrade to premium now </p>', unsafe_allow_html=True)
        l,m,r = st.beta_columns((4,3,4))
        m.image(qr, use_column_width=1)
        col1,col2,col3 = st.beta_columns((1,6,1))
        col2.markdown('<p style= "text-align: center; font-family:Courier New;"> Enjoy all premium features at just <span style ="font-weight:bold;"> Rs. 99 </span> a month.<br> Mention your username while paying. </p>', unsafe_allow_html=True)
         
        paid = col2.checkbox("I have made the required transaction to enjoy premium features")
        
        lb,mb,rb = st.beta_columns((4,3,4))
        if paid:
            state.paid = True
        if not paid:
            state.paid = False
        proceed = mb.button("Upgrade my account")
        
    return proceed , premium_page   
       

def confirm_pay(state):
    confirm = st.empty()
    with confirm.beta_container():
        st.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> <br> Welcome to our Premiere club <br><br><br></p>', unsafe_allow_html=True)
        l,m,r = st.beta_columns((4,6,4))
        transID = m.text_input("Just enter your Transaction ID")
        if transID != "":
            state.transID = True
            
        upgrade = m.checkbox("I Confirm")
        col1,col2,col3 = st.beta_columns((1,6,1))
        col2.markdown('<p style= "text-align: center; font-family:Courier New;"> We will upadate your account status within 2-4  hrs. </p>', unsafe_allow_html=True)
        
    return upgrade , confirm


def thankyou(state):
    thanks = st.empty()
    with thanks.beta_container():
        st.markdown('<p style="text-align: center;font-size:30px;font-family:Segoe Script"> <br><br><br> Welcome to our Premiere club <br></p>', unsafe_allow_html=True)
        st.markdown('<p style= "text-align: center; font-family:Courier New;"> We will upadate your account status within 2-4  hrs.<br><br><br><br> </p>', unsafe_allow_html=True)
        col1, col2, col3 = st.beta_columns((4,1,4))
        cancel = col2.button("Close")
        if cancel:
            thanks.empty()
        