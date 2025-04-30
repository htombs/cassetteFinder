# cassetteFinder

cassetteFinder is a tool designed to assist bike shop mechanics in streamlining the process of ordering bicycle cassettes. By aggregating data from various suppliers, it enables users to quickly identify available cassettes based on specific criteria, reducing the time spent searching across multiple platforms.

## 🛠 Features

- Supplier Aggregation: Consolidates cassette listings from multiple suppliers into a single interface.

- Advanced Filtering: Search cassettes by speed, gear ratio and brand.

- Direct Links: Provides direct links to supplier pages for easy ordering.

- Part Number Retrieval: Offers part numbers for quick reference and ordering.



## 🚀 Getting Started

- Prerequisites
  
- Python 3.8+

- Node.js 14+

- npm 6+

- SQLite (for local database management)


## Installation

Clone the Repository
```shell
git clone https://github.com/htombs/cassetteFinder.git
cd cassetteFinder
```

## Running the API locally

The following command should install all the external modules needed for this api to run.
```shell
pip install -r requirements.txt
```

This tells python to read this file, and install any named modules in the file.

Once this is done, you can run the API locally using `python3 server/api.py`

## Running the client locally

We can make use of a useful NPM module called `http-server` to serve the website.

simply run:
```shell
npx http-server -c-1 ./client
```
> Note: the "-c-1" sets the cache to no-store to ensure files are not cached between each start
