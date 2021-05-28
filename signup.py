# -*- coding: utf-8 -*-
"""
Created on Sun May 23 06:58:13 2021

@author: robin
"""

# Import required libraries
import streamlit as st 
from PIL import Image
import login
from datetime import date


def launch_signup(state,db):
           
    @st.cache(show_spinner=False)
    def user_exists(username):
        data_ref1 = db.collection("users").document(username)
        data1 = data_ref1.get()
        if data1.exists:
            return True
        else:  
            return False      
        
            
    
    # Load image resources 
    signup_img = Image.open('signup.jpg')
        
    # Laying out page
    signup = st.empty()
    
    with signup.beta_container():
        col3, col2, col1, col4 = st.beta_columns((2,0.05,1.1,0.1))
        col1.markdown('<p style= "color: #1f4886; font-family:Segoe Script; font-size:30px; font-weight: bold"> Welcome, join us <p>', unsafe_allow_html=True )
        col3.markdown('<p style= "font-weight: bold; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True )
        col32, col22, col12, col42 = st.beta_columns((2,0.05,1.1,0.1))
        col32.image(signup_img, use_column_width=1)
        col12.markdown("Enter your details to continue", unsafe_allow_html=True)
        
        
        
        with col12.form("signup_form"):
            email = st.text_input("Email")
            username = st.text_input("Username")
            password= st.text_input("Password", type ='password')
            confirm_pass = st.text_input("Re-Enter Password", type ='password')
            submit = st.form_submit_button("Sign Up")
            error_msg = st.empty()
            trans_msg = st.empty()
        
        col12.markdown("Already have an account ?")
        signin_button = col12.button("Sign In") 
        
        
    
         
    if submit or state.signup_submit: 
        if email == '' or username == '' or password =='' or confirm_pass =='':
            error_msg.error("Fill in missing fields")
            st.stop()
        if not password == confirm_pass:
            error_msg.error("Passwords do not match")
            st.stop()
        if " " in username:
            error_msg.error("Username must not contain spaces")
            st.stop()
        if len(password) < 8:
            error_msg.error("Password must be atleast 8 characters")
            st.stop()
        
        user_info = user_exists(username)
        
        if user_info == False :
            user_info = db.collection("users").document(username)
            sign_date = date.today().strftime("%d-%m-%Y")
            user_info.set({"password": password, "email":email, "signed on": sign_date})
            error_msg.success("Account created successfully") 
                    
        else:
           error_msg.error("Username taken") 
           trans_msg.markdown('<p style ="font-size:14px; font-style: Courier New;"> Check if you signed up but couldn\'t complete the payment<p>', unsafe_allow_html = True)
               
        
    if signin_button:
        signup.empty()
        state.signup_form = False
        login.launch_login(state,db)
               
    state.sync()

    