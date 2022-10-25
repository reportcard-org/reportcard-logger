# README

## Purpose

This is a Python script for creating the data_file CSV for the ReportCard backend when new [National Center for Education Statistics](https://nces.ed.gov/) data is released, by iterating through Local Education Agency IDs for the United States, making the necessary API calls, and saving to a CSV file.

*This does not need to be run to set up the [back end repo](https://github.com/reportcard-org/reportcard-rails), only on as new data is released! This script takes around 8 hours to run depending on speed of API calls.*

## Set-up

To run this script, clone the repo to your local machine, and ensure you have [Python3](https://www.python.org/downloads/) installed. 

Navigate to the cloned repo, and run:

`$ python3 app.py`

If successful, your terminal will output the names of school districts as they are logged, and percent completion updates as it runs, reading LEA_IDs from `all_leas.csv` file and writing the results to the `data_files.csv` file. 

![image](https://user-images.githubusercontent.com/17027357/197850985-90d37065-4e41-4d10-b0ca-c0790f3d3600.png)
