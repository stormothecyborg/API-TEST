# Install VM > Ubuntu files > setup > apache2 > install necessary modules 

## "GET / HTTP/1.1" 404 Not Found RESOLVED


set your apache2 as reverse proxy 

### `sudo nano /etc/apache2/sites-enabled/reverse_proxy.conf`

i have used this, u can also use sudo nano /etc/apache2/sites-available/000-default.conf
or any other, make sure there is only 1 apache configuration file (for less confusion) use rm <file/path> to DELETE any unnecessary extra files

the file contents: 
points to note : 1. its okay if u have a different code, just make sure that your CustomLogs <file path> has the same file path when you access your logs using tail -f /var/log/apache2/access.log



'<VirtualHost *:80>
        
        ServerName 127.0.0.1

        DocumentRoot /var/www/html

        <Proxy *>
        AuthType none
        AuthBasicAuthoritative Off
        SetEnv proxy-chain-auth On
        Order allow,deny
        Allow from all
        </Proxy>
     
        ProxyPass / http://127.0.0.1:8000/
        ProxyPassReverse / http://127.0.0.1:8000/

        <Directory /var/www/html>
        Order deny,allow
        Allow from all
        </Directory>

       
       CustomLog /var/log/apache2/access.log common


</VirtualHost>

### `sudo systemctl restart apache2`

### FastAPI CODE 
make sure the endpoints [in my case>>> @app.get("/filtered-logs/") ] are correct 

'

     from fastapi import FastAPI, HTTPException, Query

    from typing import List, Optional

    from datetime import datetime

    from fastapi.middleware.cors import CORSMiddleware

    import re



    app = FastAPI()



    app.add_middleware(

        CORSMiddleware,

        allow_origins=["http://localhost:3000"],  # Replace with the actual origin of your React app

        allow_credentials=True,

        allow_methods=["*"],

        allow_headers=["*"],

    )



    # Function to read and filter access logs

    def get_filtered_logs(start_time: Optional[datetime], end_time: Optional[datetime]) -> List[str]:

        log_entries = []

        log_file_path = '/var/log/apache2/access.log'

      # Replace with the actual path to your access log file
        try:

            with open(log_file_path, 'r') as file:

                for line in file:

                    log_time_str = re.search(r'\[(.*?)\]', line).group(1)

                    log_time = datetime.strptime(log_time_str, '%d/%b/%Y:%H:%M:%S %z')

                    if (start_time is None or start_time <= log_time) and (end_time is None or log_time <= end_time):

                        log_entries.append(line.strip())
   
        except FileNotFoundError:

            raise HTTPException(status_code=404, detail="Access log file not found.")



        return log_entries



    # API endpoint to get filtered logs

    @app.get("/filtered-logs/")

    async def read_filtered_logs(

        start_time: Optional[datetime] = Query(None, alias="start_time", description="Start time for filtering"),

        end_time: Optional[datetime] = Query(None, alias="end_time", description="End time for filtering")

    ):

        logs = get_filtered_logs(start_time, end_time)

        return {"filtered_logs": logs}



    # Run the FastAPI app with Uvicorn

    if __name__ == "__main__":

        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)                              

'

##apache benchmark 
'ab -n 1000 -c 100 http://127.0.0.1/filtered-logs/' 


### `uvicorn api:app --reload`
NOTE: my py file name is api, chnage it to ur py file name 

### `(http://127.0.0.1:8000/filtered-logs/`
NOTE: make sure to give your endpoint name from ur fastapi code (in my case ''filtered-logs''

### `tail -f /var/log/apache2/access.log`

open this in other terminal 
### `curl /var/log/apache2/access.log`

#rest is just the frontend , u can look my frontend folder for code 


This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
