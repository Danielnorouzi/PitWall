import fastf1 as ff1
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st



st.title("Pitwall: ")




ff1.Cache.enable_cache('cache') 
# ff1 getter ->  get_session(year , race name / location, session type{"Q","R"});
session = ff1.get_session(2026, "Manzo", "R")
session.load()




laps = session.laps
lap1 = laps[laps["LapNumber"] == 1]
small_df = lap1[["Driver", "LapTime", "Position"]]
small_df = small_df.sort_values("Position")




def graphSector(DriverTag):
    ver_laps = laps[laps["Driver"] == DriverTag]
    ver_laps = ver_laps[['Sector1Time', 'Sector2Time', 'Sector3Time',  "LapNumber" ]]
    ver_laps.plot(x= 'LapNumber',y = ['Sector1Time', 'Sector2Time', 'Sector3Time'])
    plt.title(DriverTag + " sectors")
    plt.legend()
    
    


col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    if st.button("Verstappen"):
        graphSector("VER")
    if st.button("Russel"):
        graphSector("RUS")
    if st.button("Hulkenberg"):
        graphSector("HUL")
    if st.button("Hadjar"):
        graphSector("HAD")
       
with col2:
    if st.button("Leclerc"):
        graphSector("LEC")
    if st.button("Kimi"):
        graphSector("ANT")
    if st.button("Bearmon"):
        graphSector("BEA")
    if st.button("Lawson"):
        graphSector("LAW")
        

with col3:
    if st.button("Hamilton"):
        graphSector("HAM")
    if st.button("Albon"):
        graphSector("ALB")
    if st.button("Ocon"):
        graphSector("OCO")
    if st.button("Stroll"):
        graphSector("STR")


with col4:
    if st.button("Norris"):
        graphSector("NOR")
    if st.button("Sainz"):
        graphSector("SAI")
    if st.button("Tsunado"):
        graphSector("TSU")
    if st.button("Gasly"):
        graphSector("GAS")


with col5:
    if st.button("Piastri"):
        graphSector("PIA")
    if st.button("Alonso"):
        graphSector("ALO")
    if st.button("Bortoleto"):
        graphSector("BOR")
    if st.button("Colapinto"):
        graphSector("COL")



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