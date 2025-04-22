# News-Sentiment-Analysis (CSI-280-51 Project)
## By Kimberly Benson, Thomas Lukasiewicz, Griffin Gooch-Breault, Yin Bo Chen

# What Is This Project?

The goal of this project is to allow for a user to feed a pre-trained AI a news headline to pick out key words and sentinment (positive, neutral, negative) within it. By doing this, users can understand how a news headline skews in terms of sentiment, and compare headlines on the same subject to other news outlets.

# Repository Layout

## ASBA
This directory is the LLM model and its files.

ABSA.py - Python file that handles the LLM's logic.
requirements.txt - set up for LLM

We are using a model devleoped off of microsoft's deberta V3.

Please view the papers of its creators here:

  Yang, Heng, et al. “Back to Reality: Leveraging Pattern-Driven Modeling to Enable Affordable Sentiment Dependency Learning.” CoRR, vol. abs/2110.08604, 2021, https://arxiv.org/abs/2110.08604.
  Yang, Heng, et al. “PyABSA: A Modularized Framework for Reproducible Aspect-Based Sentiment Analysis.” Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, CIKM 2023, Birmingham, United Kingdom, October 21-25, 2023, edited by Ingo Frommholz et al., ACM, 2023, pp. 5117–22, https://doi.org/10.1145/3583780.3614752.

## Flask
This directory handles the website for the project. Static subdirectory handles the css and json, templates contains the html.

app.py - File that runs the website and handles the main logic.

## dataset
This directory contains various CSVs of real news headlines from Jan - March 2025. python_files contains the .py files used to collect data, and raw_news_titles contains the CSVs.
