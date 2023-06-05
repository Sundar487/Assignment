# Assignment

# Overview
Python script that reads data from an Excel file containing COVID-19 state-level data. It performs data processing and analysis to identify the top 3 states with the highest number of COVID deaths for each month ('March', 'April', 'May', 'June'). The script then sends this information as messages to a Slack channel at regular intervals.

1.Importing necessary libraries:
* Pandas Library is imported to work with data in a tabular format.
        WebClient from the slack library is imported to send messages to a Slack channel.
        time is imported to introduce delays between sending messages.
        os is imported to access environment variables.
        pathlib is imported to work with file paths.
        dotenv is imported to load environment variables from a .env file.

2.Loading environment variables:
* The code loads environment variables from a .env file using the load_dotenv function. The .env file is located in the same directory as the script.

3.Reading the Excel file:
* The script reads an Excel file containing COVID-19 state-level data using pd.read_excel. The file path is specified as "C:\Users\ASUS\Documents\covid-19-state-         level-data.xlsx". You may need to modify this path to point to your specific file location.

4.Grouping the data:
* The data is processed to group it by month and state using the groupby function. This allows for the calculation of the total number of deaths for each month and state.

5.Setting up variables:
* An interval of 10 seconds is set using the interval variable. This represents the time delay between sending consecutive messages to the Slack channel.

6.Finding the top 3 states:
* A loop iterates over the months ('March', 'April', 'May', 'June'). For each month, the script identifies the top 3 states with the highest number of deaths using the nlargest function. The results are stored in the top_3_states list.

7.Creating a Slack client and sending messages:
* The Slack token is retrieved from the environment variables using os.getenv("SLACK_TOKEN").
        A Slack client is created using the obtained token.
        The script enters an infinite loop (while True) to continuously send messages.
        For each month, a message is constructed containing the top 3 states with the highest number of COVID deaths.
        The message is sent to a specified Slack channel using the client.chat_postMessage method.
        The script introduces a delay of 10 seconds using time.sleep(interval) before sending the next message.
