import pandas as pd
import psycopg2
from sqlalchemy import create_engine
# 建立連線
connection = psycopg2.connect(user="postgres", password="951612", host="localhost",
                                       port="5432", database="ys_economic")
cursor = connection.cursor()
cursor.execute("select * from analyst.test_table;")
data = cursor.fetchall()
cols = list(map(lambda x: x.name, cursor.description))
dataframe = pd.DataFrame(data, columns=cols)
print(dataframe)