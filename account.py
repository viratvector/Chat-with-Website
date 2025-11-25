import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('chat-with-website.json')
firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to :violet[Chat with Website]')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f():
        try:
            user = auth.get_user_by_email(email)
            st.write('Login Successfull')
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            st.session_state.loggedout = True
            st.session_state.logout = True
        except:
            st.warning('Login Failed')
    
    def t():
        st.session_state.logout = False
        st.session_state.loggedout = False
        st.session_state.username = ''

    if 'loggedout' not in st.session_state:
        st.session_state.loggedout = False

    if 'logout' not in st.session_state:
        st.session_state.logout = False

    if not st.session_state['loggedout']:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

        if choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type = 'password')

            st.button('Login', on_click=f)
        else:
            username = st.text_input('Name')
            email = st.text_input('Email Address')
            password = st.text_input('Password', type = 'password')

            if st.button('Create My Account'):
                user = auth.create_user(email = email, password = password, uid = username)
                st.success('Account created successfully!')
                st.markdown('Please login using your email and password')
                st.balloons()
    
    if st.session_state.logout:
        st.text('Name : '+st.session_state.username)
        st.text('Email : '+st.session_state.useremail)
        st.button('Sign out', on_click=t)