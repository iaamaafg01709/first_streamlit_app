import streamlit
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Let's put pict
my_fruit_list=my_fruit_list.set_index('Fruit')

streamlit.header('Breakfast Favorite')
streamlit.title(' 🥣 Omega 3 and Blueberry Oatmeal')
streamlit.title('🥗 Kale,Spinach and Rocket Smoothie')
streamlit.title(' 🐔 Hard.boiled.free.range Egg')
streamlit.title('🥑🍞 Avocado and bread')
streamlit.header('Build Your Own Fruit Smoothie')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
#display the table on the page


 
