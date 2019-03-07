# 3/7/19 Notes
## What to do with dataset
* Show a box plot of normalized dataset
## How to download from google drive:
*url = 'URL'
* def download_data(url, filename):
	r = requests.get(url, allow_redirects=True)
	open(filename, 'wb').write(r.content)

## Only get numeric values from dataset
* numeric = file.select_dtypes(include=[np.number])

## Return a boxplot
* return send_file(boxplot, attachment_filename="plot.png",mimetype="image/png")

