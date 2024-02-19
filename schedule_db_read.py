import streamlit as st
from streamlit_autorefresh import st_autorefresh
import sqlite3


# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()


def read_users():
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    for user in users:
        st.write(user)

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
    read_users()
else:
    st.write(f"Count: {count}")
	
	

# Close the connection
conn.close()
