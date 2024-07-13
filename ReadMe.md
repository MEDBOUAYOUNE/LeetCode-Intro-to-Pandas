# Pandas Documentation README

## What is Pandas?

[**Pandas**](http://pandas.pydata.org/) is a Python library for data analysis. Started by [**Wes McKinney**](http://wesmckinney.com/pages/about.html) in 2008 out of a need for a powerful and flexible quantitative analysis tool, pandas has grown into one of the most popular Python libraries. It has an extremely active [**community of contributors**](https://github.com/pydata/pandas/graphs/contributors).

Source: [Mode](https://mode.com/python-tutorial/libraries/pandas)

## What is DataFrame?

`DataFrame` is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure in the Python programming language, provided by the pandas library. It is similar to a table in a database, an Excel spreadsheet, or a data frame in R.

### DataFrame Methods

- **Reading Data**: `pd.read_csv()`, `pd.read_excel()`, `pd.read_sql()`, etc.
- **Writing Data**: `df.to_csv()`, `df.to_excel()`, `df.to_sql()`, etc.
- **Accessing Data**: `.loc[]`, `.iloc[]`, `.at[]`, `.iat[]`
- **Manipulating Data**: `.drop()`, `.rename()`, `.sort_values()`, `.groupby()`

## What are Lists?

Lists are one of 4 built-in data types in Python used to store collections of data. The other 3 are [Tuple](https://www.w3schools.com/python/python_tuples.asp), [Set](https://www.w3schools.com/python/python_sets.asp), and [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp), all with different qualities and usage.

Source: [W3Schools](https://www.w3schools.com/python/python_lists.asp)

## Size of DataFrame

- `df.shape`: Provides a tuple (number of rows, number of columns).
- `len(df)`: Provides the number of rows.
- `len(df.columns)`: Provides the number of columns.
- `df.size`: Provides the total number of elements (rows * columns).
- `df.count().sum()`: Provides the total number of non-null cells.

## Selecting Data

For more information on selecting data, refer to the [pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html).

## DataFrame Operations

- **Drop Duplicates**: [pandas.DataFrame.drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)
- **Drop Missing Data**: [pandas.DataFrame.dropna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
- **Rename Columns**: [pandas.DataFrame.rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
- **Change Data-Types**: [pandas.DataFrame.astype](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)
- **Fill Missing Data**: [pandas.DataFrame.fillna](https://www.geeksforgeeks.org/python-pandas-dataframe-fillna-to-replace-null-values-in-dataframe/)
- **Concatenate DataFrames**: [pandas.concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
- **Pivot DataFrame**: [pandas.DataFrame.pivot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html)
- **Melt DataFrame**: [pandas.melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)

---

This README provides a basic overview of pandas and its essential functionalities. For more detailed information, please refer to the official [pandas documentation](https://pandas.pydata.org/).
