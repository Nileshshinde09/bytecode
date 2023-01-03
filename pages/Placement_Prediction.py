from utils import processing,st

class main(processing):
    st.title("Will you get placed ?")
    st.error("The prediction made by this app is based on machine learning.")
    st.markdown("[You can see source code here ](https://github.com/Nileshshinde09/student-placement-prediction)")
    age = st.slider("Choose age ",14,30)
    Stream = st.selectbox("Choose Stream",['Electronics And Communication', 'Computer Science','Information Technology', 'Mechanical', 'Electrical', 'Civil'])
    Internships = st.slider("Choose Internships",0,3)
    cgpa = st.slider("Choose CGPA ",5,10)
    HistoryOfBacklogs = st.select_slider("History Of Backlogs", ['0','1'])

    streams =['Civil','Computer Science','Electrical','Electronics And Communication','Information Technology','Mechanical']
    processing(Stream,streams,cgpa,Internships,age,HistoryOfBacklogs)

    
