# Exploring London's Travel Network

## Introduction

London, or as the Romans called it "Londonium"! Home to [over 8.5 million residents](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/populationandhouseholdestimatesenglandandwales/census2021unroundeddata#population-and-household-estimates-england-and-wales-data) who speak over [300 languages](https://web.archive.org/web/20080924084621/http://www.cilt.org.uk/faqs/langspoken.htm). While the City of London is a little over one square mile (hence its nickname "The Square Mile"), Greater London has grown to encompass 32 boroughs spanning a total area of 606 square miles!

![underground train leaving a platform](tb.jpg)

Given the city's roads were originally designed for horse and cart, this area and population growth has required the development of an efficient public transport system! Since the year 2000, this has been through the local government body called **Transport for London**, or *TfL*, which is managed by the London Mayor's office. Their remit covers the London Underground, Overground, Docklands Light Railway (DLR), buses, trams, river services (clipper and [Emirates Airline cable car](https://en.wikipedia.org/wiki/London_cable_car)), roads, and even taxis.

![london](londoncity.jpg)

The Mayor of London's office makes their data available to the public [here](https://data.london.gov.uk/dataset). In this project, you will work with a slightly modified version of a dataset containing information about public transport journey volume by transport type.

The data has been loaded into a table called `TFL`, including the following data:

| Column | Definition | Data type |
|--------|------------|-----------|
| `MONTH`| Month in number format, e.g., `1` equals January | `INTEGER` |
| `YEAR` | Year | `INTEGER` |
| `DAYS` | Number of days in the given month | `INTEGER` |
| `REPORT_DATE` | Date that the data was reported | `DATE` |
| `JOURNEY_TYPE` | Method of transport used | `VARCHAR` |
| `JOURNEYS_MILLIONS` | Millions of journeys, measured in decimals | `FLOAT` |

## Data Cleaning

The dataset from TfL required some preprocessing to ensure its suitability for analysis:

- **Handling Missing Values**: Checked for missing values in key columns such as month, year, and journey type. No missing values were found, ensuring data integrity.
- **Data Type Conversion**: Ensured proper data types for each column, converting dates to the appropriate format and verifying numerical columns.
- **Quality Assurance**: Checked for any inconsistencies or anomalies in the data, ensuring accuracy and reliability for subsequent analysis.

## Exploratory Data Analysis (EDA)

### Trend Analysis

- **Overall Journey Volumes**: Analyzed the total volume of journeys over the years to identify trends and patterns. Observed a general upward trend with some fluctuations, including a significant decrease in 2020 likely due to the COVID-19 pandemic.

### Comparative Analysis

- **Transport Mode Comparison**: Compared journey volumes between different transport modes to understand usage patterns. Identified the Underground & DLR as the most utilized mode, followed by buses and overground rail services.

### Seasonal Analysis

- **Seasonal Patterns**: Examined average journey volumes for each month to uncover seasonal variations. Found spikes in journey volumes during spring and summer months, with peak travel observed in July, August, and September. Additionally, identified smaller spikes in December likely related to holiday travel.

## Conclusion

The analysis provides valuable insights into London's travel network, highlighting seasonal patterns and trends in journey volumes. Understanding these patterns is crucial for transportation planning, resource allocation, and enhancing the efficiency of London's public transport system.
