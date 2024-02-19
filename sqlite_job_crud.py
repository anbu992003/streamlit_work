import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('job_dashboard.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS job_status (
                    BatchID TEXT,
                    JobID TEXT,
                    Downstream TEXT,
                    UpstreamFeed TEXT,
                    JobType TEXT,
                    StartTime TEXT,
                    EndTime TEXT,
                    ExpectedEndTime TEXT,
                    JobStatus TEXT,
                    SLA TEXT
                )''')

# Function to insert data into the table
def create_job(BatchID, JobID, Downstream, UpstreamFeed, JobType, StartTime, EndTime, ExpectedEndTime, JobStatus, SLA):
    cursor.execute('''INSERT INTO job_status (BatchID, JobID, Downstream, UpstreamFeed, JobType, StartTime, EndTime, ExpectedEndTime, JobStatus, SLA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (BatchID, JobID, Downstream, UpstreamFeed, JobType, StartTime, EndTime, ExpectedEndTime, JobStatus, SLA))
    conn.commit()
    print("User created successfully!")

# Function to retrieve all job_status
def read_jobs():
    cursor.execute('''SELECT * FROM job_status''')
    job_status = cursor.fetchall()
    for job in job_status:
        print(job)

'''
create_job("D1", "J1", "WCRV", "CED", "FileArrival", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "NotStarted", "None")
create_job("D1", "J2", "WCRV", "CED", "Batch", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Running", "on_Time")
create_job("D1", "J3", "WCRV", "CED", "Delivery", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "Failed", "Breached")
create_job("D1", "J4", "WCRV", "WCADS", "FileArrival", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Completed", "None")
create_job("D1", "J5", "WCRV", "WCADS", "Batch", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "NotStarted", "on_Time")
create_job("D1", "J6", "WCRV", "WCADS", "Delivery", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Running", "Breached")
create_job("D1", "J7", "SABER", "FEED1", "FileArrival", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "Failed", "None")
create_job("D1", "J8", "SABER", "FEED1", "Batch", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Completed", "on_Time")
create_job("D1", "J9", "SABER", "FEED1", "Delivery", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "NotStarted", "Breached")
create_job("D1", "J10", "SABER", "FEED2", "FileArrival", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Running", "None")
create_job("D1", "J11", "SABER", "FEED2", "Batch", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "Failed", "on_Time")
create_job("D1", "J12", "SABER", "FEED2", "Delivery", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Completed", "Breached")
create_job("D1", "J13", "SABER", "Feed3", "FileArrival", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "NotStarted", "None")
create_job("D1", "J14", "SABER", "Feed3", "Batch", "2024-02-19 20:49:05", "2024-02-21 20:49:05", "2024-02-21 20:49:05", "Running", "on_Time")
create_job("D1", "J15", "SABER", "Feed3", "Delivery", "2024-02-18 20:49:05", "2024-02-19 20:49:05", "2024-02-19 20:49:05", "Failed", "Breached")
'''

read_jobs()


# Close the connection
conn.close()