import pandas as pd
from slack import WebClient
import time
import os
from pathlib import Path 
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("C:\\Users\\ASUS\\Documents\\covid-19-state-level-data.xlsx")

# Group the data by month and state to calculate the number of deaths
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.strftime('%B')
grouped_data = df.groupby(['month', 'state']).agg({'deaths': 'sum'})

interval = 10
# Get the top 3 states with the highest number of deaths for each month
top_3_states = []
for month in ['March', 'April', 'May', 'June']:
    top_states = grouped_data.loc[month].nlargest(3, 'deaths')
    top_3_states.append(top_states)

# Create a Slack client and send the messages
slack_token = os.getenv("SLACK_TOKEN")
client = WebClient(token=slack_token)

while True:
    for i, month in enumerate(['March', 'April', 'May', 'June']):
        message = f"Top 3 states with the highest number of COVID deaths for the month of {month}\n"
        for j, (_, row) in enumerate(top_3_states[i].iterrows(), 1):
            state = row.name
            deaths = row['deaths']
            percentage = deaths / grouped_data.loc[month]['deaths'].sum() * 100
            message += f"State #{j} ({state}) - {deaths} deaths, {percentage:.2f}% of total US deaths\n"

        client.chat_postMessage(channel='#alerts', text=message)
        time.sleep(interval)




