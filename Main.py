import fastf1
import pandas as pd
import matplotlib.pyplot as plt


# year, race name, session type
session = fastf1.get_session(2025, "Monaco", "R")
session.load()

laps = session.laps
lap1 = laps[laps["LapNumber"] == 1]

small_df = lap1[["Driver", "LapTime", "Position"]]
small_df = small_df.sort_values("Position")
print(small_df)
