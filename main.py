import streamlit as st
from utils import extract_id,get_transcripts
from src.Script_Generator.Script_Generator import get_response
from src.Script_Generator.logging import logging 
import traceback
import json



st.title("Youtube Script Generator  🤖 ")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    if video_context=="" and url1=="":
        return st.warning("fill missing fields")
    else:  
        st.session_state.clicked = True

form=st.form("form")
with form:
    video_context=st.text_area("Enter Your Youtube Video Context")
    c1,c2=st.columns(2)
    url1=c1.text_input("url1",key="url1")
    url2=c2.text_input("url2",key="url2")
    url3=c1.text_input("url3",key="url3")
    url4=c2.text_input("url4",key="url4")
    url5=c1.text_input("url5",key="url5")
    btn=st.form_submit_button("Submit",on_click=click_button)


if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Details Entered Sucessfully!')
    with st.spinner("loading...."):
        try:
            logging.info("Collecting urls")
            urls_list=[url1,url2,url3,url4,url5]
            urls_list = [i for i in urls_list if i is not None and i !=""]
            transcripts=get_transcripts(urls_list)
            response=get_response(video_context,transcripts)
            st.write(response)
        except Exception as e:
            traceback.print_exception(type(e),e,e.__traceback__)
            st.error("Error")

