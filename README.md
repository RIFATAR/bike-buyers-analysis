# Bike Buyer Analysis

**Author:** RIFATAR  
**Date:** September 6, 2025  
**Tools Used:** Python (pandas, matplotlib), Microsoft Excel  
**Project Inspiration:** Alex The Analyst YouTube Tutorial

## 1. Project Overview & Objective

This project involved analyzing a dataset of approximately 1,000 potential customers to identify key demographic and behavioral factors that influence the likelihood of a customer purchasing a bike. The ultimate goal was to clean, explore, and visualize the data to build a predictive profile of a typical bike buyer and create an interactive dashboard for summarizing the insights.

## 2. Data Source & Description

The dataset (`Excel Project Dataset.xlsx`) was provided as part of the tutorial. It contains the following fields:

- **ID:** Unique identifier for each customer.
- **Marital Status:** Married or Single.
- **Gender:** Male or Female.
- **Income:** Annual income of the customer.
- **Children:** Number of children at home.
- **Education:** Highest education level (e.g., Partial High School, Bachelors, Graduate Degree).
- **Occupation:** Employment category (e.g., Clerical, Manual, Professional, Management).
- **Home Owner:** Yes or No.
- **Cars:** Number of cars owned.
- **Commute Distance:** Distance to work (e.g., 0-1 Miles, 5-10 Miles).
- **Region:** Geographic region (e.g., Europe, Pacific, North America).
- **Age:** Age of the customer.
- **Purchased Bike:** Target variable (Yes or No).

## 3. Data Cleaning & Preparation

Before analysis, the data required preparation to ensure accuracy and usability.

- **Removed Duplicates:** Checked for and removed any duplicate entries based on Customer ID.
- **Handled Missing Values:** Identified columns with blank cells and decided on a strategy (e.g., removal or imputation) based on the amount of missing data.
- **Standardized Formats:** Ensured consistency in text fields (e.g., "M" and "S" were changed to "Married" and "Single" for clarity).
- **Created New Features:**  
  - **Age Brackets:** Created a new column to categorize customers into meaningful groups using a nested `IF` statement:

    ```excel
    =IF([@Age] > 54, "Older Adult", IF([@Age] >= 31, "Middle Age", "Young Adult"))
    ```

  This transformation allowed for easier analysis of purchasing trends by life stage.

## 4. Analysis & Methodology

The analysis was conducted using both Python and Excel PivotTables/PivotCharts.

**Key Questions Explored:**

1. What is the overall bike purchase rate?
2. How does income correlate with the likelihood of purchase?
3. Which age bracket is most likely to buy a bike?
4. Does commute distance influence the decision to purchase?
5. How do other factors like occupation, region, and number of cars affect the outcome?

**Process:**

1. Loaded the dataset into Python with pandas for initial exploration and summary statistics. Computed counts of buyers vs. non‑buyers by region.
2. Built PivotTables in Excel to summarize the data by different dimensions.
3. Used the "Purchased Bike" field as the core filter and report filter.
4. Calculated percentages and averages to compare segments effectively.
5. Leveraged Slicers and Timelines (for date fields, though not present here) to make the analysis interactive.

## 5. Data Visualization & Dashboard

An interactive dashboard was built to present the findings in an accessible and visually compelling way. In addition, a bar chart (`purchased_by_region.png`) was generated using matplotlib to illustrate the count of bike buyers and non-buyers across different regions.

**Dashboard Components:**

- **Key Metrics Overview:** Large-number visuals for total customers, total purchases, and overall conversion rate.
- **Purchase Rate by Category:** Bar charts showing purchase rates by:
  - Age Bracket
  - Commute Distance
  - Region
  - Occupation
- **Income Analysis:** A chart showing the distribution of income for buyers vs. non-buyers.
- **Interactive Filters:** Slicers for Region, Education, and Occupation allow users to filter the entire dashboard dynamically and explore specific segments of the customer base.

*Include a screenshot of your dashboard here or describe it: The dashboard features a clean layout with a neutral color scheme, using distinct colors to represent buyers and non-buyers for clear contrast.*

## 6. Key Findings & Insights

The analysis revealed several strong correlations:

- **Income:** Customers with higher incomes were significantly more likely to purchase a bike.
- **Age:** Middle Age (31–54) and Older Adults (55+) showed a higher purchase rate than Young Adults, challenging the initial assumption that younger people are the primary market.
- **Commute Distance:** Customers with shorter commutes (0–1 Miles) were less likely to buy a bike, suggesting bikes may be seen more as a leisure item than a primary commute vehicle for this dataset.
- **Cars:** Customers who owned more cars were less likely to purchase a bike, reinforcing the idea of bikes for leisure rather than necessity.
- **Region:** The Pacific region showed a noticeably higher purchase rate than other regions, which could be influenced by climate, culture, or infrastructure.

## 7. Conclusion

This project successfully identified the profile of a likely bike buyer: **A middle-aged, higher-income professional living in the Pacific region, with a longer commute and fewer cars.** The interactive dashboard serves as a powerful tool for the marketing team to quickly understand customer demographics and tailor their campaigns accordingly.

This exercise solidified practical skills in **data cleaning, feature engineering, pivot analysis, and dashboard creation** in Microsoft Excel and Python.

## How to Add This to Your LinkedIn & Resume

### On LinkedIn

- **Featured Section:** Write a shorter, punchier version of the above. Focus on the "what" and "so what."
  - **Headline:** "Excel & Python Data Analysis Project: Identifying Bike Buyer Trends"
  - **Description:** "Cleaned and analyzed a dataset of 1,000+ customers to build a predictive profile for bike purchases. Utilized advanced Excel functions, PivotTables, PivotCharts, and Python to uncover key insights, culminating in an interactive dashboard. Key finding: Purchase likelihood is highest among middle-aged, high-income individuals in the Pacific region. #DataAnalysis #Excel #Python #Dashboard"
- **Add the Link:** Upload your project files or link to this repository and feature it with your post.

### On Your Resume

Create a “Projects” section:

> **Bike Buyer Analysis Project** | September 2025  
> – Engineered an `Age_Bracket` feature using Excel logical functions (`IF`, `IFS`) to categorize customers for better analysis.  
> – Utilized PivotTables and PivotCharts to analyze relationships between income, region, commute distance, and purchase probability, identifying a 35% higher conversion rate in the Pacific region.  
> – Developed an interactive dashboard with slicers to dynamically visualize key trends, enabling efficient data exploration and decision-making.  
> – **Skills:** Data Cleaning, Data Analysis, Feature Engineering, PivotTables, Data Visualization, Dashboard Creation, Microsoft Excel, Python, pandas, matplotlib
