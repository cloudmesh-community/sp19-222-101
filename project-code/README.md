# project-code
## Endpoints:
### base endpoint (localhost:8080)
This is the main page of the tool.
### /upload endpoint (localhost:8080/upload)
This is the page that shows a prediction for a previously uploaded file.


**NOTE:** You CANNOT access this endpoint via URL. You must visit the base enpoint first. The only way to correctly visit this endpoint is to upload a file from the base enpoint. 

***

## How to Run Service:
1. Make sure you have Docker installed
2. Download Dockerfile and Makefile
3. Open a new terminal window and cd into the directory where the Dockerfile and Makefile are stored.
4. In the terminal shell, type:  
```console
foo@bar:~/$ make docker-all
```
This will take several minutes to complete. When it is ready, the output on the terminal window will look similar to this:
```console
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
* Restarting with stat
```
5. Once this is done, open a web browser and go to http://localhost:8080

## How to Stop Service:
1. Open a new terminal window
2. cd into the directory where Dockerfile and Makefile are stored
3. In the terminal shell, type:
```console
foo@bar:~/$ make docker-clean
```
When this is done, the output will look similar to this:
```console
Removed container 'container_name'
DONE
```