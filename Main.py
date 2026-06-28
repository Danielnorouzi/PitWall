import fastf1 as ff1
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st



ff1.Cache.enable_cache('cache') 
# ff1 getter ->  get_session(year , race name / location, session type{"Q","R"});
session = ff1.get_session(2025, "Monaco", "R")
session.load()

laps = session.laps
lap1 = laps[laps["LapNumber"] == 1]

small_df = lap1[["Driver", "LapTime", "Position"]]
small_df = small_df.sort_values("Position")



ver_laps = laps[laps["Driver"] == "VER"]
ver_laps = ver_laps[['Sector1Time', 'Sector2Time', 'Sector3Time',  "LapNumber" ]]
#print(small_df)

ver_laps.plot(x= 'LapNumber',y = ['Sector1Time', 'Sector2Time', 'Sector3Time'])


plt.title("Verstapin sectors")
plt.legend()
st.title("PitWall")
st.pyplot(plt.gcf())





# UI/UX
#st.title("F1 Dashboard")
#lapNum = st.number_input("Enter Lap Number")
#if st.button("Click Me"):
#    lap1 = laps[laps["LapNumber"] == lapNum]
#    small_df = lap1[["Driver", "LapTime", "Position"]]
#    small_df = small_df.sort_values("Position")
#st.dataframe(small_df)

#st.dataframe(ver_laps)
#st.dataframe(laps)