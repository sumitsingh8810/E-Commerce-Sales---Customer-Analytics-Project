# 🛒 E-Commerce Sales & Customer Analytics | Python, SQL & Power BI


## 📌 Project Overview

The **E-Commerce Sales & Customer Analytics** project is an end-to-end data analytics project focused on analyzing sales performance, customer behavior, product performance, and business profitability.

Using **Python (Pandas)** for data cleaning and preprocessing, **MySQL** for SQL-based analysis, and **Power BI** for interactive visualization, this project transforms raw e-commerce data into meaningful business insights.

The project focuses on understanding revenue trends, identifying top-performing products and customers, analyzing customer segments, and evaluating profitability across different regions and categories.

## 🎯 Project Objectives

- Analyze overall e-commerce sales performance.
- Evaluate total revenue and profitability.
- Identify top-performing products and customers.
- Understand customer purchasing patterns.
- Analyze sales across different product categories.
- Compare regional sales and profit performance.
- Evaluate customer segment performance.
- Analyze payment methods and order status.
- Develop an interactive Power BI dashboard.

## 📊 Dataset Overview

| Metric                   | Details |
| ------------------------ | ------: |
| Total Orders             |   1,500 |
| Total Customers          |     390 |
| Product Categories       |       5 |
| Power BI Dashboard Pages |       3 |

### Dataset Columns

- Order_ID
- Order_Date
- Ship_Date
- Customer_ID
- Customer_Name
- Customer_Segment
- Region
- City
- Category
- Product
- Quantity
- Unit_Price
- Discount
- Sales
- Cost
- Profit
- Payment_Method
- Order_Status

## 🛠️ Tools & Technologies

| Technology  | Application                     |
| ----------- | ------------------------------- |
| Python      | Data cleaning and preprocessing |
| Pandas      | Data manipulation and analysis  |
| NumPy       | Numerical operations            |
| MySQL       | SQL-based business analysis     |
| Power BI    | Interactive dashboards          |
| DAX         | KPI calculations and measures   |
| Power Query | Data transformation             |
| CSV / Excel | Dataset management              |

## 🔄 Project Workflow

### 1. Data Understanding

- Explored the dataset structure and 18 columns.
- Examined sales, customer, product, and order information.
- Identified missing values and data inconsistencies.

### 2. Data Cleaning Using Python

Used Python and Pandas to clean and prepare the raw dataset.

Key activities:

- Handled missing and inconsistent values.
- Converted Order_Date and Ship_Date into datetime formats.
- Standardized text columns using string operations.
- Converted numerical columns into appropriate data types.
- Created additional analytical columns:
  - Profit_Margin
  - Order_Month
  - Order_Month_Name
  - Order_Year
- Exported the cleaned dataset as `ecommerce_sales_cleaned.csv`.

### 3. SQL Analysis Using MySQL

Imported the cleaned dataset into MySQL and performed business analysis.

SQL concepts applied:

- SELECT, WHERE and ORDER BY
- GROUP BY and HAVING
- Aggregate Functions
- CASE Statements
- Joins
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- Date-based Analysis

### 4. Power BI Dashboard Development

- Imported cleaned data into Power BI.
- Created DAX measures for business KPIs.
- Designed a three-page interactive dashboard.
- Developed visualizations for sales, customers, products, and profitability.
- Added slicers and filters for interactive analysis.

## 📈 Power BI Dashboard

The Power BI dashboard consists of three analytical pages.

### Page 1: Executive Overview

Provides a high-level overview of overall business performance.

**Key Performance Indicators (KPIs):**

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Orders Value
- Total Profit Margin

**Visualizations:**

- Monthly Sales Trend
- Sales by Category
- Total Sales by Region
- Order Status Distribution

**Interactive Filters:**

- Order Date
- Region
- Category
- Customer Segment

### Page 2: Product & Customer Analysis

Focuses on identifying top-performing products and analyzing customer purchasing behavior.

**Visualizations:**

- Top 10 Products by Sales
- Top 10 Products by Total Profit
- Total Sales by Customer Segment
- Quantity Sold by Category

**Customer Analysis:**

- Top 10 Customers by Total Sales
- Top 10 Customers by Profit
- Top 10 Customers by Total Orders

**Interactive Filters:**

- Category
- Region
- Customer Segment

### Page 3: Profitability & Operations Analysis

Focuses on business profitability, regional performance, and operational trends.

**Key Performance Indicators (KPIs):**

- Total Profit
- Average Orders Value
- Total Quantity

**Visualizations:**

- Monthly Profit
- Profit by Category
- Profit by Region
- Sales by Payment Method
- Order Status Distribution
- Profitability by Customer Segment

**Interactive Filters:**

- Order Date
- Region
- Category

## 💡 Business Questions Addressed

1. What is the overall sales and profit performance?
2. How do monthly sales trends change over time?
3. Which product categories generate the highest sales?
4. Which regions contribute the most to total revenue?
5. Which products generate the highest sales and profit?
6. Which customers contribute the most to overall sales?
7. Which customer segments generate the highest revenue?
8. How does profitability vary across different regions?
9. Which payment methods are most commonly used?
10. How are orders distributed across different order statuses?
11. Which customer segments contribute the most to profitability?

## 📚 Key Learnings

Through this project, I gained practical experience in:

- Cleaning and preprocessing real-world datasets using Python.
- Performing data manipulation with Pandas and NumPy.
- Writing SQL queries for business analysis.
- Identifying top-performing products and customers.
- Analyzing sales trends and profitability.
- Developing DAX measures and KPIs.
- Designing interactive multi-page Power BI dashboards.
- Converting raw business data into meaningful insights.

