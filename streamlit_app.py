import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Todays Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach& Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Eggs')
streamlit.text('🥑🍞 Avocado Teast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


