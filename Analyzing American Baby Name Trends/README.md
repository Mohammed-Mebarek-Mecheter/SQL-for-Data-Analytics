# Analyzing American Baby Name Trends

This project aims to explore American baby name trends using data published by the U.S. Social Security Administration spanning over a hundred years. We'll analyze how baby name tastes have changed since 1920, classify names based on their popularity, find top-ranked names, assist in picking a baby name, and investigate the rise of specific names over time.

## Project Overview

What makes a name timeless or trendy? In this project, we'll analyze data provided by the United States Social Security Administration, listing first names along with the number and sex of babies given those names each year from 1920 to 2020. By using SQL queries, we'll delve into various aspects of American baby name trends.

### Dataset Description

The dataset includes the following columns:

- `year`: Year of birth.
- `first_name`: First name given to babies.
- `sex`: Sex of the babies (M for male, F for female).
- `num`: Number of babies with the given first name and sex born in that year.

## Tasks

### Task 1: Classic American Names

Find names that have been given to over 5,000 babies of either sex every year from 1920 to 2020.

### Task 2: Timeless or Trendy?

Classify each name's popularity according to the number of years that the name appears in the dataset.

### Task 3: Top-ranked Female Names since 1920

Find the top-ranked American female names in the dataset since 1920.

### Task 4: Picking a Baby Name

Return a list of first names that meet specific criteria set by a friend for choosing a baby name.

### Task 5: The Olivia Expansion

Explore the rise of the name Olivia by finding the cumulative number of babies named Olivia over the years.

### Task 6: Many Males with the Same Name

Find the maximum number of babies given any one male name in each year.

### Task 7: Top Male Names Over the Years

Find the top male name for each year in the dataset.

### Task 8: The Most Years at Number One

Find the first names that have been the top male first name in any year, along with the count of the number of years each name has held that position.

## Running the Code

The project utilizes SQL queries to analyze the dataset. You can run the provided queries in a SQL environment or editor such as PostgreSQL, MySQL, or SQLite.

