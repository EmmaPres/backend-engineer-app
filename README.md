# Syndio Backend App

### Setting up the App
1. Download the zip file or clone the repo from https://github.com/EmmaPres/backend-engineer-app
2. Ensure you are using Python 3.10 or later, and have pip installed.
3. Open the project in an IDE of your choice, or navigate to the project in the command line, and install the necessary packages:
```
$ pip install -r requirements.txt
```

### Running the App
4. To run the App, make sure you are in your project and run:
```
$ flask run
```
6. Once the app is running, you can navigate to `localhost:$FLASK_RUN_PORT/employees` in your browser, or run `$ curl localhost:FLASK_RUN_PORT/employees`
   - `$FLASK_RUN_PORT` is an environmental variable defined in `.flaskenv`. It's default is `5000` but can be changed to any port from that file.