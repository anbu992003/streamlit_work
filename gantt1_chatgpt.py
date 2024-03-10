import streamlit as st
import pandas as pd
import plotly.express as px

#Aditional reference
#https://plotly.com/python/gantt/


def generate_gantt_chart(df):
    fig = px.timeline(df, x_start='Start Time', x_end='End Time', y='Task', color='Status', labels={'Task': 'Job', 'Start Time': 'Start', 'End Time': 'End'})
    fig.update_yaxes(categoryorder='total ascending')
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.title('Job Execution Schedule and SLA Time Gantt Chart')

    # Sample data (replace this with your actual data)
    data = {
        'Task': ['Job A', 'Job B', 'Job C'],
        'Start Time': ['2024-03-01 08:00:00', '2024-03-01 10:00:00', '2024-03-01 09:30:00'],
        'End Time': ['2024-03-01 09:30:00', '2024-03-01 11:00:00', '2024-03-01 10:30:00'],
        'Status': ['Completed', 'In Progress', 'Overdue'],
        'SLA Time': ['2024-03-01 09:00:00', '2024-03-01 10:30:00', '2024-03-01 10:00:00']
    }
    df = pd.DataFrame(data)
    print(df)

    generate_gantt_chart(df)

if __name__ == "__main__":
    main()
