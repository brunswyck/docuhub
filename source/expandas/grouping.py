import Toolkit
import matplotlib

np = Toolkit.initiate_numpy()
pd = Toolkit.initiate_pandas(max_cols=20)
import matplotlib.pyplot as plt

df = pd.read_csv("files/csv/train.csv", low_memory=False, parse_dates=["Date"])  # allow load all in to determine dtype
print(df.head(5))
# doublecheck dtypes with df.info()
print(df.info())
# dates is still just dtype object:  2   Date           1017209 non-null  object
# fix with parse_dates=["Date"]

# https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
dfg = df.groupby("Store")
# print(dfg.mean())
# put store back into the dataframe with reset_index()
print(dfg.mean().reset_index())
store_avg = dfg.mean()
store_avg = store_avg.reset_index()
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
plt.style.use('dark_background')
store_avg.plot.scatter("Store", "Sales", s=3, title="avg sale/store")  # s = point size
# plt.show()
plt.clf()  # clear current figure
# Multiple groups
# group in multiple categories
store_day = df.groupby(["Store", "DayOfWeek"], as_index=False).mean()  # instead of reset_index -> as_index=False
print(store_day.head())
# print(store_day.Store.unique())
for store in df.Store.unique()[:5]:
    df_tmp = store_day[store_day.Store == store]
    plt.plot(df_tmp.DayOfWeek, df_tmp.Sales, label=f"Store {store}")
plt.xlabel("Day of Week")
plt.ylabel("Avg Sales")
plt.legend()
# plt.show()
plt.clf()

# continuous grouping
# eg cut sales made
print(df.groupby("Sales").mean().shape)  # (21734, 6)
print(df.Sales.describe())  # check up to where your sales go to know where you should cut
"""
count    1.017209e+06
mean     5.773819e+03
std      3.849926e+03
min      0.000000e+00
25%      3.727000e+03
50%      5.744000e+03
75%      7.856000e+03
max      4.155100e+04
Name: Sales, dtype: float64
"""
bins = [0, 2000, 4000, 6000, 8000, 10000, 50000]
cuts = pd.cut(df.Sales, bins,
              include_lowest=True)  # cut is not attached to the dataframe itself.. , include sales with 0!
# add cuts back into original dataframe
df["SalesGroup"] = cuts
print(df.head())
print(df.groupby(["Store", "SalesGroup"]).DayOfWeek.value_counts())
print(
    df.groupby(["Store", "SalesGroup"]).DayOfWeek.value_counts().unstack(fill_value=0))  # fill_value=0 (instead of NaN)
"""
DayOfWeek                  1   2   3   4   5    6    7
Store SalesGroup                                      
1     (-0.001, 2000.0]     6   1   3  11   6    0  134
      (2000.0, 4000.0]    28  42  42  43  28   13    0
      (4000.0, 6000.0]    70  80  83  72  91  109    0
      (6000.0, 8000.0]    26  12   7   9   9   10    0
      (8000.0, 10000.0]    4   0   0   0   1    2    0
...                       ..  ..  ..  ..  ..  ...  ...
1115  (2000.0, 4000.0]    15  17  15   9   0    0    0
      (4000.0, 6000.0]    34  54  65  64  61   36    0
      (6000.0, 8000.0]    30  52  39  39  50   80    0
      (8000.0, 10000.0]   37   9  12  10  11   16    0
      (10000.0, 50000.0]  12   2   1   2   7    2    0

[6263 rows x 7 columns]
"""
print(df.groupby(["Store", "SalesGroup", "DayOfWeek"]).count())
"""
                                    Date  Sales  Customers  Open  Promo  StateHoliday  SchoolHoliday
Store SalesGroup         DayOfWeek                                                                  
1     (-0.001, 2000.0]   1             6      6          6     6      6             6              6
                         2             1      1          1     1      1             1              1
                         3             3      3          3     3      3             3              3
                         4            11     11         11    11     11            11             11
                         5             6      6          6     6      6             6              6
...                                  ...    ...        ...   ...    ...           ...            ...
1115  (10000.0, 50000.0] 3             1      1          1     1      1             1              1
                         4             2      2          2     2      2             2              2
                         5             7      7          7     7      7             7              7
                         6             2      2          2     2      2             2              2
                         7             0      0          0     0      0             0              0

[46830 rows x 7 columns]
"""
# Imputation
# filling in missing/corrupt values in your dataframe. it shouldn't affect your final result
dfo = pd.read_csv("files/csv/train.csv", low_memory=False, parse_dates=["Date"])  # allow load all in to determine dtype
print(dfo.head(5))
# plt.hist(df.Sales)
# plt.show()
df = dfo[dfo.Open == 1].copy()  # masked array with stores that are open (removing sunday closed outlier)
# plt.hist(df.Sales)
print(df.shape)  # checking row count

# transform -> like apply but has to return a series with same size as the input
# https://stackoverflow.com/questions/27517425/apply-vs-transform-on-a-group-object
# instead of NaN fill with mean value of the series
test_fix = df.Sales.transform(lambda x: x.fillna(x.mean()))
# sales are heavily dependant on day of the week, so use that intelligence with groupby cuts


# different aggregates for different columns
# aggregate statistics functions can be used to calc stats on a column of a DataFrame Eg df.columnName.mean()
# aggregate statistic functions can be applied across multiple rows by using a groupby function
# give the mean for the Sales & Customers column
print(
    df.groupby(["Store", "DayOfWeek", ]).agg({"Sales": "mean", "Customers": np.mean}))  # str for common funcs works too

# do multiple things with 1 column (pass multiple things through a list)
print(df.groupby(["Store", "DayOfWeek", ]).agg({"Sales": ["mean", "max", "min"], "Customers": "count"}))
"""
                       Sales              Customers
                        mean    max   min     count
Store DayOfWeek                                    
1     1          5177.968750   9528  3414       128
      2          4685.626866   7959  2362       134
      3          4555.712121   7821  2605       132
      4          4457.838710   7785  2462       124
      5          4726.480620   8414  3198       129
"""
monte_carlo_uncertainty = lambda x: np.std(x) / np.sqrt(x.size)
df2 = df.groupby(["Store", "DayOfWeek", ]).agg({"Sales": ["mean", monte_carlo_uncertainty], "Customers": "count"})
print(df2)
"""
            Sales             Customers
                        mean  <lambda_0>     count
Store DayOfWeek                                   
1     1          5177.968750  108.777349       128
      2          4685.626866   88.507530       134
"""
# override column names by using a tuple
df2 = df.groupby(["Store", "DayOfWeek", ]).agg({"Sales":
                                                    [("SalesMean", "mean"),
                                                     ("SalesUncert", monte_carlo_uncertainty)],
                                                "Customers": "count"})
print(df2.head())
# notice the nested multi-column layout
"""
             Sales             Customers
                   SalesMean SalesUncert     count
Store DayOfWeek                                   
1     1          5177.968750  108.777349       128
      2          4685.626866   88.507530       134
      3          4555.712121   79.957721       132
"""


# new way of using aggregates (recommended) won't work with lambda as all functions need to have a name
# => only 1 layer of columns
def mc_uncert(x):
    return np.std(x) / np.sqrt(x.size)

dfagg = df.groupby(["Store", "DayOfWeek"])
print(dfagg.agg(
    SalesMean=("Sales", "mean"),
    SalesUncert=("Sales", mc_uncert)
).reset_index().head())
"""
   Store  DayOfWeek    SalesMean  SalesUncert
0      1          1  5177.968750   108.777349
1      1          2  4685.626866    88.507530
2      1          3  4555.712121    79.957721
3      1          4  4457.838710    82.332880
4      1          5  4726.480620    80.066588
"""