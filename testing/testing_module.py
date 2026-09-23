import pandas as pd
books = pd.read_csv("data/library.csv") # we've pulled the data and store in a dataframe called books
# print(books.head())
customers = pd.read_csv("data/library_customers.csv")

def clean_titles(df):
    """Strip the trailing spaces the library export leaves behind"""
    out = df.copy()
    out['Books'] = out['Books'].str.strip()
    return out

count_of_trailing_spaces = books['Books'].str.endswith(" ").sum()
print(f"count of whitespace {count_of_trailing_spaces}")
recount_trailing_spaces = clean_titles(books)['Books'].str.endswith(" ").sum()
print(f"recount: {recount_trailing_spaces}")



import pandas as pd
# def test_customer_id_never_missing():
#     books = pd.read_csv("data/library.csv").dropna(subset=['Id']) # subset for id
#     n = books['Customer ID'].isna().sum() # 0
#     assert int(n) == 0, f"{n} loans have no customers"
# try:
#     test_customer_id_never_missing()
# except AssertionError as e:
#     print(e)



na_books = pd.read_csv("data/library.csv").dropna(subset=['Id'])
print(na_books)


