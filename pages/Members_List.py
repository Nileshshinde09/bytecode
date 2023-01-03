import streamlit as st
import pandas as pd


def view_all_users(c):
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def ml():
    import sqlite3 
    conn = sqlite3.connect("data.db", check_same_thread=False)
    c = conn.cursor()
    st.title("Members List")
    table = view_all_users(c)
    df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","password"])
    df = df.iloc[:,:-1]
    for index,i in enumerate(df['mobile_no']):
        i = str(i)
        df.iloc[index,3] =i[:4]+'XXXXXX'
    st.table(df)

