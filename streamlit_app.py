# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:15:05 2021

@author: robin
"""


import streamlit as st 
from PIL import Image
import login 
import SessionState as session
from google.cloud import firestore
from google.oauth2 import service_account
import json
#import streamlit_analytics


#Getting session state
state = session._get_state()

#Loading image resources 
favicon = Image.open('favicon.jpg')
home_bg = Image.open('home_bg.jpg')


#Setting up page configuration
st.set_page_config(page_title= 'apollo' , page_icon=favicon, layout='wide', initial_sidebar_state='auto') 

# Authenticate to Firestore 
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-algotrade")  
    
def load_home(state):
    
    # Laying out the homepage 
    home = st.empty() 
    col1 , col2 = st.beta_columns((7,2))
    back = col2.empty()
    
    
    # Building up the homepage
    if state.login:
        login.launch_login(state,db)
        back_click = back.button("< Go Back ")
        if back_click:
            state.login = False
            load_home(state)
                     
    else:
        with home.beta_container():
            col1, col2 = st.beta_columns((8,1.5))
            col1.markdown('<p style= "font-weight: bold; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True )
            clicked = col2.button("Get Started")
            st.markdown("<h1 style='text-align: center;'>Let's make some money</h1> <h4 style='text-align: center;'> But please don't kill us if you lose your money <h4><br> ", unsafe_allow_html=True
                     )
            left, middle,right = st.beta_columns((1,4,1))
            middle.image(home_bg, use_column_width= 1)
        
        if clicked:
            home.empty()
            login.launch_login(state,db)
            state.login = True

load_home(state)    
state.sync()   


    

        


        
        
