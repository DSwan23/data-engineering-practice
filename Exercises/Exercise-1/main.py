import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def create_dir(dirName: str):
    # TODO: Add code in here to create a new directory
    pass

def download_from_uri(uri: str):
    # TODO: Download a file from a URI, include error checking
    pass

def split_filename(uri: str) -> str:
    # TODO: return the filename from the passed URI
    pass

def extract_csv_from_zip(zipFile: str) -> str:
    # TODO: extract the csv from the zip file\
    # TODO: remove the zip file
    # TODO: return the csv filename
    pass

def main():
    # TODO: write unit tests for the files above (Learn how to do this!)
    # TODO: get the basic code working
    # TODO: try todo it in an async manner
    # TODO: try it in a multithreaded manner
    # your code here
    pass


if __name__ == "__main__":
    main()
