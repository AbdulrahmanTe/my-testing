import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests


#https://my-testing-tw4vkay4oba.streamlit.app/
#https://docs.streamlit.io/develop/quick-reference/cheat-sheet
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

sweet=st.slider("Select a number",min_value=0,max_value=100,step=5)

if sweet<10:
    st.write("Very healthy")
elif sweet<50:
    st.write("You should cut back")
else:
    st.write("You should stop")

my_title=st.empty()
my_title.title(f"You've picked {user_choice}")

st.title(f"You've picked {user_choice}")

col1, col2, col3 = st.columns(3)
col1.write("col2")
col2.write("col2")
col3.write("col3")

with col1:
    st.write("iuusfiudsf")
    st.write("oiseofusaidfu")


st.title("Pokemon")
#pokemon_number = input('What is your favourite pokemon_number?')

pokemonNumber=st.slider("Select a number",min_value=1,max_value=100,step=1)
#
url = f'https://pokeapi.co/api/v2/pokemon/{pokemonNumber}/'

#
response = requests.get(url)
pokemon = response.json()
print(response)

st.write(f"Pokemon Name: {pokemon['name']}")
st.write("Move List:")
for x in pokemon['abilities']:    
    st.write(f"{x['ability']['name']}")
    


pokedex = pd.DataFrame(columns = ['name', 'height', 'weight', 'move_count'])

def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves'])
    except:
        return 'Error', np.NAN, np.NAN, np.NAN
for poke_number in range(1, 7):
    pokedex.loc[poke_number] = get_details(poke_number)

st.write("#################")

Name, Height, Weight,NumberOfMoves = st.columns(4)
Name.write(get_details(3)[0])
Height.write(get_details(3)[1])
Weight.write(get_details(3)[2])
NumberOfMoves.write(get_details(3)[3])

st.write("#################")

st.write(get_details(3))


pokedex