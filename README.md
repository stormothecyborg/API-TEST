# Install VM > Uuntu files > setup > apache2 > install necessary modules 

## "GET / HTTP/1.1" 404 Not Found SAVIOUR


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

'from fastapi import FastAPI, HTTPException, Query

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

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
