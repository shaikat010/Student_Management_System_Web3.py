import streamlit as st
# import Image from pillow to open images
from PIL import Image
import base64
from Deploy import add_student,view_function,updateStudentInfo,updateStudentAge


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('BG.jpg')


img = Image.open("logo.png")



col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    st.image(img, width=200)

with col3:
    st.write("")


st.markdown("<h1 style='text-align: center; color: white;'>  Student Management System </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: white;'>  Add Student </h3>", unsafe_allow_html=True)

name = st.text_input("Enter Your name", value = "Type Here ...", key="name")
age = st.text_input("Enter Your age",value = "Type Here ...", key="age")
enrolledStatus = st.text_input("Enrollment Status",value = "Type Here ...", key="enroll")
grades_str = st.text_input("Enter comma separated grades (e.g. 90,85,95)", "Type Here ...")

if st.button("Create Student Info"):
    grades = [int(g) for g in grades_str.split(",")]
    result = add_student(name, int(age), enrolledStatus, grades)
    st.success("Student Added")

st.markdown("<h3 style='text-align: left; color: white;'>  Retrieve Student </h3>", unsafe_allow_html=True)

id = st.text_input("Enter Student ID to retrieve",value = "Type Here ...", key="GetID")

if st.button("Retrieve Student"):
    result = view_function(int(id))
    st.success(result)

st.markdown("<h3 style='text-align: left; color: white;'>  Update Student Info </h3>", unsafe_allow_html=True)

id1 = st.text_input("Enter Student ID to update", value = "Type Here ...", key="Updated_ID")
enrolledStatus1 = st.text_input("Updated Enrollment Status",value = "Type Here ...", key="Updated_Status")
if st.button("Update Student Info"):
    result = updateStudentInfo(int(id1), enrolledStatus1)
    st.success(result)

st.markdown("<h3 style='text-align: left; color: white;'>  Update Student Age </h3>", unsafe_allow_html=True)

id2 = st.text_input("Enter Student ID to update", value = "Type Here ...", key="Updated_ID2")
age1 = st.text_input("Updated Age", value = "Type Here ...", key="Updated_Age")
if st.button("Update Student Age"):
    result = updateStudentAge(int(id2), int(age1))
    st.success(result)

