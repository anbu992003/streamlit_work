import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
from streamlit_autorefresh import st_autorefresh

#https://www.analyticsvidhya.com/blog/2021/06/style-your-pandas-dataframe-and-make-it-stunning/https://www.analyticsvidhya.com/blog/2021/06/style-your-pandas-dataframe-and-make-it-stunning/
#https://pandas.pydata.org/docs/user_guide/style.html

limit=100
# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=10000, limit=limit, key="fizzbuzzcounter")

st.subheader("Dashboard")

tab_value=ui.tabs(options=['Overview', 'Analytics'], default_value='Overview', key="main_tabs")
st.write("Tab Value:", tab_value)

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
#df1 = pd.DataFrame(np.random.randn(20, 10), columns=("col %d" % i for i in range(10)))
df1 = pd.read_csv("job_status.csv")

def highlight_job_status(s):
    #is_sla_breach = s == "Breached"
    return ['background-color: red' if i == "Breached" else ('background-color: green' if i == "on_Time" else 'background-color: black') for i in s]


df1=df1.style.apply(highlight_job_status)

def populate_dashboard():
    if tab_value=='Overview':        
        st.dataframe(df.style.highlight_max(axis=0))

    else:        
        #st.dataframe(df1.style.highlight_max(axis=0))
        st.dataframe(df1)
        
populate_dashboard()
