import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import date
import streamlit as st
from streamlit_calendar import calendar
from sqlalchemy import create_engine, Column, Integer, String 
import sqlalchemy
import re
options = {
    "editable": True,
    "selectable": True,
    "initialView": "dayGridMonth",
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,listMonth"
    }
}
ticket_details_df = pd.read_csv("ticket_schema.csv")

name = st.text_input(
    "Enter your name", 
    label_visibility="visible"
)
age = int(st.number_input(
    "Enter your age", 
    label_visibility="visible",
    value=0
))

gender = st.radio(
    "Select your gender:",
    options=["Male", "Female", "Non-binary", "Prefer not to say"],
    index=None,  # No default selection
    help="Enter your gender"
)
if gender:
    st.write(f"You selected: {gender}")

# booking_date = calendar(options=options, key="basic_cal")
book_date = st.date_input("Booking date", date.today())
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
# import pandas as pd
# # 1. Define your MySQL connection credentials
USERNAME = "root"
PASSWORD = "root"
HOST = "localhost"  # or 'localhost'
PORT = "3306"
DATABASE = "railway"

# # 2. Create the SQLAlchemy engine (using the pymysql driver)
connection_string = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_string)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class StationView(Base):
#     __tablename__ = "train_stations" # Replace with your Table or View name
#     station_name = Column(String, primary_key=True)
#     station_code = Column(String)
#     state = Column(String)

# from_station = st.text_input("From station: ")
# db = SessionLocal()

# # Dynamically filter based on the text input
# if from_station:
#     query = db.query(StationView).filter(StationView.station_name.ilike(f"%{from_station}%"))
# else:
#     query = db.query(StationView).limit(50)

with engine.connect() as con:
    list1 = con.execute(text("select station_code from train_stations")).fetchall()
    list2 = con.execute(text("select station_name from train_stations")).fetchall()
    list3 = con.execute(text("select state from train_stations")).fetchall()
    station_code_list = [str(x) for x in list1]
    station_code_symbol_list = [x.split("'")[1] for x in station_code_list]
    # print(station_code_symbol_list[0])
    station_name_list = [str(x) for x in list2]
    station_name_symbol_list = [x.split("'")[1] for x in station_name_list]
    # print(station_name_symbol_list[0])
    station_state_list = [str(x) for x in list3]
    # print(station_state_list[0].split("'")[1])
    station_state_symbol_list = [x.split("'")[1] for x in station_state_list]
    # print(station_state_symbol_list[0])
    station_list = [x + " - "+ y + "\n" + z for x,y,z in zip(station_code_symbol_list, station_name_symbol_list, station_state_symbol_list)]
    print(station_list[0])
    from_station = st.selectbox("From station", station_list, None)
    to_station = st.selectbox("To station", station_list, None)
    boarding_from = st.selectbox("Boarding from station", station_list, None)
    # Work on availability table
    booking_class = st.selectbox("Booking Class", ["All Classes", "Anubhuti Class (EA)", "AC First Class(1A)", "Vistadome AC (EV)", "Exec. Chair Car (EC)", "AC 2 Tier (2A)", "First Class (FC)", "AC 3 Tier (3A)", "AC 3 Economy (3E)", "Vistadome Chair Car (VC)", "AC Chair car (CC)", "Sleeper (SL)", "Vistadome Non AC (VS)", "Second Sitting (2S)"], None)
    search_train = st.button("Search Trains")
    berth_availability = {
        '':[],
        '':[],
        '':[]
    }
    con.execute(text("select "))
    # station_code_list[0].split("'")[1]
    # print(re.split(station_code_list[0], "',"))
    # list1 = list1.apply(lambda x: str(x))
    # print(re.split(list1[0], "',"))
    # print(type(str(list1[0])))
    # list1 = list1.apply(lambda x: re.split(x,"',") for x in list1)
    # options = list(str(+" "+ + " "+))
    # print(list1)
    # print(list2)
    # print(list3)
#     # cur = con.cursor()
#     # cur.fetchall()
#     # st.title("From station: ")
#     search_query = st.text_input("Enter your travel from station")
#     filtered_items = [
#         item for item in list(con.execute(text("select station_code from train_stations")))
#         if search_query.upper() in item
#     ]
    # from_station = st.radio(
    #     "From station:",
    #     options=[list(con.execute(text("select station code from train_stations")))],
    #     index=None,  # No default selection
    #     help="Enter your Travel from station"
    # )
    # 
    
# adoni - ad
# andhra pradesh
# from_station, to_station, booking_from
# engine = create_engine('mysql+pymysql:///root:rootstations.db', echo=True)

# with Session(engine) as session:
#     # --- CREATE ---
#     # new_user = User(name="Alice", email="alice@example.com")
#     session.add(new_user)
#     session.commit()  # Commits structural changes safely

#     # --- READ ---
#     # Construct explicit selection queries decoupled from the active cursor
#     stmt = select(User).where(User.name == "Alice")
#     user = session.scalars(stmt).first()
#     print(f"Found User ID: {user.id}")

#     # --- UPDATE ---
#     user.email = "new_alice@example.com"
#     session.commit()

#     # --- DELETE ---
#     session.delete(user)
#     session.commit()
# boarding_from
# to_station

# st.write(ticket_details_df)
# SQL connection

st.stop()
# st.write(cal_data)

