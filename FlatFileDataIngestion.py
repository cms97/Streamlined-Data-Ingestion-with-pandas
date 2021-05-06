""" Import Tax data published as a CSV by the Internal Revenue Service, the U.S. government's tax collection agency
Nature of data : Has information about household composition and income by ZIP code, making it useful for social
and economic analyses """

import pandas as pd
from matplotlib import pyplot as plt

tax_data = pd.read_csv('InputData/VTtaxdata16.csv')
print(tax_data.head())
print(tax_data.shape)
''' To read flat files with a different delimeter include the argument 'sep' for instance if tab is the delimeter
tax_data = pd.read_csv('InputData/VTtaxdata16.csv', sep="\t") '''


''' Limit the number of columnd and rows read using usecols & nrows keyword argument
Usecols can take a list of either all column names or all column numbers to import 
nrows is an integer of the maximum number of rows we want '''
vt_data_first500 = pd.read_csv("InputData/VTtaxdata16.csv", nrows=500)
print("First 500")
print(vt_data_first500.head(4))
print(vt_data_first500.shape)


'''we read the CSV, using nrows and skiprows to get the next 500 records, setting header to none,
 and passing the list of column names to names. Now our data frame has column names!'''
vt_data_next500 = pd.read_csv("InputData/VTtaxdata16.csv",
                              nrows=500,
                              skiprows=500,
                              header=None,
                              names=vt_data_first500.columns)
print("Next 500")
print(vt_data_next500.head(4))
print(vt_data_next500.shape)


# Plot the total number of tax returns by income group
tax_data.groupby("agi_stub").N1.sum().plot.bar()
plt.show()


# View counts of dependents and tax returns by income level
print(tax_data.groupby("agi_stub").sum())


'''Instead of letting pandas guess, we can set the data type of any or all columns with read CSV's dtype keyword argnt. 
Dtype takes a dictionary, where each key is a column name and each value is the data type that column should be.'''
tax_data = pd.read_csv('InputData/VTtaxdata16.csv', dtype={"zipcode": str})
print(tax_data.dtypes)


''' Identify missing data with the NA values keyword argument. NA values accepts either a single value, a list of values
or a dictionary of columns and values in that column to treat as missing'''
tax_data = pd.read_csv('InputData/VTtaxdata16.csv', na_values={"zipcode": 0})
print(tax_data[tax_data.zipcode.isna()])


'''error bad lines and warn bad lines both take Boolean, or true/false values. Setting error bad lines to False makes 
pandas skip bad lines and load the rest of the data, instead of throwing an error. Warn bad lines tells pandas whether 
to display messages when unparseable lines are skipped.'''
try:
    # Import the CSV without any keyword arguments
    tax_data = pd.read_csv('InputData/VTtaxdata16.csv')

    # View first 5 records
    print(tax_data.head())

except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")

