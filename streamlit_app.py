import streamlit
import pandas
streamlit.title('Snowflake Workshop Streamlit')
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
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#parsing JSON response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Displaying the normalized form
streamlit.dataframe(fruityvice_normalized)
streamlit.stop()


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The furit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add ?','Kiwi')
streamlit.write('The user entered ',add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('add_my_fruit')")
