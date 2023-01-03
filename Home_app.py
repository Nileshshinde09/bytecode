from question import question
from snippet import snippet
import streamlit as st
from streamlit_option_menu import option_menu
from pages.About import about
from pages.Members_List import ml
from pages.Table_Operations import table_main
from pages.main_page import main_method
from pages.user_authenticaton import main


if __name__=="__main__":

    st.set_page_config(
        page_title="Bytecode Velocity",
        page_icon="📚",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"}
    )
    # hide_menu_style ="""
    #         <style>
    #          #MainMenu {visibility: hidden;}
    #          </style>
    #          """

    # st.markdown(hide_menu_style, unsafe_allow_html=True)
    no_sidebar_style = """
    <style>
        div[data-testid="collapsedControl"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
    if ('loggedin_name' not in st.session_state):
        st.session_state['loggedin_name'] = 0
    def streamlit_menu1():
        selected = option_menu(
        menu_title=None,  # required
        options=["Log in/Log out","Home", "Members List","Table Operations","Sign Up","About","Exit"],  # required
        icons=["login","house", "list", "table operations", "about","sign up","exit"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        )
        return selected
    def streamlit_menu2():
        selected = option_menu(
        menu_title=None,  # required
        options=["Sign Up","Login/Logout","Home", "Members List","About","Exit"],  # required
        icons=["sign up","login","house", "list", "about","exit"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        )
        return selected

    def streamlit_user():
        selected = option_menu(
		menu_title=None,  # required
		options=["Sign Up","Login"],  # required
		icons=["sign up","login"],  # optional
		menu_icon="cast",  # optional
		default_index=0,  # optional
		orientation="horizontal",
		)
        return selected
    if ('username_login' not in st.session_state):
        st.session_state['username_login'] = 0
    if ('ans' not in st.session_state):
        st.session_state['ans'] = 0
    if st.session_state['loggedin_name'] != 0:
        st.header(f"Welcome {st.session_state['loggedin_name']}")
    else:
        pass

    # page_authenticator()

    selected =streamlit_menu1()
    try:
        if selected == "Sign Up" or selected == "Log in/Log out":
            try:
                main(selected)           
            except Exception :
                pass

        if selected == "Home":
            try:
                
                main_method()
            except Exception :
                pass
        if selected == "About":
            about()
        if selected == "Members List":
            ml()
            pass
        if selected == "Table Operations":
            try:
                table_main()
                pass
            except Exception :
                pass    
        if selected =="Exit":
            st.markdown("""
                <meta http-equiv="refresh" content="0; url='https://www.google.com'" />
                """, unsafe_allow_html=True
            )
    except Exception:
        pass



