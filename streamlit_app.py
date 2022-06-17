import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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
fruits_selected=streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the repeatable code block:
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalised=pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalised

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice=streamlit.text_input("What Fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please Select a Fruit to get Information.")
  else:
    back_from_fuction = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_fuction)
except URLError as e:
  streamlit.error()



#connecting to SnowFlake:
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

#querying on SnowFlake data:
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_rows = my_cur.fetchall()
streamlit.header("View our Fruit List - Add your Favorites:")
#function for query:
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
if streamlit.button("Get Fruit List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

# streamlit.stop()
#choice of adding fruit

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"');")
    return "Thanks for adding "+new_fruit
    
add_my_fruit=streamlit.text_input("What Fruit would you like to add?")
if streamlit.button("Add a Fruit to the List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_fuction=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_fuction)
  
# streamlit.write("Thanks for adding ",add_my_fruit)

# my_cur.execute("insert into fruit_load_list values ('from streamlit');")
