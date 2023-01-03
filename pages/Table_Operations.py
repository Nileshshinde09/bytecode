import streamlit as st
import pandas as pd
from csv import writer
import sqlite3 
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

def view_all_users(c):
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def view_all_user_names():
    c.execute('SELECT username FROM userstable')
    data = c.fetchall()
    return data

def remove_users(username):
    c.execute("DELETE FROM userstable WHERE username=?",(username))
    conn.commit()


def showtable():
    table = view_all_users(c)
    df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","password"])
    df = df.iloc[:,:-1]
    st.table(df)
    if ('table_len' not in st.session_state):
	    st.session_state['table_len'] = len(df)-1

def table_main():
    
    try:
        # password = st.secrets['password']
        password = '9403'
        if password == st.session_state['password_ad']:
            st.title("List")
            
            if st.button('update'):
                showtable()
            else:
                showtable()
            username_i=st.text_input("Enter the index of the username you wish to remove from list:")
            if st.button('Remove'):
                try:
                    usernames = []
                    for user in view_all_user_names():
                        usernames.append(user[0])
                    if username_i in usernames or username_i !="nilesh":
                        remove_users(username_i)
                    else:
                        st.error("UserName is Not in list")

                except Exception:
                    pass
            st.header('Download Member List')
            with open('./data.db') as f:
                st.download_button('Download Database', f)
        else:
            st.info(
"""
You cant access this page
Login As Admin
""")

    except Exception:
        pass



