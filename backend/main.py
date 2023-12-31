# main.py (FastAPI server)



from fastapi import FastAPI

from datetime import datetime



from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()



# CORS middleware configuration

app.add_middleware(

    CORSMiddleware,

    allow_origins=["http://localhost:3000"],  # Replace with the actual origin of your React app

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)







# Sample logs data

logs = [

    {"ip": "192.168.1.1", "timestamp": "2022-01-01T10:00:00"},

    {"ip": "192.168.1.2", "timestamp": "2022-01-01T11:00:00"},

    {"ip": "192.168.1.3", "timestamp": "2022-01-01T09:00:00"},

]



@app.get("/logs")

async def get_logs():

    sorted_logs = sorted(logs, key=lambda x: (x["ip"], datetime.fromisoformat(x["timestamp"])))

    formatted_logs = [f"{log['ip']} - {log['timestamp']}" for log in sorted_logs]

    return {"logs": formatted_logs}

