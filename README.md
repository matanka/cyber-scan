# cyber-scan

In order to run this program:
1) Run redis in localhost (with no authentication)
2) Install requirements 
3) Run worker:
                rq worker
4) Run main file:
                python main.py

The web server is running on port 5000.
2 endpoints are available:
- GET http://localhost:5000/task
- GET http://localhost:5000/task/8d44f026-41c5-4257-98e9-2c834ba15369
