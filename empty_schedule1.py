import time
import streamlit as st
from schedule import every, repeat, run_pending

#https://schedule.readthedocs.io/en/stable/examples.html



with st.empty():
    #@repeat(every(3).minutes)
    def strike_details():
        i=i+1
        col1, col2 = st.columns(2)
        with col1:
            st.header("NIFTY" + str(i))
            
        with col2:
            st.header("BANKNIFTY")
            
every(5).seconds.do(strike_details)

while True:
    run_pending()
    time.sleep(1)