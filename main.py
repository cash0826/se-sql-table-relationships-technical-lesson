import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Sometimes JOIN does not increase the number of records, in this example, each employee is associated to one office.

## Employee to office (One-to-Many)

# q = """
# SELECT firstName, lastName, email, city
# FROM employees
# JOIN offices
#   USING(officeCode)
# WHERE jobTitle = 'Sales Rep'
# ;
# """
# df = pd.read_sql(q, conn)
# print("Number of results:", len(df))
# print(df)


# Sometimes the number of records will increase to match the number of records in the larger table. 

## Product Line with Products (One-to-Many)
## The number of records increased because the same product line is now appearing multiple times in the results, once per actual product

# q = """
# SELECT productLine, textDescription, productVendor, productDescription
# FROM productlines
# JOIN products
#     USING(productLine)
# ;
# """
# df = pd.read_sql(q, conn)
# print("Number of results:", len(df))


# Joined Offices with Customers (Many-to-Many)

q = """
SELECT *
FROM offices
JOIN customers
  USING(state)
;
"""

df = pd.read_sql(q, conn)
print('Number of results:', len(df))
print(df)

conn.close()