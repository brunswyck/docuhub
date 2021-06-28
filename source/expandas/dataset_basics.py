import Toolkit
import tables
"""kaggle | drivedata | crowdanalytix | innocentive | codalab | crowdai | datahack - sql
numpy.loadtxt
numpy.genfromtxt
pandas.read_csv
pandas.read_pickle
"""


pd = Toolkit.initiate_pandas()
np = Toolkit.initiate_numpy()

""" creating dataframes"""
data = np.random.random(size=(5, 5))
print(data)

df = pd.DataFrame(data=data, columns=["A", "B", "C", "D", "E"])  # use this
print(df)

dtype = [('A', int), ("B", (str, 20))]
data = np.array([(1, "Sam"), (2, "Alex"), (3, "James")], dtype=dtype)
print(data)  # [(1, 'Sam') (2, 'Alex') (3, 'James')]
df = pd.DataFrame(data)
print(df)

data = {"A": [1, 2, 3], "B": ["Sam", "Alex", "James"]}  # and use this
df = pd.DataFrame(data)
print(df)

data = [{"A": 1, "B": "Sam"}, {"A": 2, "B": "Alex"},{"A": 3, "B": "James"}]  # too messy
df = pd.DataFrame(data)
print(df)
"""
   A      B
0  1    Sam
1  2   Alex
2  3  James
"""

""" saving & serializing"""
random_data = np.random.random(size=(100000, 4))
columns = ["A", "B", "C", "D"]
df = pd.DataFrame(data=random_data, columns=columns)
print(df.head())
df.to_csv("files/csv/save.csv", index=False, float_format="%0.4f")

# pickle = much faster
df.to_pickle("files/pkl/save.pkl")
# conda install pytables
# https://anaconda.org/conda-forge/pytables
df.to_hdf("files/hdf/save.hdf", key="data", format="table")

astronaut_csv = "files/csv/astronauts.csv"
df = pd.read_csv(astronaut_csv)
print(df.head())
df.to_csv("files/csv/astronauts.csv", index=False, float_format="%0.4f")

""" inspecting data"""
df.tail(4)
df.sample(3) # random rows
df.info()
df.describe() # useful for troubleshooting your data with quick glance over
df.shape # [5 rows x 19 columns]
df.corr()  # correlations between columns
print(df["Year"].value_counts())
df.max()  # get max for every column

