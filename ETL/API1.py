import pandas as pd
import requests
from  datetime import datetime

url = "https://arbeitnow.com/api/job-board-api"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
# print(data)

df = pd.DataFrame(data['data'])
# print(df)
df['tags'] = df['tags'].apply(lambda x: ", ".join(x))
df['job_types'] = df["job_types"].apply(lambda x: ", ".join(x))
df['created_at']= (df['created_at'].apply(datetime.fromtimestamp))
df.to_excel("jobs.xlsx")