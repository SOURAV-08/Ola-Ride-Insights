import pandas as pd 

df = pd.read_excel('first project/OLA_PROJECT/OLA_DataSet.xlsx')

print(df.head())
print(df.info())
print(df.describe())

# Remove duplicates
print("Remove duplicates\n")
df.drop_duplicates()

# remove useless column
print("remove useless column")
df = df.drop(columns=["Vehicle Images"])

# Convert date column 
print("Convert date column \n")
df["Date"] = pd.to_datetime(df["Date"])

# Check missing values
print("Check missing values\n")
print(df.isnull().sum())

# Make Correct Cleaning Decision 
# Columns that must be filled
# df.["Payment_Method"].fillna("Unknown", inplace = True)  (old method but still work)

df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")

#Driver_Ratings and Customer_Rating
df["Driver_Ratings"].fillna(0, inplace=True)
df["Customer_Rating"].fillna(0, inplace=True)

# V_TAT and C_TAT ---> These are time metrics (Vehicle arrival time / Customer waiting time).

df["V_TAT"].fillna(df["V_TAT"].median(), inplace=True)
df["C_TAT"].fillna(df["C_TAT"].median(), inplace=True)

# Cancellation Columns---> These should not stay NULL.

df["Canceled_Rides_by_Customer"].fillna(0, inplace=True)
df["Canceled_Rides_by_Driver"].fillna(0, inplace=True)
df["Incomplete_Rides"].fillna(0, inplace=True)

# Incomplete_Rides_Reason ---> Missing means ride completed.

df["Incomplete_Rides_Reason"].fillna("Completed", inplace=True)

print(df.isnull().sum())

print(df.info())


# Save cleaned dataset
print("Save cleaned dataset")

df.to_csv("clean_ola_dataset.csv", index = False)




'''import pandas as pd
from sqlalchemy import create_engine

# 1. Load the data (using the path we fixed earlier)
path = 'first project/OLA_PROJECT/OLA_DataSet.xlsx'
df = pd.read_excel(path)

# 2. Basic Cleaning (Example: filling missing values)
df['Payment_Method'] = df['Payment_Method'].fillna('Unknown')

# 3. Create Connection to MySQL
# Format: 'mysql+mysqlconnector://user:password@host/database'
engine = create_engine('mysql+mysqlconnector://root:PASTE_PASSWORD_HERE@localhost/ola_project')

# 4. Push data to MySQL (Creates a table named 'rides')
df.to_sql('rides', con=engine, if_exists='replace', index=False)

print("Success! Your OLA data is now in MySQL.")'''