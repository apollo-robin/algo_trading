# -*- coding: utf-8 -*-
"""
Created on Sun May 23 05:03:03 2021

@author: robin
"""

# Import required libraries
import streamlit as st 
from PIL import Image
import dashboard as sd
import signup



def launch_login(state,db):
    
    @st.cache(show_spinner=False)
    def get_user_info(username):
        data_ref = db.collection("users").document(username)
        data = data_ref.get()
        if not data.exists:
            return False
        else:
            data = data.to_dict()
            return data
    
    if state.logged_in :
        sd.start_dashboard(state)  
        
    elif state.signup_form :
        signup.launch_signup(state,db)
        
    else:
        # Load image resources 
        login_img = Image.open('login.png')
        
        # Laying out page
        login = st.empty()
        
        with login.beta_container():
            col1, col2, col3, col4 = st.beta_columns((2,0.05,1,0.5))
            col1.markdown('<p style= "font-weight: bold; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True  )
            col3.markdown('<h1 style= "color: #1f4886;font-family:Segoe Script;font-size:30px; font-weight: bold"> Sign in to apollo <h1>', unsafe_allow_html=True )
            col3.markdown("Enter your details to continue", unsafe_allow_html=True)
            
            col12, col22, col32, col42 = st.beta_columns((2,0.05,1,0.5))
            col12.image(login_img, use_column_width=1)
            
            with col32.form("login_form"):
                username_login = st.text_input("Username")
                password_login = st.text_input("Password", type ='password')
                submit_login = st.form_submit_button("Sign In")
                error_msg_login = st.empty()
            
            col32.markdown("Don't have an account ?")
            signup_button = col32.button("Sign Up")
                
        if submit_login :
            if username_login == '' or password_login == '':
                error_msg_login.error("Missing username or password")
                st.stop()
                
            user_info = get_user_info(username_login)
            if user_info == False:
                error_msg_login.error("Invalid credentials")
               
            elif user_info["password"] == password_login:
                login.empty()
                state.logged_in = True
                state.user = username_login
                sd.start_dashboard(state)  
            
            else:
                error_msg_login.error("Invalid credentials")
                
        if signup_button:
            login.empty()
            state.signup_form = True
            signup.launch_signup(state,db)
        
        
        state.sync()
    