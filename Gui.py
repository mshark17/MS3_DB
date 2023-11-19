import streamlit as st
import mysql.connector
import pandas as pd
import datetime
import re

pattern = r'\d{4}-\d{2}-\d{2}'

def connect_to_database():  
    mydb = mysql.connector.connect(
    host = "db4free.net",
    user = "mshark",
    password = "Mostafa23#",
    database = "wuzzuf900184043",
    )
    return mydb

def register_user(mydb):
    
    user_email = st.text_input("Enter User Email:")
    user_dob = st.text_input("Enter DOB: YYYY-MM-DD")
    user_name = st.text_input("Enter User Name:")
    gender = st.text_input("Enter Gender: M or F")
    
    pattern = r'\d{4}-\d{2}-\d{2}'

    match = re.match(pattern, user_dob)


    if(match):
        dob_date = datetime.datetime.strptime(user_dob, '%Y-%m-%d')

        today = datetime.date.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    
    try:
        if st.button("Submit"):
            
            query= """
                INSERT INTO user VALUES (\'"""+user_email+"""\', \'"""+user_dob+ """\', \'"""+user_name+"""\',\'"""+str(age)+"""\', \'"""+gender+"""\')
                """
            
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                mydb.commit()
                st.subheader('User Added Succesfully!')
            except:
                st.subheader('ERROR')
    except:
        st.subheader('ERROR')
    return 

if __name__=="__main__":
    register_user(connect_to_database())