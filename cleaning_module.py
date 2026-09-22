import pandas as pd 


# pd.set_options("display.width", 200)
# pd.set_option("display.max_columns", 20) # on occassion, setting a default size allocation is beneficial to
# our dev 


books = pd.read_csv("data/library.csv") # we've pulled the data and store in a dataframe called books
# print(books.head())
customers = pd.read_csv("data/library_customers.csv")
print(customers.head()) # first 5 values (head - unix)
print(books.shape) # print dimensions of my data frame
books.columns.tolist() # print "title", "Book checkout", "id", etc
quant = len(books.to_string().splitlines()) # header count, row count, etc 

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

# loc value vs iloc index 
# books.loc('id')
output = books.loc[books.isnull().all(axis=1)].to_string()
print(output)
# when we don't let default fail/decide silently -> you decide the rows fate yourself
# the difference being in the early coerce examples, we handed control to the func, it promtoed what it could
# the rest was removed 

dropped_na = books.dropna(how=all) # little less harsh than any, e.g. row that is missing a single field 
dropped_na.shape # gives me the updated dimension 
dropped_na.isna.sum() # count for present na values, has it worked?
books.isna.sum() # compare with the above for missing value removeal 
# books["loan amount.."].mean() 

filled_value = data.fillna("value") # inplace errors, see value handed back to the col with a new type 
## this went from dtype flaot to text ^ value 
filled_value.isnull().sum().sum() # 0
filled_value["Customer"].tolist[-1] # value it ran, it isn't too useful, but it'll showcase the output
filled_value["Books"].toList() # list of remnaining books with value updated
filled_value["Books"].mean() # shows the mean book, similary mode, etc; can be applied here. 

# books.duplicated = true false true -> returns true for every row its seen before
dropped_na.duplicated().sum() # agg of the true returns 
deduped_dropped_na = dropped_na.drop_duplicates(subset="col") # common func 
deduped_dropped_na.shape # inspect 
deduped_dropped_na.describe.mean() # console mean 