# project-code
## Endpoints:
### base endpoint (localhost:8080)
This is the main page of the tool.
### /upload endpoint (localhost:8080/upload)
This is the page that shows a prediction for a previously uploaded file.


**NOTE:** You CANNOT access this endpoint via URL. You must visit the base enpoint first. The only way to correctly visit this endpoint is to upload a file from the base enpoint. 

***

## How to Run:
1. Make sure you have Docker installed
2. Download Dockerfile and Makefile
3. open a new terminal window and type:
    make docker-all
4. Profit