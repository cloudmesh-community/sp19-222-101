# *templates* directory
### This directory holds all of the html pages for the tool.

## home.html
HTML page for the root endpoint of the tool. Can be accessed via http://localhost:8080

## showModel.html
HTML page for the /upload endpoint of the tool. This page shows the tool's prediction and other information about the tool. This endpoint CANNOT be accessed via url. You must go to the root page first and upload a file. After that, you will be automatically directed to http://localhost:8080/upload

## error.html
HTML page for a custom error message. This page displays a custom error message in case the user tries to access something that is inaccessible. It includes a link to the root page of the tool.


