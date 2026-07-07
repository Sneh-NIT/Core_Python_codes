import pandas as pd
from sqlalchemy import create_engine

# # 1. Define your MySQL connection credentials
USERNAME = "root"
PASSWORD = "root"
HOST = "localhost"  # or 'localhost'
PORT = "3306"
DATABASE = "railway"

# # 2. Create the SQLAlchemy engine (using the pymysql driver)
connection_string = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_string)

# # 3. Read the CSV file into a Pandas DataFrame
csv_file_path = "train_stations.csv"
df = pd.read_csv(csv_file_path)

# # 4. Upload the data to your MySQL database
table_name = "train_stations"
df.to_sql(
    name=table_name,
    con=engine,
    if_exists="replace",  # Options: 'fail', 'replace', 'append'
    index=True,  # Set to True if you want the CSV index saved as a column
)

print(f"Successfully uploaded data to the '{table_name}' table!")
