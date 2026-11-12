import pandas as pd

data = pd.read_csv('Ecommerce.csv')

data["Order_Date"] = pd.to_datetime(data["Order_Date"])

data["Ship_Date"] = pd.to_datetime(data["Ship_Date"])


column_name = ["Order_ID","Customer_ID","Customer_Name","Customer_Segment","Region","City","Category","Product","Payment_Method","Order_Status"]

for col in column_name:
    data[col] = data[col].str.strip() 

data.fillna({"Customer_Segment":"Unknown"},inplace=True)

data.fillna({"Payment_Method":"Unknown"},inplace=True)

data.fillna({"Discount":0},inplace=True)

data["Profit_Margin"] = (data["Profit"]/data["Sales"])*100

data["Order_Year"] = data["Order_Date"].dt.year

data["Order_Month"] = data["Order_Date"].dt.month

data["Order_Month_Name"] = data["Order_Date"].dt.strftime("%B")

# data["Order_Date"] = pd.to_datetime(data["Order_Date"],dayfirst=True).dt.strftime("%Y-%m-%d")

# data["Ship_Date"] = pd.to_datetime(data["Ship_Date"],dayfirst=True).dt.strftime("%Y-%m-%d")

data.drop(columns=["Unnamed: 19","Unnamed: 20","Unnamed: 21"],inplace=True)

# data.to_csv("ecommerce_cleaned_data.csv", index=False)

# print(data)

data["Order_Date"] = pd.to_datetime(
    data["Order_Date"], dayfirst=True
).dt.strftime("%Y-%m-%d")

data["Ship_Date"] = pd.to_datetime(
    data["Ship_Date"], dayfirst=True
).dt.strftime("%Y-%m-%d")

data.to_csv("ecommerce_cleaned_data_mysql.csv", index=False)



data.to_csv("Cleaned_data.csv",index=False)

print(data)







