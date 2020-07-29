import streamlit as st
import PIL.Image
import io

#uploaded_file = st.file_uploader("/home/gopinath/Documents/AMBERTAG/Support Department/FITTO/Release_notes_R1.00_25_07_2020.odt")
#text_io = io.TextIOWrapper(uploaded_file)

photo = "/home/gopinath/Documents/AMBERTAG/Support Department/FITTO/logo.png"
img = PIL.Image.open(photo)

if img.mode != 'RGB':
    img = img.convert('RGB')

st.image(img, width=100)
st.title("AmberTAG - Customer Centricity - Who are my customers")

#st.write("This system will have all the details for the FITTO Support.The list of customers, their contact details. The Release information and Release notes. Information about support team with their contact details ")

st.sidebar.header("Gopinath Subbegowda - Mycustomers")
main_selectbox = st.sidebar.selectbox("Please select option for more details", ("Support Team", "FITTO Customers", "FITTO Release Info", "MY CUSTOMERS"))
if main_selectbox == "MY CUSTOMERS":
    st.header("Please select ROLE to show My Customers")
    sec_selectbox = st.selectbox('',("TCoE - HEAD", "Support Team Member/Lead", "Employee"))
    if sec_selectbox == "TCoE - HEAD":
        st.write("1. AmberTAG Project Teams")
        st.write("2. Project Team stakeholders")
        st.write("3. AmberTAG Management")
        st.write("4. Testing Team")
    elif sec_selectbox == "Support Team Member/Lead":
        st.write("1. Customers of the Product/s supported")
        st.write("2. Stakeholders of the Product/s supported")
        st.write("3. Support team")
        st.write("4. AmberTAG Management")
            #st.selectbox('',("Release 1.01", "Release 1.02"))
    elif sec_selectbox == "Employee":
        st.write("1. Customers of AmberTAG")
        st.write("2. My Project Team members")
        st.write("3. AmberTAG Management/Managers")
                
        