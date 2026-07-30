#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import streamlit as st

#df = pd.read_csv("cleaned_online_retail.csv")

#print(df.head())


# ============================================================
# WEEK 3 INTERNSHIP TASK
# Interactive Online Retail Dashboard using Streamlit
# ============================================================

# Import the libraries needed to build the dashboard and work with data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

# Set the browser tab title, icon, and make the page wide for better display
st.set_page_config(
    page_title="Online Retail Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# 2. TITLE
# ============================================================

# Display the main title of the dashboard at the top of the page
st.title("🛒 Online Retail Sales Dashboard")

# Show a short welcome message describing what the dashboard does
st.write(
    "An interactive dashboard for exploring online retail sales "
    "using filters and visualizations."
)


# ============================================================
# 3. LOAD DATASET
# ============================================================

# Cache the loaded data so Streamlit does not reload it every time the app refreshes
@st.cache_data
def load_data():

    # Read the CSV file containing the online retail data
    df = pd.read_csv(
        "cleaned_online_retail.csv",
        encoding="latin1"
    )

    # Return the loaded data so it can be used later in the script
    return df


# Call the function and store the data in a variable for later use
df = load_data()


# ============================================================
# 4. DATA PREPARATION
# ============================================================

# Convert the invoice date column into a proper datetime format
# This allows the data to be used for time-based analysis later
# If any date is invalid, it will become missing instead of causing an error
# because errors="coerce" is used

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)


# Create a new TotalPrice column if it is not already present
# This is calculated by multiplying quantity by unit price
if "TotalPrice" not in df.columns:

    df["TotalPrice"] = (
        df["Quantity"] * df["UnitPrice"]
    )


# Remove rows that have missing values in important columns
# This keeps the dashboard cleaner and avoids errors in calculations
# The subset list defines which columns must not be empty

df = df.dropna(
    subset=[
        "Country",
        "Description",
        "Quantity",
        "UnitPrice",
        "TotalPrice"
    ]
)


# ============================================================
# 5. SIDEBAR FILTERS
# ============================================================

# Create a sidebar section where users can filter the data
st.sidebar.header("🔎 Dashboard Filters")


# ------------------------------------------------------------
# FILTER 1: COUNTRY
# ------------------------------------------------------------

# Get the list of countries from the data and sort them alphabetically
countries = sorted(
    df["Country"].dropna().unique()
)

# Create a dropdown for choosing a country or viewing all countries
selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All Countries"] + countries
)


# ------------------------------------------------------------
# FILTER 2: PRICE RANGE
# ------------------------------------------------------------

# Find the minimum and maximum total price values in the dataset
min_price = float(df["TotalPrice"].min())
max_price = float(df["TotalPrice"].max())

# Create a slider so the user can choose a price range to display
selected_price = st.sidebar.slider(
    "Select Total Price Range",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)


# ============================================================
# 6. APPLY FILTERS
# ============================================================

# Start with a copy of the full dataframe so the original data remains unchanged
filtered_df = df.copy()


# Apply the country filter if the user selected a specific country
if selected_country != "All Countries":

    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]


# Apply the price range filter using the selected minimum and maximum prices
filtered_df = filtered_df[
    (filtered_df["TotalPrice"] >= selected_price[0])
    &
    (filtered_df["TotalPrice"] <= selected_price[1])
]


# ============================================================
# 7. DASHBOARD SUMMARY / KPIs
# ============================================================

# Create a summary heading for the key performance indicators
st.subheader("📊 Dashboard Summary")


# Create four columns to show the KPI cards side by side
col1, col2, col3, col4 = st.columns(4)


# Show the total number of transactions after filtering
col1.metric(
    "Transactions",
    f"{len(filtered_df):,}"
)


# Show the total number of units sold
col2.metric(
    "Units Sold",
    f"{filtered_df['Quantity'].sum():,.0f}"
)


# Show the total sales amount formatted as currency
col3.metric(
    "Total Sales",
    f"${filtered_df['TotalPrice'].sum():,.2f}"
)


# Calculate the average sales value, or use 0 if no data exists
if len(filtered_df) > 0:

    average_sale = filtered_df["TotalPrice"].mean()

else:

    average_sale = 0


# Display the average sale amount in the fourth KPI card
col4.metric(
    "Average Sale",
    f"${average_sale:,.2f}"
)


# ============================================================
# 8. CHECK IF DATA EXISTS
# ============================================================

# If the filtered data is empty, show a warning and stop the app
if filtered_df.empty:

    st.warning(
        "No data is available for the selected filters. "
        "Please change the filters."
    )

    st.stop()


# ============================================================
# 9. VISUALIZATION 1
# TOP 10 PRODUCTS BY SALES
# ============================================================

# Show a chart for the top 10 products by sales value
st.subheader("🏆 Top 10 Products by Sales")


# Group the data by product description and calculate total sales per product
# Then sort and keep the top 10 products
# The final sort makes the chart easier to read

top_products = (
    filtered_df
    .groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)


# Create a horizontal bar chart for the top products
fig1, ax1 = plt.subplots(
    figsize=(10, 6)
)


top_products.plot(
    kind="barh",
    ax=ax1
)


# Add labels and a title to the chart
ax1.set_title(
    "Top 10 Products by Total Sales"
)

ax1.set_xlabel(
    "Total Sales"
)

ax1.set_ylabel(
    "Product"
)

# Make the layout look neat before displaying the chart
plt.tight_layout()


# Display the chart in the Streamlit app
st.pyplot(fig1)


# ============================================================
# 10. VISUALIZATION 2
# MONTHLY SALES TREND
# ============================================================

# Show a line chart of monthly sales over time
st.subheader("📈 Monthly Sales Trend")


# Copy the filtered data and create a new month column for grouping
monthly_data = filtered_df.copy()

monthly_data["Month"] = (
    monthly_data["InvoiceDate"]
    .dt.to_period("M")
    .astype(str)
)


# Group sales by month and calculate the total for each month
monthly_sales = (
    monthly_data
    .groupby("Month")["TotalPrice"]
    .sum()
)


# Create a line chart for monthly sales trend
fig2, ax2 = plt.subplots(
    figsize=(12, 5)
)


monthly_sales.plot(
    kind="line",
    marker="o",
    ax=ax2
)


# Add chart titles and labels
ax2.set_title(
    "Monthly Sales Trend"
)

ax2.set_xlabel(
    "Month"
)

ax2.set_ylabel(
    "Total Sales"
)

# Rotate the month labels so they are easier to read
plt.xticks(
    rotation=45
)

plt.tight_layout()


# Display the monthly sales chart
st.pyplot(fig2)


# ============================================================
# 11. VISUALIZATION 3
# TOP 10 COUNTRIES BY SALES
# ============================================================

# Show a chart for the top countries by sales
st.subheader("🌍 Top Countries by Sales")


# Group sales by country and keep the top 10 countries
country_sales = (
    filtered_df
    .groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)


# Create the horizontal bar chart for countries
fig3, ax3 = plt.subplots(
    figsize=(10, 6)
)


country_sales.plot(
    kind="barh",
    ax=ax3
)


# Add title and axis labels to the country chart
ax3.set_title(
    "Top 10 Countries by Sales"
)

ax3.set_xlabel(
    "Total Sales"
)

ax3.set_ylabel(
    "Country"
)

plt.tight_layout()


st.pyplot(fig3)


# ============================================================
# 12. ADDITIONAL VISUALIZATION
# QUANTITY SOLD BY PRODUCT
# ============================================================

# Show another chart for the top products by total quantity sold
st.subheader("📦 Top 10 Products by Quantity Sold")


# Group the filtered data by product description and sum the quantities sold
# Then keep the top 10 products with the highest quantity sold

top_quantity = (
    filtered_df
    .groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)


# Create a horizontal bar chart for quantity sold
fig4, ax4 = plt.subplots(
    figsize=(10, 6)
)


top_quantity.plot(
    kind="barh",
    ax=ax4
)


# Add title and axis labels to the quantity chart
ax4.set_title(
    "Top 10 Products by Quantity Sold"
)

ax4.set_xlabel(
    "Quantity Sold"
)

ax4.set_ylabel(
    "Product"
)

plt.tight_layout()


# Display the quantity chart
st.pyplot(fig4)


# ============================================================
# 13. FILTERED RAW DATA TABLE
# ============================================================

# Show a section for the filtered raw data
st.subheader("📋 Filtered Raw Data")


# Explain how many records are currently visible after the filters are applied
st.write(
    f"Showing {len(filtered_df):,} records after applying filters."
)


st.dataframe(
    filtered_df,
    use_container_width=True
)


# ============================================================
# 14. DOWNLOAD FILTERED DATA
# ============================================================

# Add a download section so users can save the filtered data as a CSV file
st.subheader("⬇️ Download Filtered Data")


# Convert the filtered dataframe into CSV text for downloading
csv = filtered_df.to_csv(
    index=False
)


st.download_button(
    label="Download Filtered CSV",
    data=csv,
    file_name="filtered_online_retail.csv",
    mime="text/csv"
)


# ============================================================
# 15. FOOTER
# ============================================================

# Add a divider line and footer text at the bottom of the dashboard
st.markdown("---")

st.write(
    "Online Retail Sales Dashboard | "
    "Data Science & Analytics Internship - Week 3"
)