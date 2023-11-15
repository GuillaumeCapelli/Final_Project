Analysis of Toxic Comments on Social Media Platforms
Project Overview

Author: Guillaume Capelli
Date: November 2023
GitHub Repository: Final_Project

This project is focused on analyzing toxic comments across various social media platforms to understand and predict the level of toxicity. The primary goal is to dissect the complex dynamics of these comments and use the findings to inform a machine learning model capable of detecting and categorizing toxicity autonomously.
Data Sources

    YouTube: Comments scraped using Selenium from videos with polarizing content.
    Reddit: Comments extracted via Reddit API from threads with debate and controversy.
    Kaggle: "Jigsaw Toxic Comment Classification Challenge" dataset, offering pre-labeled comments.
    BigQuery: Extensive datasets processed and analyzed for comments from various online forums.

Methodology
Data Collection

    Utilized tools like Selenium, PRAW (Python Reddit API Wrapper), and BigQuery.
    Ensured GDPR compliance through data anonymization, data minimization, and secure data handling.

Data Cleaning

    Harmonized dataframes by renaming columns.
    Removed special characters and added new columns like "comment_length".

Exploratory Data Analysis (EDA)

    Calculated descriptive statistics and generated visualizations like histograms and word clouds.
    Performed correlation analysis and activity over time assessment.

Database

    Chose MySQL for its scalability, transactional support, and community support.
    Ensured data integrity and security.

Machine Learning Model

    Aimed to train a model to categorize comments into different levels of toxicity.

Project Outcome

The project successfully analyzed trends in toxic comments, revealing insights into user engagement and the nature of online toxicity. It laid the groundwork for developing a predictive model to aid in moderating online communities.
