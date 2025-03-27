# News-Sentiment-Analysis (CSI-280-51 Project)
## By Kimberly Benson, Thomas Lukasiewicz, Griffin Gooch-Breault, Yin Bo Chen

# What Is This Project?

The goal of this project is to allow for a user to feed a pre-trained AI a news headline to pick out key words and sentinment (positive, neutral, negative) within it. By doing this, users can understand how a news headline skews in terms of sentiment, and compare headlines on the same subject to other news outlets.

# Repository Layout

## ASBA prototype
This directory is the LLM model and its files.

BasicABSA.py - Python file that handles the LLM's logic.
requirements.txt - set up for LLM

## Flask
This directory handles the website for the project. Static subdirectory handles the css and json, templates contains the html.

app.py - File that runs the website and handles the main logic.

## dataset
This directory contains various CSVs of real news headlines from Jan - March 2025. python_files contains the .py files used to collect data, and raw_news_titles contains the CSVs.
