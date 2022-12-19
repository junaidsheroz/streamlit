import streamlit as st
import pandas as pd
# title() method is for setting the title of the web page
st.title('Smart Tech!')
st.header('This is a header')

st.write('This is a simple web page created using Streamlit.')

st.image('https://media.giphy.com/media/3o7TKSjRrfIPjeUGO8/giphy.gif')

st.video('https://www.youtube.com/watch?v=9bZkp7q19f0')

file = pd.read_csv('https://raw.githubusercontent.com/junaidsheroz/Datasets/master/airline-passengers.csv')
st.dataframe(file)

st.table(file)

# calendar
st.date_input('Enter a date')


name = st.text_input('Enter your name')
roll = st.number_input('Enter your roll number', min_value=1, max_value=100)
date = st.date_input('Enter your date of birth')

button = st.button('Click here to submit')

if button:
    st.write('Your name is', st.write(name))
    st.write('Your roll number is', st.write(roll))
    st.write('Your date of birth is', st.write(date))