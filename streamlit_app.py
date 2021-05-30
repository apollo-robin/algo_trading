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
import base64
#import streamlit_analytics


#Getting session state
state = session._get_state()

#Loading media resources 
favicon = Image.open('favicon.jpg')
demo = Image.open('app_demo.png')
backtest = Image.open('back_test.png')
img_1 = Image.open('un_1.png')
img_2 = Image.open('un_2.png')
img_3 = Image.open('un_3.png')



#Setting up page configuration
st.set_page_config(page_title= 'apollo' , page_icon=favicon, layout='wide', initial_sidebar_state='auto') 


# Loading gif
file_ = open("head_gif.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


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
            
            logo, start = st.beta_columns((6,1))
            
            click1 = start.button("Get Started")
            logo.markdown('<p style= "font-weight: bold; text-align:left; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True)
            
            st.markdown(f'<img width="100%" src="data:image/gif;base64,{data_url}">', unsafe_allow_html=True,)
            
            with st.beta_container():
                st.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 36px"> <br>How apollo helps you trade better <p>', unsafe_allow_html=True)
                st.markdown('<p style= "text-align:center; color: black; font-size: 16px"> With our expert trading algorithms, anyone can trade in a more <br> disciplined manner free from emotional decisions  <p>', unsafe_allow_html=True)
                
                col1 , col2 , col3 = st.beta_columns(3)
                col1.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 28px"> Choose Strategies <p>', unsafe_allow_html=True)
                col2.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 28px"> Factor in Risk <p>', unsafe_allow_html=True)
                col3.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 28px"> Get buy-sell Signals <p>', unsafe_allow_html=True)
                
                
                
                col1.image(img_1, use_column_width= True)
                col2.image(img_2, use_column_width= True)
                col3.image(img_3, use_column_width= True)
                
                
                
                col1.markdown('<p style= " text-align:center; color: black;  font-size: 14px"> Choose from a rich collection of     intelligent strategies. Just not implement, but understand the principles beneath each strategy  <p>', unsafe_allow_html=True)           
                
                col2.markdown('<p style= " text-align:center; color: black; font-size: 14px"> Tell us your risk appetite and we will take care of the rest. Our platform protects you from market volatility and turbulences <p>', unsafe_allow_html=True)
                
                col3.markdown('<p style= " text-align:center;color: black; font-size: 14px"> With just one-click you get the best trades for the day suited to your risk and investment amount  <p>', unsafe_allow_html=True)
            
            with st.beta_container():
                st.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 36px"> <br> Everything packed at one place <p>', unsafe_allow_html=True)
                st.markdown('<p style= "text-align:center; color: black; font-size: 16px"> Charts, Indicators, Strategies, Financials and a lot more ,<br> in one simple Dashboard  <p>', unsafe_allow_html=True)
                demo_1, demo_2, demo_3 = st.beta_columns((1,7,1))
                demo_2.image(demo, use_column_width= True)
            
            with st.beta_container():
                st.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 36px"> <br>Test it before you take it <p>', unsafe_allow_html=True)
                st.markdown('<p style= "text-align:center; color: black; font-size: 16px"> So, you cannot just trust our strategies <br> and put your money in ? No issues  <p>', unsafe_allow_html=True)
                
                back1 , back2, back3 = st.beta_columns((2,6,2))
                back2.image(backtest, use_column_width = 1)
                
                  
                col11 , col12 ,col_m, col13 , col14 = st.beta_columns((1,4,1,4,1))
                col12.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 28px"> Paper Trading <p>', unsafe_allow_html=True)
                col12.markdown('<p style= " text-align:center;color: black; font-size: 14px"> Simulate your chosen strategy with virtual money to get real trade dynamics in real time and make better trading decisions  <p>', unsafe_allow_html=True)
                
                
                
                col13.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 28px">  Backtesting <p>', unsafe_allow_html=True)
                col13.markdown('<p style= " text-align:center;color: black; font-size: 14px"> Test your chosen strategy on historical market data and get a clearer picture on the strategy’s performance in real scenarios <p>', unsafe_allow_html=True)
            
            st.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 28px"> <br> We have got something for everyone , from learners to experts !<p>', unsafe_allow_html=True)
            col31 , col32, col33 = st.beta_columns((5.4,3,4))
            click2 = col32.button("Get Started", key = 43543)
            
            st.markdown("***", unsafe_allow_html=True)
            
            b1,b2 ,b3 = st.beta_columns(3)
            b1.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-family:Segoe Script; font-size: 44px"> apollo <p>', unsafe_allow_html=True)
            b2.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-size: 20px"> About Us <p>', unsafe_allow_html=True)
            b3.markdown('<p style= "font-weight: bold; text-align:center; color: #1f4886; font-size: 20px"> Contact <p>', unsafe_allow_html=True)
            b3.markdown('<p style= "text-align:center; color: #1f4886;" >  +91 8789835022 <br>  robinraj055@gmail.com <br> <p>', unsafe_allow_html=True)
            
            
                                                   
            st.markdown("***", unsafe_allow_html=True)
            st.markdown('<p style= "font-family:Calibri; color: black; text-size:20px; ">Disclaimer: Apollo is meant to be a teachnology provider platform and does not act/intent to act as a wealth manger in any capacity. We are not a Wealth Advisor/Investment Advisor/Portfolio Managment Service or any similar service affiliated to stock markets. Every selection/transaction placed is solely the responsiblity of the user. Please ensure that you fully understand the risks involved <p>', unsafe_allow_html= True)
      
            
        if click1 or click2:
                home.empty()
                login.launch_login(state,db)
                state.login = True
        
    if state.logged_in:
        home.write("")

load_home(state)    
state.sync()   


    

        


        
        
