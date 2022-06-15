import streamlit
import pandas as pd

streamlit.title("It's my First ever Streamlit application")
streamlit.header("My SnowFlake Course")
streamlit.text("It contains multiple Badges's")
streamlit.text("As of now I hv Completed the First Badge")
streamlit.header("First Badge is 'Badge 1: Data Warehousing Workshop' ")
streamlit.text(" Hands On Essentials - Data Warehouse")
streamlit.text("It contains 11 Lesson's and Wrapping Up session for Badge")
streamlit.header("Now in Badge two, We are on some excercise's ")
streamlit.text("Fruit list")
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
