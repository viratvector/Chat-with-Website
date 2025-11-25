import streamlit as st

from streamlit_option_menu import option_menu

import account, chatbot

st.set_page_config(page_title="Chat with Website",)

class MultiApp:

    def __init__(self):
        self.apps = []
    
    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title = 'Chat with website',
                options=['Account', 'Chatbot'],
                icons = ['person-circle', 'robot'],
                menu_icon = 'chat-text-fill',
                default_index=1
            )
        
        # if app == 'Home':
        #     home.app()
        if app == 'Chatbot':
            chatbot.app()
        if app == 'Account':
            account.app()
        
        
    run()