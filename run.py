import pandas as pd
from sqlalchemy import create_engine


#CSV File Paths
events_path = "datasets/events.csv"
categories_path = "datasets/category_tree.csv"
item_properties_path = "datasets/item_properties_part1.csv"

#Read CSV Files
print("Reading CSV files...")
events = pd.read_csv(events_path)
categories = pd.read_csv(categories_path)
item_properties = pd.read_csv(item_properties_path)

# events.rename(columns={'itemid':'item_id'},inplace=True)

#Transform Data
print(events.head())
print(categories.head())
print(item_properties.head())   
print("Transforming data...")
events['timestamp'] = pd.to_datetime(events['timestamp'], unit='ms')
item_properties['timestamp'] = pd.to_datetime(item_properties['timestamp'], unit='ms')
categories.dropna(inplace=True)
categories.drop_duplicates(inplace=True)

#Connect to PostgreSQL
print("Connecting to PostgreSQL...")
engine = create_engine(f"postgresql://postgres:shahid@localhost:5432/retailrocket")

#Load to PostgreSQL
print("Loading data into PostgreSQL...")
events.to_sql('events', engine, if_exists='replace', index=False)
categories.to_sql('categories', engine, if_exists='replace', index=False)
item_properties.to_sql('item_properties', engine, if_exists='replace', index=False)

print("ETL Completed Successfully.")
