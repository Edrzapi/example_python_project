import pandas as pd 

books = pd.read_csv("data/library.csv") # we've pulled the data and store in a dataframe called books
# print(books.head())
customers = pd.read_csv("data/library_customers.csv")
# print(customers.head())

print(books.shape) # print dimensions of my data frame
count = books.isnull().all().sum() # count empty values in "books"
real = books.dropna(how="any") # if a column is missing a value, drop it and return DF
print(real.shape)
print(real)

# books['Id'] # points to the id column in the dataframe
three_books = books['Id'].head(3).tolist() # using key/value pair mapping to identify 3 books from the top of the DF
print(three_books)
print(books.dtypes) # identify the type of datatype the df is using, e.g. Dtype = float64 (float64 is the standard promotion
# pandas will use when given NaN errors, text, etc)
# pd.to_datetime(arg, error=coerce) # coerce is a error hunting tool, which strips the standard process of 
# "raise error" aware from nan, etc values, so we can perform agg (sum, max, etc) functions on a series/df
silence_the_errors = pd.to_datetime(books['Book checkout'], errors="coerce", dayfirst=True)
print(silence_the_errors.dtype)
print(silence_the_errors.isnull().sum())
print(silence_the_errors.isna().sum())