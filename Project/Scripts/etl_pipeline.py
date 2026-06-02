import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

file_path = r"C:\data_engineering_project\Project\data\sales_data_sample.csv"

df = pd.read_csv(file_path, encoding='latin1')

print("Missing Values:")
print(df.isnull().sum())

print("\nOriginal Shape:", df.shape)

df = df.drop_duplicates()

df['ORDERDATE'] = pd.to_datetime(
    df['ORDERDATE'],
    errors='coerce'
)

df = df.dropna(subset=['SALES', 'ORDERDATE'])

df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month

print("\nCleaned Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
#creating python to sql database connection
username = 'root'
password = quote_plus("Ranjeet@143")
host = 'localhost'
port = '3306'
database = 'ecommerce_project'
# Create MySQL engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
print("MySQL Database Connected Successfully")

# Load dataframe into MySQL
df.to_sql("sales_data", engine, if_exists='replace', index=False)
print("Data Loaded Successfully")
