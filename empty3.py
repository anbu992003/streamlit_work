import time
import streamlit as st
from schedule import every, repeat, run_pending


with st.empty():
    @repeat(every(3).minutes)
    def strike_details():
        col1, col2 = st.columns(2)
        with col1:
            st.header("NIFTY")
            #data1 = pd.read_csv(os.path.join(directory_of_python_script, str('strike_data_csv') , "NIFTY_strike.csv"), on_bad_lines='skip')
            #st.table(data1)

        with col2:
            st.header("BANKNIFTY")
            #data2 = pd.read_csv(os.path.join(directory_of_python_script, str('strike_data_csv') , "BANKNIFTY_strike.csv"), on_bad_lines='skip')
            #st.table(data2)


    while True:
      run_pending()
      time.sleep(1)