import streamlit
import pandas
import requests
#
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Let's put pict
my_fruit_list=my_fruit_list.set_index('Fruit')

streamlit.header('Fruityvice Fruit Advice!')
streamlit.text(fruityvice_response.json())
streamlit.header('Breakfast Favorite')
streamlit.title(' 🥣 Omega 3 and Blueberry Oatmeal')
streamlit.title('🥗 Kale,Spinach and Rocket Smoothie')
streamlit.title(' 🐔 Hard.boiled.free.range Egg')
streamlit.title('🥑🍞 Avocado and bread')
streamlit.header('Build Your Own Fruit Smoothie')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
#display the table on the page


 
