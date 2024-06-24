import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


#https://my-testing-tw4vkay4oba.streamlit.app/
# Show app title and description.
st.set_page_config(page_title="Support ticket workflow", page_icon="🎫")
st.title("🎫 Support ticket workflowTest123")
st.write(
    """
    This app shows how you can build an internal tool in Streamlit. Here, we are 
    implementing a support ticket workflow. The user can create a ticket, edit 
    existing tickets, and view some statistics1212312334.
    """
)

if 'counter' not in st.session_state.keys():
    st.session_state['counter']=0

if st.button("Click me for ballons!"):
    st.balloons()
    st.session_state['counter']+=1


st.write(st.session_state['counter'])
st.write(f"You hit the button {st.session_state['counter']} times")


st.title("Playing with inputs")

user_choice=st.radio("Which is the best?", options=['Cats','Dogs'])
st.write(f"Yous elected {user_choice}")

st.slider("Select a number",min_value=0,max_value=100,step=5)