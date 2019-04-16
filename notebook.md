# 3/7/19 Notes
## What to do with dataset
* Show a box plot of normalized dataset
## How to download from google drive:
* url = 'URL'
* def download_data(url, filename):
	r = requests.get(url, allow_redirects=True)
	open(filename, 'wb').write(r.content)

## Only get numeric values from dataset
* numeric = file.select_dtypes(include=[np.number])

## Return a boxplot
* return send_file(boxplot, attachment_filename="plot.png",mimetype="image/png")


# 3/19/19 Notes
## K Nearest Neighbors
### Euclidean Distance
* Normalize dataset 
* Find distance between input and dataset
* Find smallest distance/nearest neighbors
* If input is within these distances, then you found your output

# 3/28/19 Notes
## Docker steps
* Write Docker file
* docker build -t name .
* docker run -p 5000:5000 name 
* To view containers: docker container ls -all

# 4/16/19 Notes
## docker run -i -t -p 8080:8080 NAME /bin/bash
