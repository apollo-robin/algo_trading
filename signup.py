# -*- coding: utf-8 -*-
"""
Created on Sun May 23 06:58:13 2021

@author: robin
"""

# Import required libraries
import streamlit as st 
from PIL import Image
import login
import qr
import time


def launch_signup(state,db):
           
    @st.cache(show_spinner=False)
    def user_exists(username):
        data_ref = db.collection("users").document(username)
        data = data_ref.get()
        if data.exists:
            return True
        else:
            return False
            
    
    # Load image resources 
    signup_img = Image.open('signup.jpg')
        
    # Laying out page
    signup = st.empty()
    
    with signup.beta_container():
        col3, col2, col1, col4 = st.beta_columns((2,0.05,1,0.2))
        col1.markdown('<p style= "color: #1f4886; font-family:Segoe Script; font-size:30px; font-weight: bold"> Welcome, join us <p>', unsafe_allow_html=True )
        col3.markdown('<p style= "font-weight: bold; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True )
        col1.markdown("Enter your details to continue", unsafe_allow_html=True)
        
        col32, col22, col12, col42 = st.beta_columns((2,0.05,1,0.2))
        col32.image(signup_img, use_column_width=1)
        
        with col12.form("signup_form"):
            email = st.text_input("Email")
            username = st.text_input("Username")
            password= st.text_input("Password", type ='password')
            confirm_pass = st.text_input("Re-Enter Password")
            submit = st.form_submit_button("Sign Up")
            error_msg = st.empty()
        
        col12.markdown("Already have an account ?")
        signin_button = col12.button("Sign In")        
                
    if submit:
        if email == '' or username == '' or password =='' or confirm_pass =='':
            error_msg.error("Fill in missing fields")
            st.stop()
        if not password == confirm_pass:
            error_msg.error("Passwords do not match")
            st.stop()
        user_info = user_exists(username)
        
        if user_info == False:
            user_info = db.collection("new_users").document(username)
            user_info.set({"passwored": password, "email":email})
            error_msg.success("Account created successfully") 
            time.sleep(4)
            signup.empty()
            qr.pop_qr()
        else:
           error_msg.error("Username taken") 
    
    if signin_button:
        signup.empty()
        state.signup_form = False
        login.launch_login(state,db)
               
    state.sync()

    