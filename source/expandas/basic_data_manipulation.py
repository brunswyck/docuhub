import Toolkit

np = Toolkit.initiate_numpy()
pd = Toolkit.initiate_pandas(max_cols=20)

"""labeling & ordering"""
# https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
airbnb_data = "files/csv/AB_NYC_2019.csv"
df = pd.read_csv(airbnb_data)
df2 = df.set_index("id")
print(df2.head(3))
print("--------------")
print(df2.name)
print("--------------")
print(df2.name[5022])

df3 = df.groupby("room_type").mean()  # index becomes the room_type
print(type(df3))
print(df3.index)  # Index(['Entire home/apt', 'Private room', 'Shared room'], dtype='object', name='room_type')
df_workaround = df.groupby("room_type", as_index=False).mean()  # don't set as id
# print(df_workaround)
df3 = df3.reset_index()
print(df3)
""" After setting an index use sort!! = better performance"""
df3.sort_index()
df.sort_values("host_name")
print(df.sort_values("host_name").head())
print(df.sort_values(["neighbourhood_group", "host_name"], ascending=[False, True]).head())

print(df.neighbourhood_group.unique())  # ['Brooklyn' 'Manhattan' 'Queens' 'Staten Island' 'Bronx']
print(df.neighbourhood_group.value_counts())

""" Rank - what to do when you have equal values in a column - aka sorting with collision detection """
df_price = df.sort_values("price", ascending=False)
print(df_price[["id", "host_name", "price"]].head(5))

print("----- rank ----")
df_price["price_rank"] = df_price.price.rank(method="average", ascending=False)  # rank based on avg
print(df_price[["id", "host_name", "price", "price_rank"]].head(5))

"""slicing & filtering"""
# slicing columns
print(df["host_name"])
print(df.host_name)
# multiple columns
print(df[["host_name", "neighbourhood_group"]])

# filtering on rows (mask filtering)
print((df["host_name"] == "Taz").sum())  # 6
mask = df.host_name == "Taz"
print(df[mask].head(2))

quick_and_cheap = (df.price < 100) & (df.minimum_nights < 3)
print(quick_and_cheap.sum())  # 12129
print(df[quick_and_cheap])

reviews_consistent = df[(df.reviews_per_month > 3) | (df.number_of_reviews > 50)]
print(reviews_consistent.head())
# not that you should but you can do it with numpy too
mask = np.logical_or((df.reviews_per_month > 3), (df.number_of_reviews > 50))
print(df[mask].head())
# logical inversion (will now contain inconsistent reviews)
df[~mask].head()

"""filtering columns & rows together with loc"""
# eg give me just the name of app with consistent reviews
print(df.loc[mask, ["name", "host_name"]])
# use colon ':' if you want everything
print(df.loc[:, ["name", "host_name"]])  # all rows
print(df.loc[mask, :].head())  # all columns for consistent reviews

"""filtering based on index with iloc (internal array index)"""
# just row 0 & all the columns
print(df.iloc[0, :])  # all columns row 1
print(df.iloc[0, 1])  # Clean & quiet apt home by the park
print(df.iloc[1:4, 6:])  # all columns row 1 - 3, all cols starting with 6th col

"""provided mask helpers"""
# between
print(df.loc[df.price.between(100, 200), "price"].head())
# isin
print(df.loc[df.price.isin([100, 200]), "price"].head())  # is price 100 or 200
# you can apply mask on entire df not just column
print(df == "John")
print((df == "John").any())  # any column that contains "john"
# now get rows! by changing default axis
print((df == "John").any(axis=1))  # any column that contains "john"

"""views vs copy"""
# a common pitfall is to not understand this difference between views & copies
df_copy = df.copy()
df_copy["name"][0] = "TESTING"
print(df_copy.head(1))
# SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
df_copy.loc[
    df_copy.index == 0, "name"] = "TESTING2"  # no warning -> loc returns a view & directly affects underlying df
print(df_copy.head(1))
df_copy[df_copy.host_name == "John"][
    "name"] = "oh no"  # name is not updated! -> you are not affecting original df but a copy
print(df_copy.head(1))

"""replacing & tresholding"""
# dealing with NaN's -> # get rid of em or put in sensible values

# you can see that cols with non-null rows have different counts
print(df.info())
print(df.dropna().info())  # gives you how many rows you would have when no NaN values
# you can say only drop it when a row has at least 3 NaN's in it
print(df.dropna(thresh=3).info())
# only drop events that have "last_review" = Nan
print(df.dropna(subset=["last_review"]).info())  # by default we operate on row by row basis
print(df.dropna(axis=1).info())  # you now dropped the entire review column cuz it had a NaN in it :)
# df.fillna(0)
# if eg you have number_of_items = 0 -> you want total_purchased to be 0 instead of NaN
""" df.fillna(0) # replaces every nan with a 0"""
# for time-series data you can use method like backfill forwardfill (eg fill with previous finite value)

# generic replace

df.replace("John", "Jono").head(1)  # on every row and every column by default
df.replace("John", "Jono", limit=1)  # John is on 1st row, set a replacement limit
df.host_name.replace({"John": "Jono", "James": "Jamey"})  # on every row and every column by default

# thresholding - eg enforce a min/max value to keep outliers out of a plot
import matplotlib.pyplot as plt

# plt.hist(df.price, log=True)
plt.hist(df.price.clip(upper=1000))
df_copy.loc[df_copy.price > 1000, "price"] = 1000  # identical to .clip(upper=1000)
# plt.hist(df_copy.price)
# plt.show()  # todo: remove # if you want to see plot


"""removing & adding data"""
astro_df = pd.read_csv("files/csv/astronauts.csv")
astro_df.head(10)
# timeseries
# modify column type (BirthDate is a timeseries read as string right now)
birthdate = pd.to_datetime(astro_df["Birth Date"], format="%m/%d/%Y")
print(birthdate)  # Name: Birth Date, Length: 357, dtype: datetime64[ns]
# now we can work with it (no need to manipulate strings), eg use year
print(birthdate.dt.year)
zarya = pd.to_datetime("1998-11-20")  # 1st module ISS
# how old were astronauts when zarya was deployed?
astro_df["age_at_zarya"] = (zarya - birthdate).astype(
    'timedelta64[Y]')  # zarya - birthdate = seconds, now turned into years
print(astro_df)
astro_df["birth"] = birthdate
print(astro_df.head(3))

# categoricals
# info can be used by other libraries, provide explicit sorting order to improve speed on group categories
# eg no use sorting military rank alphabetically
print(astro_df["Military Rank"].unique())
# [nan 'Colonel' 'Lieutenant Colonel' 'Captain' 'Major General' 'Commander' 'Lieutenant Commander' 'Brigadier General' 'Major' 'Lieutenant General' 'Chief Warrant Officer' 'Rear Admiral' 'Vice Admiral']
print(astro_df["Military Rank"].dtype)  # object
# turn military into a categorical with "category"
astro_df["Military Rank"].astype("category")
astro_df["Military Rank"] = astro_df["Military Rank"].astype("category")  # overwrite orginal mil rank
print(astro_df["Military Rank"].dtype)  # category -> no longer a generic object

# numeric/string conversion
print(astro_df.head())
# always convert a string to float first b4 converting to an int
print(astro_df.age_at_zarya.astype("str").astype("float").astype("int"))  # first astype("str") for demo only

# removing cols or rows
df4 = astro_df[["Name", "Year", "Group"]].copy()
print(df4.head())
print(df4.drop("Group", axis=1).head())
# if you want to drop a row instead, change label to a #
print(df4.drop(1).head())
# instead of axis 1 you can solve it syntactically too
df5 = astro_df.copy(deep=True)
print(df5.drop(columns=["Group", "Undergraduate Major"]).head())

# adding rows
df4.append({"Name": "Senor Gringo", "Year": 2011, "Group": 20.0}, ignore_index=True)
print(df4)
df_sis = pd.DataFrame({"Name": ["El Gringo"], "Year": [2010], "Group": [20.0]})
print(df_sis)
# glue two dataframes together with append
df4.append(df_sis, ignore_index=True)

# adding columns
df4["Extra Column"] = "default"  # set value for all rows in col
print(df4)
# add col using assing
print(df4.assign(new_col="hello"))  # you can just use [] to add more
df4.insert(0, "Firstname",
           df5.Name.str.split(" ", 1, expand=True)[0])  # expand out to a dataframe so we can access 1st column
print(df4)

# transposing data: cols/rows -> rows/cols
# set index to name on copy
df11 = df4.set_index("Name")
print(df11.head(2))
"""
                Firstname    Year  Group Extra Column
Name                                                 
Joseph M. Acaba    Joseph  2004.0   19.0      default
Loren W. Acton      Loren     NaN    NaN      default
"""
df22 = df11.transpose(copy=True)  # .T
print(df22.T)

"""apply map & vectorized functions"""
"""
eg: df.apply(np.square)

Apply
Apply: It is used when you want to apply a function along the axis of a dataframe
accepts a Series whose index is either column (axis=0) or row (axis=1)
apply works on df and series too
map works on series only """

random_data = np.round(np.random.random(size=(4, 3)), 2)  # 2 decimal points
dfx = pd.DataFrame(random_data, columns=["A", "B", "C"])
print(dfx.head())
dfx.apply(lambda x: 1 + np.abs(x))  # apply needs vectorized function
print(dfx.A.apply(np.abs))  # abs makes neg number positive


# apply requires a vectorized function!
# def double_if_positive(x):
#     if x > 0:
#         return 2 * x  # x here is an array, not a single number!
#     return x

def double_if_positive(x):
    x = x.copy()  # prevents you from mutating x datasource
    x[x > 0] *= 2  # masked array  x[condition]
    return x


print(dfx.apply(double_if_positive,
                raw=True))  # raw=False -> Panda Series so 1 col at a time, raw=True fast on simple calculations
# ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
# Map
# map operates on Series & uses dictionary input not array input
series = pd.Series(["Steve", "Alex", "Jess", "Mark"])
print(series.map({"Steve": "Stephen"}))
"""
0    Stephen
1        NaN
2        NaN
3        NaN
dtype: object
"""
print(series.map(
    lambda fn: f"I am {fn}"))  # unlike apply (needs vector. function) this goes over each element 1 at a time

# Vectorized functions
# https://medium.com/codex/vectorizing-functions-in-numpy-d00dc5e58f65
# import IPython.core.display as dp
# dp.display((dfx, dfx.abs()))
sky_series = pd.Series(["Obi-Wan Kenobi", "Luke Skywalker", "Han Solo", "Leia Organa"])
print("Luke Skywalker".split())  # ['Luke', 'Skywalker']
# sky_series.split()  # series objes has no attr split, you have to str first!
print(sky_series.str.split())
"""['Luke', 'Skywalker']
   0    [Obi-Wan, Kenobi]
   1    [Luke, Skywalker]
   2          [Han, Solo]
   3       [Leia, Organa]
   dtype: object"""
# TURN THIS INTO A DATAFRAME WITH EXPAND
print(sky_series.str.split(expand=True))

print(sky_series.str.contains("Skywalker"))  # True for row 1d
print(sky_series.str.upper().str.split())  # always use str on a series

# user defined functions
data2 = np.random.normal(10, 2, size=(100000, 2))
df_extra1 = pd.DataFrame(data2, columns=["x", "y"])
print(df_extra1)
hypot = (df_extra1.x ** 2 + df_extra1.y ** 2) ** 0.5
print(hypot)
# non vectorized -> takes 16 seconds
"""
def hypot_bad(x, y):
    return np.sqrt(x**2 + y**2)

h1 = []
for index, (x, y) in df_extra1.iterrows():
    h1.append(hypot_bad(x, y))

print(h1[0])
"""


# vectorized -> quick 13ms
def hypot_good(row_of_xs, row_of_ys):  # feed it with rows of data not element by element
    return np.sqrt(row_of_xs ** 2 + row_of_ys ** 2)


h2 = hypot_good(df_extra1.x, df_extra1.y)
print(h2[0])
