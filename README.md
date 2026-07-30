# Interactive Online Retail Sales Dashboard using Streamlit

## Project Overview

This project is a Streamlit-based interactive dashboard built with Python to explore a cleaned Online Retail dataset. It allows users to filter sales data by country and total price range, view key performance indicators (KPIs), inspect interactive visualizations, and download the filtered dataset for further analysis. The dashboard is designed to be accessible for beginners and suitable as a Week 3 internship project submission.

## Features

- Load and display a pre-cleaned Online Retail dataset
- Interactive filters for:
  - Country selection
  - Total Price range slider
  - (Optional) Date range and product filters
- Dynamic KPIs:
  - Total sales (sum of Total Price)
  - Number of orders
  - Number of unique customers
  - Average order value
- Visualizations:
  - Time series of sales
  - Top selling products
  - Sales by country (bar / choropleth)
  - Distribution of order values
- Filtered raw data table with pagination
- Download button to export filtered data as CSV
- Beginner-friendly UI using Streamlit widgets and Plotly / Seaborn for charts

## Technologies Used

- Python 3.8+ (recommended)
- Streamlit for the interactive dashboard
- pandas and numpy for data manipulation
- Plotly / Matplotlib / Seaborn for visualizations
- openpyxl (if dataset is in Excel)
- Git and GitHub for version control and submission

## Project Structure

Recommended project layout (adjust if your actual repo differs):
- task3.py                # Main Streamlit app (run with `streamlit run task3.py`)
- data/
  - online_retail_cleaned.csv  # Pre-cleaned dataset (place dataset here)
- requirements.txt        # Python dependencies
- README.md               # This file
- .gitignore

If your filenames differ, update the commands below accordingly.

## Dataset Information

- Dataset: Cleaned Online Retail dataset (a cleaned version of the typical "Online Retail" dataset)
- Expected columns (typical):
  - InvoiceNo
  - StockCode
  - Description
  - Quantity
  - InvoiceDate
  - UnitPrice
  - CustomerID
  - Country
  - TotalPrice (Quantity * UnitPrice) — may already be present in the cleaned file
- Placement: Put the cleaned dataset in `data/online_retail_cleaned.csv` or update the path in `task3.py`.

## Dashboard Visualizations

The dashboard includes the following visual outputs:
- KPI cards at the top (Total Sales, Orders, Unique Customers, Avg Order Value)
- Sales over time: a line chart showing revenue trend (daily / monthly)
- Top N products: bar chart of best-selling items by revenue or quantity
- Sales by country: bar chart (or choropleth if country codes available)
- Distribution plots: histograms or boxplots for order values and quantities
- Raw data table: shows filtered rows with sorting and paging

## Interactive Filters

- Country: single-select or multi-select dropdown to focus analysis on a country or group of countries
- Total Price Range: slider to limit results by the order total (min → max)
- (Optional) Date range selector to focus on particular time periods
- (Optional) Product or category filter to drill into specific SKUs

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Muneeza-Siddiqui/Vortextech-DS-WEEK-3.git
   cd Vortextech-DS-WEEK-3
   ```
2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If you don't have a requirements file, install the main libraries:
   ```bash
   pip install streamlit pandas numpy plotly seaborn openpyxl
   ```

## How to Run the Project

- Ensure the cleaned dataset is placed in the `data/` folder (or update the data path in `task3.py`).
- Run the Streamlit app:
  ```bash
  streamlit run task3.py
  ```
- A local browser window will open with the dashboard (usually at http://localhost:8501).

## Required Libraries

- streamlit
- pandas
- numpy
- plotly
- seaborn (optional)
- matplotlib (optional)
- openpyxl (if dataset is .xlsx)
- (Optional) scikit-learn (if any modeling/preprocessing is added)

You can create a `requirements.txt` like:
```
streamlit
pandas
numpy
plotly
seaborn
openpyxl
```

## Example Command
To launch the dashboard from the project root, run:
```bash
streamlit run task3.py
```

## Expected Output
When the app runs successfully you will see:
- A clean header with the project title and short description
- Interactive widgets (country select, total price slider) on the sidebar
- KPI cards showing aggregated metrics
- Interactive charts that update when filters change
- A table displaying filtered raw rows and a button to download the filtered dataset as CSV

Screenshots (if available) can be added to this README to show the layout, KPIs, and charts.

## Future Improvements

- Add date range filter and time granularity controls (daily / weekly / monthly)
- Add product category analysis and user cohort segmentation
- Implement caching for faster filtering on large datasets
- Add map-based visualizations (choropleth) for global sales if country codes available
- Improve UI/UX: theming, custom layouts, and mobile responsiveness
- Add automated tests for data-loading and preprocessing functions
- Deploy to Streamlit Cloud or another hosting platform for public access

## Author
Muneeza Siddiqui  
GitHub: [Muneeza-Siddiqui](https://github.com/Muneeza-Siddiqui)  
Email: (add your email here if you want to share it)

---

*README generated and updated by GitHub Copilot.*
