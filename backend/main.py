# NOT THIS FILE see>>> api.py
# WRONG CODE DOESNT WORK 


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

#OTHERCODE 


#WRONG CODE SEE api.py


from fastapi import FastAPI

from fastapi.responses import JSONResponse

from fastapi import Query

from datetime import datetime, timedelta

import re



app = FastAPI()



# Dummy access log data for demonstration purposes

access_logs = [

    {"timestamp": "2023-01-01T12:00:00", "message": "Request 1"},

    {"timestamp": "2023-01-01T12:01:00", "message": "Request 2"},

    # Add more access log entries...

]



@app.get("/access-logs/")

def get_access_logs(start_time: str = Query(None), end_time: str = Query(None)):

    try:

        start_datetime = datetime.fromisoformat(start_time) if start_time else datetime.min

        end_datetime = datetime.fromisoformat(end_time) if end_time else datetime.max

    except ValueError:

        return JSONResponse(content={"error": "Invalid datetime format"}, status_code=400)



    filtered_logs = [

        log for log in access_logs

        if start_datetime <= datetime.fromisoformat(log["timestamp"]) <= end_datetime

    ]



    return filtered_logs
