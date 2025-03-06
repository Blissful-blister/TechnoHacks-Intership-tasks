Data Science Internship Tasks

Task Overview
This repository contains two tasks related to data preprocessing, feature engineering, and exploratory data analysis (EDA) using Python and the Pandas, NumPy, and Scikit-Learn libraries.

Task 1: Analyzing House Prices
Dataset
The dataset consists of the following features:
- Square_feet: The area of the house in square feet.
- Bedroom_number: Number of bedrooms.
- Bathroom_number: Number of bathrooms.
- Year_built: Year the house was built.
- Price: Target variable (house price).

Feature Engineering & Data Processing
New features were created to enhance data insights:
- House_age: 2025 - Year_built
- Rooms/1000sqft: (Bedroom_number + Bathroom_number) / Square_feet * 1000
- Is_newhouse: A binary indicator for houses built after 2015.

Additionally, the dataset was analyzed using:
- Descriptive statistics
- Correlation analysis
- Visualization techniques (e.g., histograms, scatter plots)

Task 2: Data Cleaning & Preprocessing 
Task 2 involves cleaning another dataset, the following techniques were used:
- Handling missing values
- Removing duplicates
- Encoding categorical variables
- Normalization & standardization where necessary

Installation & Usage
To run the project:
1. Clone the repository:
   ```bash
   git clone https://github.com/Blissful-blister/TechnoHacks-Intership-tasks
   ```
2. Run the script in Spyder or another Python environment.

Possible Improvements
- Conduct deeper exploratory data analysis (EDA) for better insights.
- Apply advanced feature engineering techniques.
- Use interactive visualizations with libraries like; Plotly or Seaborn.

Author
- Boipelo



