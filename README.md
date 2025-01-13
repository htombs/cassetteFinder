Ideally used by bikeshop mechanics in order to help streamline their process for ordering cassettes.

I'm previously a Manager of a small independent bike shop and the amount of time myself and the mechanincs would spend searching all our suppliers for a specific cassette was rediculas. We were constantly plagued with stock issues, compatibility issues, suppliers picking up or dropping brands or sometimes suppliers just closing down. With this database, I aim to build a free website that mechanics can use as a tool to do the searching for them. The idea is they will select the speed, ratio or the brand they need, and be given a list of all the suppliers that stock that cassette. With links, they will be able to copy the part number that will be provided and go straight to that supplier to find what they need, saving time and making the whole process more efficeint and cost effective for the business.

If this is successful, I'd love to expand to other parts of a bike, but for the mean time, cassettes are the most frustrating and common time-waster as their are just so many different ratios and B2Bs to look, so let's start there!

## Developing this Project

### Pre Requisites
 - git
 - Python 3+
 - nodejs 20+
 - flask
 - flask-corss
 - sqlite3

### Running the API locally

The following command should install all the external modules needed for this api to run.
```shell
pip install -r requirements.txt
```

This tells python to read this file, and install any named modules in the file.

Once this is done, you can run the API locally using `python3 server/api.py`

### Running the client locally

We can make use of a useful NPM module called `http-server` to serve the website.

simply run:
```shell
npx http-server -c-1 ./client
```
> Note: the "-c-1" sets the cache to no-store to ensure files are not cached between each start
