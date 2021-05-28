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

#Loading media resources 
favicon = Image.open('favicon.jpg')
home_bg = Image.open('home_bg.jpg')
demo = Image.open('app_demo.png')


#Setting up page configuration
st.set_page_config(page_title= 'apollo' , page_icon=favicon, layout='wide', initial_sidebar_state='auto') 


# Authenticate to Firestore 
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-algotrade")  
    
def load_home(state):
    
    # Laying out the homepage 
    home = st.empty() 
     
    
    # Building up the homepage
    if state.login:
        login.launch_login(state,db)
        back_click = home.button("< Go Back ")
        if back_click:
            state.login = False
            load_home(state)
                     
    else:
        with home.beta_container():           
            
            clicked = st.button("Get Started")
            st.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True)
            #st.markdown("![Alt Text](https://media.giphy.com/media/zcsNOwAimBbd5okbQM/giphy.gif)")
            
            top1 ,top2 , top3 = st.beta_columns((4,2,4))
            top1.markdown('<p style="font-weight: bold; text-align:center;font-family:Segoe Script; font-size:30px"> Let’s make some money  <p>', unsafe_allow_html= True)
            top1.markdown('<p style="text-align:center; font-size:16px; font-family:Calibri"> Leverage Algorithmic Trading Strategies to enhance your returns from the capital market  <p>', unsafe_allow_html= True)
            
            top3.markdown('<p style="font-weight: bold; text-align:center;font-family:Segoe Script; font-size:30px"> Save time and effort <p>', unsafe_allow_html= True)
            top3.markdown('<p style="text-align:center; font-size:16px; font-family:Calibri"> We do all the analysis for you, so you  don’t have to. Get buy-sell signals for trading <p><br>', unsafe_allow_html= True)
            
            
            top11 ,top12 , top13 = st.beta_columns((2,4,2))
            top12.markdown('<p style="font-weight: bold; text-align:center;font-family:Segoe Script; font-size:30px"> Trade. Grow. Repeat  <p>', unsafe_allow_html= True)
            top12.markdown('<p style="text-align:center; font-size:16px; font-family:Calibri">Our strategies are backtested with historical data for risk management and return maximization  <p>', unsafe_allow_html= True)
            
            l, m,r = st.beta_columns((1,4,1))
            m.image(home_bg, use_column_width= 1)
            
            
            st.markdown('<p style="text-align:center;font-family:Segoe Script; font-size:30px"> <br> How does apollo help you trade <br> <p>', unsafe_allow_html= True)
            
            
            left, middle,right = st.beta_columns((1,6,1))
            middle.image(demo, use_column_width= 1)
            
            st.markdown('<p style="text-align: center"> With our tried and tested formula, anyone can now bet in the capital markets<br> <p>', unsafe_allow_html= True)
            
            beg , exp = st.beta_columns(2)
            beg0, beg1 , beg2, exp0, exp1 , exp2 = st.beta_columns((1,4,1,1,4,1))
            beg.markdown('<p style="text-align:center;font-family:Segoe Script; font-weight:bold; font-size:20px"> <br>For those who are starting <p>', unsafe_allow_html= True)
            beg1.markdown('<p style= "font-family:Calibri; text-size:20px; ">*Get direct buy-sell signals<br> *Learn algorithms as you trade with our blog posts<p>',unsafe_allow_html= True)
            
            exp.markdown('<p style="text-align:center;font-family:Segoe Script;font-weight:bold; font-size:20px"><br>For the experienced ones <p>', unsafe_allow_html= True)
            exp1.markdown('<p style= "font-family:Calibri; text-size:20px; ">* Build your own strategy <br>                     * Backtest your developed strategy for risk mgmt. <p> <br>',unsafe_allow_html= True)
            
            col31 , col32, col33 = st.beta_columns((5,3,4))
            clicked = col32.button("Get Started", key = 43543)
            
            st.markdown("***", unsafe_allow_html=True)
            
            b1,b2 ,b3 = st.beta_columns(3)
            b1.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True)
            b2.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-size: 20px"> About Us <p>', unsafe_allow_html=True)
            b3.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-size: 20px"> Contact <p>', unsafe_allow_html=True)
            b3.markdown('<p style= "text-align:center; color: #1f4886;" > Call: +91 8789835022 <br> Mail: robinraj055@gmail.com <br> Apollo Ltd. Patna,Bihar <p>', unsafe_allow_html=True)
            
            
                                                   
            st.markdown("***", unsafe_allow_html=True)
            st.markdown('<p style= "font-family:Calibri; text-size:20px; ">Disclaimer: Apollo is meant to a teachnology provider platform and does not act/intent to act as a wealth manger in any capacity. We are not a Wealth Advisor/Investment Advisor/Portfolio Managment Service or any similar service affiliated to stock markets. Every selection/transaction places is solely the responsiblity of the user. Please ensure that you fully understand the risks involved <p>', unsafe_allow_html= True)
      
            
        if clicked:
                home.empty()
                login.launch_login(state,db)
                state.login = True
        
        if state.logged_in:
            home.empty()

load_home(state)    
state.sync()   


    

        


        
        
