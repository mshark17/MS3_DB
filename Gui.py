import streamlit as st
import mysql.connector
import pandas as pd
import datetime
import re

pattern = r'\d{5}-\d{5}-\d{5}'

def connect_to_database():  
    mydb = mysql.connector.connect(
    host = "db4free.net",
    user = "mshark",
    password = "Mostafa23#",
    database = "wuzzuf900184043",
    )
    return mydb

def register_user(mydb):
    
    email = st.text_input("Enter Email:")
    username = st.text_input("Enter User Name:")
    dateofbirth = st.text_input("Enter Date of Birth: YYYY-MM-DD")
    gender = st.text_input("Enter Gender: M or F")
    gpa = st.text_input("Enter GPA:")
    temp = st.text_input("Enter list of skills (seperate by comma and space): Skill1, Skill2")
    listofskills = temp.split(", ")
    
    pattern = r'\d{5}-\d{5}-\d{5}'

    match = re.match(pattern, dateofbirth)


    if(match):
        dob_date = datetime.datetime.strptime(dateofbirth, '%Y-%m-%d')

        today = datetime.date.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    
    try:
        if st.button("Submit"):
            
            query= """
                INSERT INTO user VALUES (\'"""+email+"""\', \'"""+dateofbirth+ """\', \'"""+username+"""\', \'"""+gender+"""\', \'"""+gpa+"""\', \'"""+listofskills+"""\')
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