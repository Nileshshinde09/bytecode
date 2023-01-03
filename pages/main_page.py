from question import question
from snippet import snippet
import streamlit as st
from streamlit_ace import st_ace
import sys
from csv import writer


class main_method:
    def __init__(self) -> None:
        
        def run(code,year):
            code_part = code
            try:
                if year =='1':
                    inputfile = './static/file_first.txt'
                elif year =='2':
                    inputfile = './static/file_second.txt'
                else :
                    inputfile = './static/file_third.txt'
                orig_stdout = sys.stdout
                sys.stdout = open(inputfile, 'w')
                exec(code_part)
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = open(inputfile, 'r').read()
            except Exception as e:
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = e
            return output
        def submit(year,code):

            if year =='1':
                inputfile = './static/file_first_temp.txt'
            elif year =='2':
                inputfile = './static/file_second_temp.txt'
            else :
                inputfile = './static/file_third_temp.txt'
            output = open(inputfile, 'r').read()
            if output ==run(code,year):
                return 1
        st.title("Enter Information")
        
        Semester = st.selectbox("Choose Semester",['I','II' ,'III','IV' ,'V' ,'VI' ],key="non_uas")
        name =st.text_input("Enter Name ",key="non_uan")
        mobile_no = st.text_input("Enter Mobile No. ",value="+91",max_chars=13,key="non_uam")
        if 'I' ==Semester or 'II' ==Semester:
            year = '1'
        elif 'III' ==Semester or 'IV' ==Semester:
            year = '2'
        else:
            year = '3'


        st.header('Question :')
        question(year)
        first,second= st.columns([6, 2])
        with first:
            st.markdown("## Code Editor")
            code = st_ace(value=(snippet(year)),
            language = 'python',
            theme='xcode')

        if st.button('run'):
            if 1 !=st.session_state['ans']:
                st.error('Please do Sign up/log in first')
    
            
            else:
                with second:
                    st.markdown("## Output")
                    st_ace(value =run(code,year) ,
                    language = 'python',
                    theme = 'pastel_on_dark',
                    readonly  = True)
        else:
            with second:
                st.markdown("## Output")
                st_ace(value ='' ,
                language = 'python',
                theme = 'pastel_on_dark',
                readonly  = True)
        if st.button('Submit'):
            if 1 !=st.session_state['ans']:
                st.error('Please do Sign up/log in first')
            
            elif name == None or mobile_no ==None or name == '' or mobile_no =='':
                st.error('Please fill the information')
            
            elif " " in mobile_no or len(mobile_no) < 12 :
                st.error('Invalid mobile number') 
            
            elif mobile_no[-12:].isdigit() or mobile_no[0]=='+':
                st.error('Invalid mobile number') 

            elif submit(year):
                list = []
                st.success('Congratulations you did it 🏆🥇')
                list.append(name)
                list.append(Semester)
                list.append(mobile_no)
                with open('./static/std_info.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(list)
                f_object.close()

            else:
                st.error('Better luck next time :thumbsdown:') 
  


