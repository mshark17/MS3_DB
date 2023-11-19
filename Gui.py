import streamlit as st
import mysql.connector
import pandas as pd

def connect_to_database():  
    mydb = mysql.connector.connect(
    host = "db4free.net",
    user = "mshark",
    password = "Mostafa23#",
    database = "wuzzuf900184043",
    )
    return mydb

def register_user(database):
    name=st.text_input("Enter Name: John Doe")
    email = st.text_input("Enter Email:")
    username = st.text_input("Enter User Name:")
    dateofbirth = st.text_input("Enter Date of Birth: YYYY-MM-DD")
    gender = st.text_input("Enter Gender: M or F")
    gpa = st.text_input("Enter GPA:")
    listofskills = st.text_input("Enter list of skills (seperate by comma and space): Skill1, Skill2")
    try:
        if st.button("Submit"):
            query= """
                INSERT INTO user VALUES (\'"""+email+"""\', \'"""+username+"""\', \'"""+gender+ """\', \'"""+dateofbirth+"""\',\'"""+gpa+"""\', \'"""+name+"""\')
                """
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                database.commit()
                st.subheader('user Added Succesfully!')
            except:
                st.subheader('ERROR')

            query= """
                INSERT INTO user_list_of_skills (List_Of_Skills,User_Name) VALUES (\'"""+listofskills+"""\',\'"""+username+"""\')
                """
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                database.commit()
                st.subheader('user_list_of_skills Added Succesfully!')
            except:
                st.subheader('ERROR')
    except:
        st.subheader('ERROR')
    return 

def appyForJob(database):
    query='''SELECT * FROM job_posting
        '''
    try:
        executeQuery = database.cursor()
        executeQuery.execute(query)
        # database.commit()
        output = pd.DataFrame(executeQuery.fetchall())
        output.columns = ['ID','CompanyID','Title','Salary','Experience Needed','Education Level','Career Level','Description']
        output['ID'] = output['ID'].astype(str)
        output['ID'] = output['ID'].str.replace(',', '')
        output['CompanyID'] = output['CompanyID'].astype(str)
        output['CompanyID'] = output['CompanyID'].str.replace(',', '')        
        st.subheader('Found '+ str(len(output)) + ' Job Postings')
        st.write(output)
        st.subheader("In Salary, '-1' means Confidential")
        jobID=st.text_input("Enter ID of the Job you want to apply to: Ex. 10011001")
        cv=st.file_uploader("Upload CV or Resume")
        if st.button("Submit"):
            st.subheader("You applied to Job:{}".format(jobID))
        # st.subheader('Query Succesful!')
    except:
        st.subheader('ERROR')

def showResults(database):
    st.subheader("Please Select which of the following results you would like to see")
    selection=st.selectbox('Select',('All the job postings for a given sector','All the job postings for a given set of skills',
                                     'The top 5 sectors by number of job posts and the average salary','The top 5 skills that are in the highest demand',
                                     'The top 5 growing startups','The top 5 most paying companies','All the postings for a given company/organization',
                                     'The top 5 categories'),index=1)
    if selection=='All the job postings for a given sector':
        companySector=st.text_input("Enter Sector:")
        if st.button("Submit"):
            query='''SELECT ID FROM company_sectors WHERE company_sectors LIKE "%{}%"
                    '''.format(companySector)
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                companyIDs=pd.DataFrame(executeQuery.fetchall())
                companyIDs.columns=['ID']
                companyIDs['ID'] = companyIDs['ID'].astype(str)
                companyIDs['ID'] = companyIDs['ID'].str.replace(',', '')
                # st.subheader(companyIDs['ID'][0])
            except:
                print("Error! Couldn't find companies")
            # listofPosts=pd.DataFrame()
            # listofPosts.columns = ['ID','CompanyID','Title','Salary','Experience Needed','Education Level','Career Level','Description']
            if len(companyIDs)>1:
                query='''SELECT * FROM job_posting WHERE (job_posting.CompanyID="{}"'''.format(companyIDs['ID'][0])
                for i in companyIDs['ID'][1:]:
                    query+=''' OR job_posting.CompanyID="{}"'''.format(i)
                query+=')'
            else:
                query='''SELECT * FROM job_posting WHERE (job_posting.CompanyID="{}")'''.format(companyIDs['ID'][0])
            # st.subheader(query)
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                output=pd.DataFrame(executeQuery.fetchall())
                output.columns = ['ID','CompanyID','Title','Salary','Experience Needed','Education Level','Career Level','Description']
                output['ID'] = output['ID'].astype(str)
                output['ID'] = output['ID'].str.replace(',', '')
                output['CompanyID'] = output['CompanyID'].astype(str)
                output['CompanyID'] = output['CompanyID'].str.replace(',', '') 
                st.subheader('Found '+ str(len(output)) + ' Job Postings')
                st.write(output) 
                st.subheader("In Salary, '-1' means Confidential")
            except:
                print("Error! Couldn't fetch posts from job_posting")
    elif selection=='All the job postings for a given set of skills':
        temp=st.text_input("Enter skills sperated by comma followed by a space: Ex. Skill1, Skill2")
        if st.button("Submit"):
            listOfskills=temp.split(', ')
            if len(listOfskills)>1:
                query=''' SELECT ID FROM job_posting_required_skills WHERE ( Required_Skills LIKE "%{}%"
                    '''.format(listOfskills[0])
                for i in listOfskills[1:]:
                    query+= ''' OR Required_Skills LIKE "%{}%'''.format(i)
                query+=')'
            else:
                query='''SELECT ID FROM job_posting_required_skills WHERE ( Required_Skills LIKE "%{}%")'''.format(listOfskills[0])
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                postIDs=pd.DataFrame(executeQuery.fetchall())
                postIDs.columns=['ID']
                postIDs['ID'] = postIDs['ID'].astype(str)
                postIDs['ID'] = postIDs['ID'].str.replace(',', '')
                # st.subheader(companyIDs['ID'][0])
            except:
                print("Error! Couldn't find companies")
            st.subheader(len(postIDs))
            if len(postIDs)>1:
                query='''SELECT * FROM job_posting WHERE (job_posting.ID="{}"'''.format(postIDs['ID'][0])
                for i in postIDs['ID'][1:]:
                    query+=''' OR job_posting.ID="{}"'''.format(i)
                query+=')'
            else:
                query='''SELECT * FROM job_posting WHERE (job_posting.ID="{}")'''.format(postIDs['ID'][0]) 
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                output=pd.DataFrame(executeQuery.fetchall())
                output.columns = ['ID','CompanyID','Title','Salary','Experience Needed','Education Level','Career Level','Description']
                output['ID'] = output['ID'].astype(str)
                output['ID'] = output['ID'].str.replace(',', '')
                output['CompanyID'] = output['CompanyID'].astype(str)
                output['CompanyID'] = output['CompanyID'].str.replace(',', '')  
                st.subheader('Found '+ str(len(output)) + ' Job Postings')
                st.write(output) 
                st.subheader("In Salary, '-1' means Confidential")
            except:
                print("Error! Couldn't fetch posts from job_posting")
    elif selection=='The top 5 sectors by number of job posts and the average salary':
        pass
    elif selection=='the top 5 skills that are in the highest demand':
        pass
    elif selection=='The top 5 growing startups':
        pass
    elif selection=='The top 5 most paying companies':
        pass
    elif selection=='All the postings for a given company/organization':
        companyName=st.text_input("Enter Company/Organization name:")
        if st.button("Submit"):
            query='''SELECT ID FROM company WHERE company.Name="{}"'''.format(companyName)
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                companyID=executeQuery.fetchone()[0]
                # st.subheader(companyID)
            except:
                print("Error! Can't find companyID!")
            query='''SELECT * FROM job_posting WHERE job_posting.CompanyID="{}"
                '''.format(companyID)
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                output=pd.DataFrame(executeQuery.fetchall())
                output.columns = ['ID','CompanyID','Title','Salary','Experience Needed','Education Level','Career Level','Description']
                output['ID'] = output['ID'].astype(str)
                output['ID'] = output['ID'].str.replace(',', '')
                output['CompanyID'] = output['CompanyID'].astype(str)
                output['CompanyID'] = output['CompanyID'].str.replace(',', '')        
                st.subheader('Found '+ str(len(output)) + ' Job Postings')
                st.write(output)
                st.subheader("In Salary, '-1' means Confidential")
            except:
                print("Error! Can't find Job Postings!")
            # companyID=executeQuery
            # query
    elif selection=='The top 5 categories':
        pass

if __name__=="__main__":
    database=connect_to_database()
    st.write ('''
    # Milestone 3 Database Project
    ''')
    st.sidebar.header("Navigation")
    navi=st.sidebar.selectbox('Choose',  ('Register a user', 'Apply for Job', 'Results'), index=1)
    if navi=="Register a user":
        register_user(database)
    elif navi=="Apply for Job":
        appyForJob(database)
    elif navi=="Results":
        showResults(database)