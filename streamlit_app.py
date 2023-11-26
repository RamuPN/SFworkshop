import streamlit
import pandas
Streamlit.title('Snowflake Workshop Streamlit')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast');

streamlit.header('🍌🥭 Mikasa Ackerman Food court🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruits_selected]
#show table on page
streamlit.dataframe(fruits_to_show)
#display fruityviceapi_response

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#parsing JSON response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Displaying the normalized form
streamlit.dataframe(fruityvice_normalized)
