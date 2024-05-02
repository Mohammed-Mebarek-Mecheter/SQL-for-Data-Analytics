# Analyzing Industry Carbon Emissions Project

## Overview

![Factories creating emissions](pollution.jpg)

This project aims to analyze industry carbon emissions using a PostgreSQL database containing product carbon footprints (PCFs) for various companies. The analysis includes examining trends in emissions, geographic variations, industry comparisons, company performance, and lifecycle analysis.

## Data Source

Our data, which is publicly available on [nature.com](https://www.nature.com/articles/s41597-022-01178-9), contains product carbon footprints (PCFs) for various companies. PCFs are the greenhouse gas emissions attributable to a given product, measured in CO<sub>2</sub> (carbon dioxide equivalent).

This data is stored in a PostgreSQL database containing one table, `prouduct_emissions`, which looks at PCFs by product as well as the stage of production that these emissions occurred. Here's a snapshot of what `product_emissions` contains in each column:

### Table Structure

| Field                        | Data Type  |
|------------------------------|------------|
| id                           | VARCHAR    |
| year                         | INT        |
| product_name                 | VARCHAR    |
| company                      | VARCHAR    |
| country                      | VARCHAR    |
| industry_group               | VARCHAR    |
| weight_kg                    | NUMERIC    |
| carbon_footprint_pcf         | NUMERIC    |
| upstream_percent_total_pcf   | VARCHAR    |
| operations_percent_total_pcf | VARCHAR    |
| downstream_percent_total_pcf | VARCHAR    |

## Project Steps

### 1. Data Cleaning

- Handled missing values by replacing them with 'N/A' or NaN.
- Standardized data formats by removing extra characters (e.g., '"') and converting to appropriate data types.
- Removed duplicate rows to ensure each observation is unique.

### 2. Exploratory Data Analysis (EDA) Using SQL

#### Trend Analysis

- Examined how carbon emissions from different industries have changed over time.
- Identified trends in emissions to understand factors driving these changes.

#### Geographic Analysis

- Explored variations in carbon emissions across different countries or regions.
- Analyzed geographic patterns in emissions intensity and emission sources.

#### Industry Comparison

- Compared carbon emissions between different industries to identify sectors with the highest emissions and those with the greatest potential for emission reduction.

#### Company Performance

- Assessed the carbon footprint of individual companies within each industry to identify leaders in emission reduction efforts.

#### Lifecycle Analysis

- Analyzed the carbon footprint of products at different stages of their lifecycle, from production to transportation to disposal.
- Identified stages contributing the most to overall emissions to prioritize emission reduction strategies.

## Conclusion

This project provides valuable insights into industry carbon emissions, highlighting trends, geographic variations, industry comparisons, company performance, and lifecycle analysis. The findings can inform decision-making and guide emission reduction efforts to mitigate environmental impact.
