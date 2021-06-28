******
pandas
******

links
=====

* http://pandas.pydata.org/pandas-docs/stable/10min.html
* https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
* http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
* https://www.dataquest.io/blog/pandas-python-tutorial/
* https://www.w3resource.com/python-exercises/pandas/index.php
* https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y
* https://www.machinelearningplus.com/python/101-pandas-exercises-python/
* https://www.kaggle.com/python10pm/pandas-75-exercises-with-solutions

resources
=========

* http://pandas.pydata.org/pandas-docs/stable/10min.html
* https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
* http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
* https://www.dataquest.io/blog/pandas-python-tutorial/
* https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y
* read csv file: https://www.youtube.com/watch?v=vmEHCJofslg

files
=====

.. only:: builder_html or readthedocs

   download csv :download:`here <files/csv/pandas_tut_read.csv>`

csv schema
==========

add a schema to csv
-------------------

.. code-block:: python

   df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
   schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

.. code-block:: python

   chipo = pd.read_csv('chipotle.tsv', sep='\t', header=0)
   chipo = pd.read_csv('chipotle.tsv', header=1, delimiter='\t', error_bad_lines=False)

   url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv' 
   chipo = pd.read_csv(url, sep = '\t')


access values
=============

`df.iloc[[df['value'].idxmax()]]` get row = iloc[] (use when you know row index integer)

.. list-table::
   :widths: 5 5 15 15 15 15
   :header-rows: 1

   * - 
     - ins
     - type_entity
     - entity
     - period
     - value
   * - 144
     - 62093
     - Commune
     - Saint-Nicolas
     - 01/01/2019
     - 3518.6

get max in col X
----------------

.. code-block:: python

   # get row = iloc[] (use when you know row index integer)
   df.iloc[[df['value'].idxmax()]]
   144


if max in col X show value in col Y
-----------------------------------

.. code-block:: python

   # iloc[[int 144]][select value of col 'ins']
   df.iloc[[df['value'].idxmax()]]['ins']
   """
   144    62093
   Name: ins, dtype: int64
   """
   type(df.iloc[[df['value'].idxmax()]]['ins'])
   pandas.core.series.Series

   type(df.iloc[[df['value'].idxmax()]])
   pandas.core.frame.DataFrame


.. note:: when you see data displayed in the above format, you're dealing with a pandas **series** object, not a dataframe object

label vs location
-----------------

* loc gets rows (and/or columns) with particular labels
* iloc gets rows (and/or columns) at integer locations

.. warning::

   loc = inclusive of endpoint
   iloc = exclusive of endpoint

.. code-block:: python

   s = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2]) 
   49    a
   48    b
   47    c
   0     d
   1     e
   2     f

   s.loc[0]    # value at index label 0
   'd'

   s.iloc[0]   # value at index location 0
   'a'

   s.loc[0:1]  # rows at index labels between 0 and 1 (inclusive)
   0    d
   1    e

   s.iloc[0:1] # rows at index location between 0 and 1 (exclusive)
   49    a

Here's a Series where the index contains string objects:

.. code-block::

   s2 = pd.Series(s.index, index=s.values)
   s2
   a    49
   b    48
   c    47
   d     0
   e     1
   f     2

Since loc is label-based, it can fetch the first value in the Series using s2.loc['a']. It can also slice with non-integer objects

.. code-block::

   s2.loc['c':'e']  # all rows lying between 'c' and 'e' (inclusive)
   c    47
   d     0
   e     1

for DateTime indexes, we don't need to pass the exact date/time to fetch by label

.. code-block::

   s3 = pd.Series(list('abcde'), pd.date_range('now', periods=5, freq='M'))
   s3
   2021-01-31 16:41:31.879768    a
   2021-02-28 16:41:31.879768    b
   2021-03-31 16:41:31.879768    c
   2021-04-30 16:41:31.879768    d
   2021-05-31 16:41:31.879768    e

to fetch the row's for march/april

.. code-block::

   s3.loc['2021-03':'2021-04']
   2021-03-31 17:04:30.742316    c
   2021-04-30 17:04:30.742316    d

more is better

.. code-block:: python

   df.loc['c': , :'z']  # rows 'c' and onwards AND columns up to 'z'
       x   y   z
   c  10  11  12
   d  15  16  17
   e  20  21  22
   
   df.iloc[:, 3]        # all rows, but only the column at index location 3
   a     3
   b     8
   c    13
   d    18
   e    23

how to slice rows up to & including 'c' and take the first 4 columns?

.. code-block:: python

   import numpy as np
   df = pd.DataFrame(np.arange(25).reshape(5, 5),
                         index=list('abcde'),
                         columns=['x','y','z', 8, 9])
   df
       x   y   z   8   9
   a   0   1   2   3   4
   b   5   6   7   8   9
   c  10  11  12  13  14
   d  15  16  17  18  19
   e  20  21  22  23  24

answer

.. code-block:: python

   df.iloc[:df.index.get_loc('c') + 1, :4]
       x   y   z   8
   a   0   1   2   3
   b   5   6   7   8
   c  10  11  12  13


.. note::

   get_loc() is an index method meaning "get the position of the label in this index"
   since slicing with iloc is exclusive of its endpoint
   we must add 1 to this value if we want row 'c' as well

.. code-block:: python



label-location loc
------------------

.. note:: loc() means you have to pass the **name** of row/column you want to select

.. note:: you can use boolean conditions with loc()

.. code-block:: python

   data = pd.DataFrame({'Brand' : ['Maruti', 'Hyundai', 'Tata',
                                   'Mahindra', 'Maruti', 'Hyundai',
                                   'Renault', 'Tata', 'Maruti'],
                        'Year' : [2012, 2014, 2011, 2015, 2012, 
                                  2016, 2014, 2018, 2019],
                        'Kms Driven' : [50000, 30000, 60000, 
                                        25000, 10000, 46000, 
                                        31000, 15000, 12000],
                        'City' : ['Gurgaon', 'Delhi', 'Mumbai', 
                                  'Delhi', 'Mumbai', 'Delhi', 
                                  'Mumbai','Chennai',  'Ghaziabad'],
                        'Mileage' :  [28, 27, 25, 26, 28, 
                                      29, 24, 21, 24]})

   display(data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)])
   """
     Brand  Year  Kms  Drive  City    Mileage
   0 Maruti 2012       50000  Gurgaon      28
   4 Maruti 2012       10000   Mumbai      28
   """

select range of rows
--------------------

.. note:: index includes start:stop values

.. code-block:: python

   # selecting range of rows from 2 to 5
   display(data.loc[2 : 5])

select column value with loc
----------------------------

.. code-block:: python

   df.loc[df['value'].idxmax(), 'ins']
   62093

at() when you know row & column label
-------------------------------------

at() is faster

.. code-block:: python

   df.at[df['value'].idxmax(), 'ins']
   62093

extracting rows & columns
-------------------------

the bracket indexing operator is one way to extract certain columns from a df

.. code-block:: python

   df[['entity', 'value']].head()
   """
    	entity	value
   0	Wallonie	215.0
   1	Brabant Wallon	367.9
   2	Nivelles	367.9
   3	Beauvechain	187.8
   4	Braine-l'Alleud	764.8   
   """

.. note::

   you can achieve the same result by using the loc function. loc is a very versatile function that can help you in a lot of accessing and extracting tasks


.. code-block:: python

   df.loc[:, ['entity', 'value']].head()
   """
    	entity	value
   0	Wallonie	215.0
   1	Brabant Wallon	367.9
   2	Nivelles	367.9
   3	Beauvechain	187.8
   4	Braine-l'Alleud	764.8   
   """

.. note::

   Note the difference is the return types when you use brackets and when you use double brackets

.. code-block:: python

   type(df['entity'])
   pandas.core.series.Series
   type(df[['entity']])
   pandas.core.frame.DataFrame


as seen before you can access columns through df['colname'] You can also access rows by using slicing operations

.. code-block:: python

   df[0:3]
   """
      	ins 	type_entity 	entity          period      value
   0	3000	Région          Wallonie    	01/01/2019	215.0
   1	20002	Province	    Brabant Wallon	01/01/2019	367.9
   2	25000	Arrondissement	Nivelles    	01/01/2019	367.9

   same using iloc:
   """
   df.iloc[0:3,:]


sorting
=======

.. code-block:: python

   df.sort_values('value').head()
   """
        ins     type_entity	entity              period      value
   228	84016	Commune    	Daverdisse          01/01/2019	24.5
   265	91143	Commune    	Vresse-sur-Semois   01/01/2019	25.8
   214	82038	Commune    	Sainte-Ode          01/01/2019	26.1
   229	84029	Commune    	Herbeumont          01/01/2019	27.8
   219	83031	Commune    	La Roche-en-Ardenne 01/01/2019	28.6
   """

filtering rows conditionally
============================

.. code-block:: python

   df[df['value'] > 150]
   """
        ins	type_entity	entity	period	value
   0	3000	Région	Wallonie	01/01/2019	215.0
   1	20002	Province	Brabant Wallon	01/01/2019	367.9
   2	25000	Arrondissement	Nivelles	01/01/2019	367.9
   3	25005	Commune	Beauvechain	01/01/2019	187.8
   4	25014	Commune	Braine-l'Alleud	01/01/2019	764.8
   ...	...	...	...	...	...
   277	92114	Commune	Sombreffe	01/01/2019	235.1
   278	92137	Commune	Sambreville	01/01/2019	825.7
   280	92140	Commune	Jemeppe-sur-Sambre	01/01/2019	408.5
   281	92141	Commune	La Bruyère	01/01/2019	174.9
   282	92142	Commune	Gembloux	01/01/2019	269.7
   165 rows × 5 columns
   """

.. code-block:: python

   df[(df['value'] > 150) & (df['value'] < 200)]
   """
    	ins	type_entity	entity	period	value
   3	25005	Commune	Beauvechain	01/01/2019	187.8
   8	25031	Commune	Genappe	01/01/2019	170.7
   11	25044	Commune	Ittre	01/01/2019	196.7
   12	25048	Commune	Jodoigne	01/01/2019	191.5
   16	25084	Commune	Perwez	01/01/2019	181.8
   25	25120	Commune	Orp-Jauche	01/01/2019	175.7
   29	25124	Commune	Walhain	01/01/2019	188.8
   31	51000	Arrondissement	Ath	01/01/2019	190.4
   61	53044	Commune	Jurbise	01/01/2019	178.4
   76	55085	Commune	Seneffe	01/01/2019	179.2
   84	56044	Commune	Lobbes	01/01/2019	181.1
   87	56078	Commune	Thuin	01/01/2019	191.7
   95	57062	Commune	Pecq	01/01/2019	171.9
   99	57093	Commune	Brunehaut	01/01/2019	173.5
   100	57094	Commune	Leuze-en-Hainaut	01/01/2019	186.0
   111	61000	Arrondissement	Huy	01/01/2019	171.5
   119	61039	Commune	Marchin	01/01/2019	181.4
   121	61043	Commune	Nandrin	01/01/2019	159.3
   123	61063	Commune	Verlaine	01/01/2019	173.3
   124	61068	Commune	Villers-le-Bouillet	01/01/2019	197.7
   132	62009	Commune	Aywaille	01/01/2019	155.6
   147	62100	Commune	Sprimont	01/01/2019	197.4
   182	63088	Commune	Plombières	01/01/2019	196.6
   183	63089	Commune	Thimister-Clermont	01/01/2019	199.0
   189	64025	Commune	Fexhe-le-Haut-Clocher	01/01/2019	166.3
   191	64034	Commune	Hannut	01/01/2019	191.6
   193	64056	Commune	Oreye	01/01/2019	199.8
   200	81000	Arrondissement	Arlon	01/01/2019	196.4
   205	81015	Commune	Messancy	01/01/2019	156.2
   263	91141	Commune	Yvoir	01/01/2019	160.6
   269	92035	Commune	Éghezée	01/01/2019	158.3
   271	92048	Commune	Fosses-la-Ville	01/01/2019	164.1
   281	92141	Commune	La Bruyère	01/01/2019	174.9
   """



dataframe iteration
===================

.. code-block:: python

   for index, row in df.iterrows():
       print(row)
       if index == 1:
           break
   """
   ins                  3000
   type_entity        Région
   entity           Wallonie
   period         01/01/2019
   value               215.0
   Name: 0, dtype: object
   ins                     20002
   type_entity          Province
   entity         Brabant Wallon
   period             01/01/2019
   value                   367.9
   Name: 1, dtype: object
   """


data sources
============

data sources:
 - `kaggle`_
 - `drivedata`_
 - `crowdanalytix`_
 - `innocentive`_
 - `codalab`_
 - `crowdai`_
 - sql

.. _kaggle: https://www.kaggle.com/
.. _drivedata: http://www.drivedata.io/
.. _crowdanalytix: https://www.crowdanalytix.com/
.. _innocentive: https://www.innocentive.com/
.. _codalab: https://codalab.org/
.. _crowdai: https://crowdai.com/

.. code-block:: python

   import Toolkit
   import tables

   """
   numpy.loadtxt
   numpy.genfromtxt
   pandas.read_csv
   pandas.read_pickle
   """


   pd = Toolkit.initiate_pandas()
   np = Toolkit.initiate_numpy()

summary
=======

.. code-block:: python

   DataFrame.at   # Access a single value for a row/column label pair.
   DataFrame.loc  # Access a group of rows and columns by label(s).
   DataFrame.iloc # Access a group of rows and columns by integer position

.. code-block:: python

   import numpy as np
   import pandas as pd
   
   df = pd.read_csv('pandas_tutorial_read.csv')
   
   df.head()
   df.tail()
   df.shape  # dimensions df
   
   df.columns.tolist()
   # ['ins', 'type_entity', 'entity', 'period', 'value']
   
   df.describe()

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 
     - ins
     - value
   * - count
     - 291.000000
     - 291.000000
   * - mean
     - 64080.941581
     - 319.149828
   * - std
     - 19262.087619
     - 428.431706
   * - min
     - 3000.000000
     - 24.500000
   * - 25%
     - 55019.500000
     - 79.400000
   * - 50%
     - 62096.000000
     - 186.000000
   * - 75%
     - 83020.500000
     - 323.700000
   * - max
     - 93090.000000
     - 3518.600000

.. code-block:: python

   df.max() # max accross all columns

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - ins
     - 93090
   * - type_entity
     - Région
   * - entity
     - Étalle
   * - period
     - 01/01/2019
   * - value
     - 3518.6
   * - dtype: object
     - 

.. code-block:: python

   df['value'].max()  # max 1 column
   3518.6
   
   df['value'].mean()
   319.1498281786941
   
   df['value'].idxmax() # id row index of max value
   144
   
   df['value'].value_counts() # times a value occurs in column

   """
   49.4     3
   292.3    2
   642.8    2
   30.6     2
   36.4     2
         ..
   144.8    1
   38.1     1
   144.1    1
   242.5    1
   764.8    1
   Name: value, Length: 280, dtype: int64
   """

creating dataframes
===================

.. code-block:: python

   data = np.random.random(size=(5, 5))
   print(data)
   """
   [[2.73096936e-01 6.65136576e-04 3.71069955e-01 9.37296738e-01 6.96564364e-01]
    [8.67359198e-01 9.41641736e-02 3.50042124e-01 6.20751307e-01 4.89966195e-01]
    [3.36140496e-01 5.49812902e-01 4.28645470e-01 9.15147038e-02 8.80548474e-01]
    [1.11154412e-01 9.48011218e-03 5.72797076e-01 3.04287648e-01 2.99374900e-01]
    [5.38842443e-01 9.00000326e-01 3.33998205e-01 4.07660159e-01 5.46279766e-01]]
   """

   df = pd.DataFrame(data=data, columns=["A", "B", "C", "D", "E"])  # use this
   print(df)
   """
             A         B         C         D         E
   0  0.273097  0.000665  0.371070  0.937297  0.696564
   1  0.867359  0.094164  0.350042  0.620751  0.489966
   2  0.336140  0.549813  0.428645  0.091515  0.880548
   3  0.111154  0.009480  0.572797  0.304288  0.299375
   4  0.538842  0.900000  0.333998  0.407660  0.546280
   """

   dtype = [('A', int), ("B", (str, 20))]
   data = np.array([(1, "Sam"), (2, "Alex"), (3, "James")], dtype=dtype)
   print(data)  # [(1, 'Sam') (2, 'Alex') (3, 'James')]

   df = pd.DataFrame(data)
   print(df)
   """
      A      B
   0  1    Sam
   1  2   Alex
   2  3  James
   """

   data = {"A": [1, 2, 3], "B": ["Sam", "Alex", "James"]}  # and use this
   df = pd.DataFrame(data)
   print(df)

   data = [{"A": 1, "B": "Sam"}, {"A": 2, "B": "Alex"},{"A": 3, "B": "James"}]  # too messy input
   df = pd.DataFrame(data)
   print(df)
   """
      A      B
   0  1    Sam
   1  2   Alex
   2  3  James
   """


saving & serializing
====================

save to csv
-----------

.. code-block:: python

   random_data = np.random.random(size=(100000, 4))
   columns = ["A", "B", "C", "D"]
   df = pd.DataFrame(data=random_data, columns=columns)
   print(df.head())
   """
             A         B         C         D
   0  0.545970  0.968191  0.789530  0.904513
   1  0.870854  0.032239  0.339050  0.212382
   2  0.140568  0.557831  0.333088  0.994743
   3  0.271945  0.573094  0.299130  0.497402
   4  0.306711  0.849376  0.953448  0.70213
   """
   df.to_csv("files/csv/save.csv", index=False, float_format="%0.4f")

write to csv
------------

.. code-block:: python

   firstRow = [['id', 'pred']]
   with open("result.csv", "w") as f:
       writer = csv.writer(f)
       writer.writerows(firstRow)
       writer.writerows(results)

pickle
------

.. code-block::

   # pickle = much faster
   df.to_pickle("files/pkl/save.pkl")

hdf
---

.. code-block:: python

   # conda install pytables
   # https://anaconda.org/conda-forge/pytables
   df.to_hdf("files/hdf/save.hdf", key="data", format="table")

csv
---

.. code-block:: python

   astronaut_csv = "files/csv/astronauts.csv"
   df = pd.read_csv(astronaut_csv)
   print(df.head())
   """
                  Name    Year  Group   Status Birth Date  ... Space Walks Space Walks (hr)                                           Missions Death Date Death Mission
   0   Joseph M. Acaba  2004.0   19.0   Active  5/17/1967  ...           2             13.0             STS-119 (Discovery), ISS-31/32 (Soyuz)        NaN           NaN
   1    Loren W. Acton     NaN    NaN  Retired   3/7/1936  ...           0              0.0                              STS 51-F (Challenger)        NaN           NaN
   2  James C. Adamson  1984.0   10.0  Retired   3/3/1946  ...           0              0.0               STS-28 (Columbia), STS-43 (Atlantis)        NaN           NaN
   3   Thomas D. Akers  1987.0   12.0  Retired  5/20/1951  ...           4             29.0  STS-41 (Discovery), STS-49 (Endeavor), STS-61 ...        NaN           NaN
   4       Buzz Aldrin  1963.0    3.0  Retired  1/20/1930  ...           2              8.0                               Gemini 12, Apollo 11        NaN           NaN
   
   """
   df.to_csv("files/csv/astronauts.csv", index=False, float_format="%0.4f")

inspecting data
===============

.. code-block:: python

   df.tail(4)
   df.sample(3) # random rows
   df.info()
   df.describe() # useful for troubleshooting your data with quick glance over
   df.shape # [5 rows x 19 columns]
   df.corr()  # correlations between columns
   print(df["Year"].value_counts())
   df.max()  # get max for every column


labeling & ordering
===================


.. code-block:: python

   import Toolkit

   np = Toolkit.initiate_numpy()
   pd = Toolkit.initiate_pandas(max_cols=20)

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
   

rank
----

.. code-block:: python

   """ Rank - what to do when you have equal values in a column - aka sorting with collision detection """
   df_price = df.sort_values("price", ascending=False)
   print(df_price[["id", "host_name", "price"]].head(5))
   
   df_price["price_rank"] = df_price.price.rank(method="average", ascending=False)  # rank based on avg
   print(df_price[["id", "host_name", "price", "price_rank"]].head(5))


slicing & filtering
-------------------

.. code-block:: python

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


filtering with loc
------------------

.. code-block:: python

   """filtering with loc"""
   # eg give me just the name of app with consistent reviews
   print(df.loc[mask, ["name", "host_name"]])
   # use colon ':' if you want everything
   print(df.loc[:, ["name", "host_name"]])  # all rows
   print(df.loc[mask, :].head())  # all columns for consistent reviews

filtering based on index with iloc
----------------------------------

.. code-block:: python

   # just row 0 & all the columns
   print(df.iloc[0, :])  # all columns row 1
   print(df.iloc[0, 1])  # Clean & quiet apt home by the park
   print(df.iloc[1:4, 6:])  # all columns row 1 - 3, all cols starting with 6th col

provided mask helpers
---------------------

.. code-block:: python

   # between
   print(df.loc[df.price.between(100, 200), "price"].head())
   # isin
   print(df.loc[df.price.isin([100, 200]), "price"].head())  # is price 100 or 200
   # you can apply mask on entire df not just column
   print(df == "John")
   print((df == "John").any())  # any column that contains "john"
   # now get rows! by changing default axis
   print((df == "John").any(axis=1))  # any column that contains "john"

views vs copy
-------------

.. code-block:: python

   # a common pitfall is to not understand this difference between views & copies
   df_copy = df.copy()
   df_copy["name"][0] = "TESTING"
   print(df_copy.head(1))
   # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
   # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
   df_copy.loc[df_copy.index == 0, "name"] = "TESTING2"  # no warning -> loc returns a view & directly affects underlying df
   print(df_copy.head(1))
   df_copy[df_copy.host_name == "John"][
       "name"] = "oh no"  # name is not updated! -> you are not affecting original df but a copy
   print(df_copy.head(1))
   

data cleaning
=============

isnull function will figure out if there are any missing values in the dataframe, and will then sum up the total for each column

df.isnull()
-----------

.. code-block:: python

   df.isnull().sum()
   """
   ins            0
   type_entity    0
   entity         0
   period         0
   value          0
   dtype: int64
   """

dealing with missing values
---------------------------

- **df.dropna()**: drop all or some of the rows that have missing values
- **df.fillna()**: replace the rows that have missing values with that you pass in

imputation
----------

convert string dates to Date format

.. code-block:: python

   # filling in missing/corrupt values in your dataframe. it shouldn't affect your final result
   dfo = pd.read_csv("files/csv/train.csv", low_memory=False, parse_dates=["Date"])  # allow load all in to determine dtype
   print(dfo.head(5))
   # plt.hist(df.Sales)
   # plt.show()
   df = dfo[dfo.Open == 1].copy()  # masked array with stores that are open (removing sunday closed outlier)
   # plt.hist(df.Sales)
   print(df.shape)  # checking row count

using transform
---------------

.. code-block:: python

   # transform -> like apply but has to return a series with same size as the input
   # https://stackoverflow.com/questions/27517425/apply-vs-transform-on-a-group-object
   # instead of NaN fill with mean value of the series
   test_fix = df.Sales.transform(lambda x: x.fillna(x.mean()))
   # sales are heavily dependant on day of the week, so use that intelligence with groupby cuts

replacing & tresholding
-----------------------

.. code-block:: python

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





.. code-block:: python

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


categoricals
============

.. code-block:: python

   # info can be used by other libraries, provide explicit sorting order to improve speed on group categories
   # eg no use sorting military rank alphabetically
   print(astro_df["Military Rank"].unique())
   # [nan 'Colonel' 'Lieutenant Colonel' 'Captain' 'Major General' 'Commander' 'Lieutenant Commander' 'Brigadier General' 'Major' 'Lieutenant General' 'Chief Warrant Officer' 'Rear Admiral' 'Vice Admiral']
   print(astro_df["Military Rank"].dtype)  # object
   # turn military into a categorical with "category"
   astro_df["Military Rank"].astype("category")
   astro_df["Military Rank"] = astro_df["Military Rank"].astype("category")  # overwrite orginal mil rank
   print(astro_df["Military Rank"].dtype)  # category -> no longer a generic object
   
numeric/string conversion
-------------------------

.. code-block:: python

   print(astro_df.head())
   # always convert a string to float first b4 converting to an int
   print(astro_df.age_at_zarya.astype("str").astype("float").astype("int"))  # first astype("str") for demo only
   

removing cols or rows
---------------------

.. code-block:: python

   df4 = astro_df[["Name", "Year", "Group"]].copy()
   print(df4.head())
   print(df4.drop("Group", axis=1).head())
   # if you want to drop a row instead, change label to a #
   print(df4.drop(1).head())
   # instead of axis 1 you can solve it syntactically too
   df5 = astro_df.copy(deep=True)
   print(df5.drop(columns=["Group", "Undergraduate Major"]).head())

adding rows
-----------

.. code-block:: python

   df4.append({"Name": "Senor Gringo", "Year": 2011, "Group": 20.0}, ignore_index=True)
   print(df4)
   df_sis = pd.DataFrame({"Name": ["El Gringo"], "Year": [2010], "Group": [20.0]})
   print(df_sis)
   # glue two dataframes together with append
   df4.append(df_sis, ignore_index=True)
   

adding columns
--------------

.. code-block:: python

   df4["Extra Column"] = "default"  # set value for all rows in col
   print(df4)
   # add col using assing
   print(df4.assign(new_col="hello"))  # you can just use [] to add more
   df4.insert(0, "Firstname",
              df5.Name.str.split(" ", 1, expand=True)[0])  # expand out to a dataframe so we can access 1st column
   print(df4)

transposing data
----------------

.. code-block:: python

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


apply map & vectorized functions
================================

apply
-----

.. code-block:: python

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

map
---

.. code-block:: python

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
   # unlike apply (needs vectorized function) this goes over each element 1 at a time
   print(series.map(lambda fn: f"I am {fn}"))

vectorized functions
--------------------

.. code-block:: python

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


grouping
========

groupby
-------

groupby allows you to group entries by certain attributes (eg grouping entries by ins number) and then perform operations on them

.. code-block:: python

   df.groupby('ins')['value'].mean().head()
   """
   ins
   3000     215.0
   20002    367.9
   25000    367.9
   25005    187.8
   25014    764.8
   Name: value, dtype: float64
   """

groups all the entities with the same value and finds how many times that specific entity appears on the group

.. code-block:: python

   df.groupby('value')['entity'].value_counts().head()
   """
   value  entity             
   24.5   Daverdisse             1
   25.8   Vresse-sur-Semois      1
   26.1   Sainte-Ode             1
   27.8   Herbeumont             1
   28.6   La Roche-en-Ardenne    1
   Name: entity, dtype: int64
   """

each df has a `values` attr that is useful as it displays your df in a numpy array style format

.. code-block:: python

   df.values
   """
   array([[3000, 'Région', 'Wallonie', '01/01/2019', 215.0],
          [20002, 'Province', 'Brabant Wallon', '01/01/2019', 367.9],
          [25000, 'Arrondissement', 'Nivelles', '01/01/2019', 367.9],
          ...,
          [93056, 'Commune', 'Philippeville', '01/01/2019', 59.0],
          [93088, 'Commune', 'Walcourt', '01/01/2019', 149.1],
          [93090, 'Commune', 'Viroinval', '01/01/2019', 46.7]], dtype=object)
   """


now, you can simply just access elements like you would in an array

.. code-block:: python

   df.values[0][0]
   3000

.. code-block:: python

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

multiple groups
---------------

.. code-block:: python

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

continuous grouping
-------------------

.. code-block:: python

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

imputation
----------

.. code-block:: python

   # filling in missing/corrupt values in your dataframe. it shouldn't affect your final result
   dfo = pd.read_csv("files/csv/train.csv", low_memory=False, parse_dates=["Date"])  # allow load all in to determine dtype
   print(dfo.head(5))
   # plt.hist(df.Sales)
   # plt.show()
   df = dfo[dfo.Open == 1].copy()  # masked array with stores that are open (removing sunday closed outlier)
   # plt.hist(df.Sales)
   print(df.shape)  # checking row count

transform
---------

transform -> like apply but has to return a series with same size as the input
https://stackoverflow.com/questions/27517425/apply-vs-transform-on-a-group-object

.. code-block:: python

   # instead of NaN fill with mean value of the series
   test_fix = df.Sales.transform(lambda x: x.fillna(x.mean()))
   # sales are heavily dependant on day of the week, so use that intelligence with groupby cuts

aggregate
---------

.. code-block:: python

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

override column names using a tuple
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

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

merging
=======

db-style  joining/merging
-------------------------

.. code-block:: python

   pd.merge(
       left,
       right,
       how="inner",
       on=None,
       left_on=None,
       right_on=None,
       left_index=False,
       right_index=False,
       sort=True,
       suffixes=("_x", "_y"),
       copy=True,
       indicator=False,
       validate=None,
   )


- **left**: A DataFrame or named Series object
- **right**: Another DataFrame or named Series object
- **on**: Column or index level names to join on. Must be found in both the left and right DataFrame and/or Series objects. If not passed and left_index and right_index are False, the intersection of the columns in the DataFrames and/or Series will be inferred to be the join keys
- **left_on**: Columns or index levels from the left DataFrame or Series to use as keys. Can either be column names, index level names, or arrays with length equal to the length of the DataFrame or Series
- **right_on**: Columns or index levels from the right DataFrame or Series to use as keys. Can either be column names, index level names, or arrays with length equal to the length of the DataFrame or Series
- **left_index**: If True, use the index (row labels) from the left DataFrame or Series as its join key(s). In the case of a DataFrame or Series with a MultiIndex (hierarchical), the number of levels must match the number of join keys from the right DataFrame or Series
- **right_index**: Same usage as left_index for the right DataFrame or Series
- **how**: One of 'left', 'right', 'outer', 'inner'. Defaults to inner. See below for more detailed description of each method
- **sort**: Sort the result DataFrame by the join keys in lexicographical order. Defaults to True, setting to False will improve performance substantially in many cases
- **suffixes**: A tuple of string suffixes to apply to overlapping columns. Defaults to ('_x', '_y')
- **copy**: Always copy data (default True) from the passed DataFrame or named Series objects, even when reindexing is not necessary. Cannot be avoided in many cases but may improve performance / memory usage. The cases where copying can be avoided are somewhat pathological but this option is provided nonetheless
- **indicator**: Add a column to the output DataFrame called _merge with information on the source of each row. _merge is Categorical-type and takes on a value of left_only for observations whose merge key only appears in 'left' DataFrame or Series, right_only for observations whose merge key only appears in 'right' DataFrame or Series, and both if the observation’s merge key is found in both
- **validate**: string, default None. If specified, checks if merge is of specified type

    - **one_to_one** or **1:1**: checks if merge keys are unique in both left and right datasets
    - **one_to_many** or **1:m**: checks if merge keys are unique in left dataset
    - **many_to_one** or **m:1**: checks if merge keys are unique in right dataset
    - **many_to_many** or **m:m**: allowed, but does not result in checks

merge methods
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - merge method 
     - SQL Join Name
     - description

   * - left
     - LEFT OUTER JOIN
     - use keys from left frame only

   * - right
     - RIGHT OUTER JOIN
     - use keys from right frame only

   * - outer
     - FULL OUTER JOIN
     - use union of keys from both frames

   * - inner
     - INNER JOIN
     - use intersection of keys from both frames

checking for duplicate keys
---------------------------

Users can use the **validate** argument to automatically check whether there are unexpected duplicates in their merge keys. Key uniqueness is checked before merge operations and so should protect against memory overflows. Checking key uniqueness is also a good way to ensure user data structures are as expected

.. code-block:: python

   left = pd.DataFrame({"A": [1, 2], "B": [1, 2]})
   right = pd.DataFrame({"A": [4, 5, 6], "B": [2, 2, 2]})
   result = pd.merge(left, right, on="B", how="outer", validate="one_to_one")
   # MergeError: Merge keys are not unique in right dataset; not a one-to-one merge

If the user is aware of the duplicates in the right DataFrame but wants to ensure there are no duplicates in the left DataFrame, one can use the **validate='one_to_many'** argument instead, which will not raise an exception

.. code-block:: python

   pd.merge(left, right, on="B", how="outer", validate="one_to_many")
   """
      A_x  B  A_y
   0    1  1  NaN
   1    2  2  4.0
   2    2  2  5.0
   3    2  2  6.0
   """

The merge indicator
-------------------

merge() accepts the argument **indicator**. If True, a Categorical-type column called _merge will be added to the output object that takes on values:

.. code-block:: python

   df1 = pd.DataFrame({"col1": [0, 1], "col_left": ["a", "b"]})
   df2 = pd.DataFrame({"col1": [1, 2, 2], "col_right": [2, 2, 2]})
   pd.merge(df1, df2, on="col1", how="outer", indicator=True)
   """
      col1 col_left  col_right      _merge
   0     0        a        NaN   left_only
   1     1        b        2.0        both
   2     2      NaN        2.0  right_only
   3     2      NaN        2.0  right_only
   """

The indicator argument will also accept string arguments, in which case the indicator function will use the value of the passed string as the name for the indicator column

joins
-----

.. code-block:: python

   import Toolkit
   # https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#
   pd.merge(
       df_left,
       df_right,
       how="inner",
       on=None,
       left_on=None,
       right_on=None,
       left_index=False,
       right_index=False,
       sort=True,
       suffixes=("_x", "_y"),
       copy=True,
       indicator=False,
       validate=None,
   )
   
   pd = Toolkit.initiate_pandas()
   
   students = pd.read_csv("students.csv")
   teachers =  pd.read_csv("teachers.csv")
   grades1 = pd.read_csv("grades1.csv")
   grades2 = pd.read_csv("grades2.csv")
   contacts = pd.read_csv("contacts.csv")
   grades = pd.concat([grades1, grades2])
   
   # add semesters
   grades1["Semester"] = 1
   grades2["Semester"] = 2
   grades1.copy().append(grades2)
   # fix duplicate indexes
   grades = grades.reset_index(drop=True)  # if you don't want to see old index, drop it
   
   # merging horizontally
   # grades have student_id, students have id
   student_grades = pd.merge(students, grades, left_on="id", right_on="student_id")
   # verify with shape that no rows are missing after merge
   print(students.shape, grades.shape, student_grades.shape)
   # alternatively you could rename column in students before merging
   students2 = students.rename({"id": "student_id"}, axis=1)
   students_full = students2.merge(contacts, on="student_id")
   student_grades = pd.merge(students2, grades, on="student_id")
   
   df = pd.merge(student_grades, contacts, on="student_id")
   df = df.merge(teachers, on="course")
   
   df2 = df.loc[df.grade == "F", "student_id"]
   method1 = df2.value_counts().rename_axis("student_id").reset_index(name="counts")  # name col & counts column
   
   method2 = df.loc[df.grade == "F", ["student_id", "grade"]].groupby("student_id").count().reset_index()
   print(method2)
   method2.columns = ["student_id", "counts"]  # change grade to counts colname
   # students failing a high number of classes
   students_failing_alot = method1[method1.counts >= 3].student_id
   print(students_failing_alot.head())
   final = students_full[students_full.student_id.isin(students_failing_alot)]
   
   # join, more sql like
   pd.display(students.head(), contacts.head())
   students2 = students.set_index("id")
   contacts2 = contacts.set_index("student_id")
   # directly joining on index
   students2.join(contacts2)
   
   # inner left & outer merging
   
   df_s = pd.read_csv("students.csv")
   df_p = pd.read_csv("contacts.csv")
   df_g = pd.read_csv("grades1.csv")
   df_design = df_g[df_g.course == "DESN101"]
   print(df_design.shape, df_s.shape)  # (12, 3) (25, 3)  only 12/25 took design 101 course
   pd.merge(df_s, df_design, left_on="id", right_on="student_id")  # will have exactly 12 rows
   pd.merge(df_s, df_design, left_on="id", right_on="student_id", how="inner")  # will have exactly 12 rows
   
   # if not in "DESN101" class then put in NaN value for "course" column
   # don't remove things if they don't exist on the right, fill with NaN
   # how="left" => left join => KEEP EVERYTHING ON THE LEFT
   pd.merge(df_s, df_design, left_on="id", right_on="student_id", how="left")
   # how="inner" => HAS TO EXIST ON LEFT & RIGHT SIDE
   
   # outer => DOESN't have to exist on either side
   # outer demo
   df_a = pd.DataFrame({"A": ["x", "y", "z"], "B": [1, 2, 3]})
   df_b = pd.DataFrame({"A": ["u", "v", "x"], "B": [5.0, 4.0, 3.0]})
   
   pd.display(df_a, df_b)

.. code-block:: python

   # outer join
   df_a = pd.DataFrame({"A": ["x", "y", "z"], "B": [1, 2, 3]})
   df_b = pd.DataFrame({"A": ["u", "v", "x"], "C": [5.0, 4.0, 3.0]})
   
   print(df_a, "\n", df_b)
   print(pd.merge(df_a, df_b, how="inner", on='A'))
   """
      A  B    C
   0  x  1  3.0
   """
   print(pd.merge(df_a, df_b, how="outer", on='A'))
   """
      A    B    C
   0  x  1.0  3.0
   1  y  2.0  NaN
   2  z  3.0  NaN
   3  u  NaN  5.0
   4  v  NaN  4.0
   """

.. code-block:: python

   # duplicate keys
   
   df_c = pd.DataFrame({"A": ["x", "x", "z"], "B": [1, 2, 3]})
   df_d = pd.DataFrame({"A": ["u", "x", "x"], "C": [5.0, 4.0, 3.0]})
   
   print(df_c)
   print(df_d)
   print(pd.merge(df_c, df_d, on='A'))
   """
      A  B    C
   0  x  1  4.0   x1 * x4.0
   1  x  1  3.0   x2 * x3.0
   2  x  2  4.0   dito
   3  x  2  3.0   dito
   """
   
   # duplicate columns
   df_e = pd.DataFrame({"A": ["x", "y", "z"], "B": [1, 2, 3]})
   df_f = pd.DataFrame({"A": ["u", "v", "x"], "B": [5.0, 4.0, 3.0]})
   print(pd.merge(df_e, df_f, on="A"))
   """
      A  B_x  B_y
   0  x    1  3.0
   """
   df_m = pd.merge(df_e, df_f, on="A", suffixes=("_left", "_right"))
   """
      A  B_left  B_right
   0  x       1      3.0
   """
   print(df_m.rename(columns={"B_left": "Hello", "B_right": "Obi_wan_kenobi"}))
   """
      A  Hello  Obi_wan_kenobi
   0  x      1             3.0
   """
   # validating
   # pd.merge(df_s, df_p, left_on="id", right_on="student_id", validate="one_to_one")
   
   
   # composite keys
   df_1 = pd.DataFrame({"year": [2000, 2000, 2001, 2001], "sem": [1, 2, 1, 2], "fee": [200, 200, 200, 200]})
   df_2 = pd.DataFrame({"year": [2000, 2000, 2001, 2001], "sem": [1, 2, 1, 2],
                        "student": [1, 2, 2, 3], "discount": [0.1, 0.2, 0.2, 1.0]})
   df_3 = pd.DataFrame({"student": [1, 2, 3, 4, 5]})
   
   print(df_1)
   print(df_2)
   print(df_3)
   """
      year  sem  fee
   0  2000    1  200
   1  2000    2  200
   2  2001    1  200
   3  2001    2  200
      year  sem  student  discount
   0  2000    1        1       0.1
   1  2000    2        2       0.2
   2  2001    1        2       0.2
   3  2001    2        3       1.0
      student
   0        1
   1        2
   2        3
   3        4
   4        5
   """
   combined = pd.merge(df_1, df_2, on=["year", "sem"])
   print(combined)
   """
      year  sem  fee  student  discount
   0  2000    1  200        1       0.1
   1  2000    2  200        2       0.2
   2  2001    1  200        2       0.2
   3  2001    2  200        3       1.0
   """
   combined["due_fee"] = combined.fee * (1 - combined.discount)
   print(combined)
   """
      year  sem  fee  student  discount  due_fee
   0  2000    1  200        1       0.1    180.0
   1  2000    2  200        2       0.2    160.0
   2  2001    1  200        2       0.2    160.0
   3  2001    2  200        3       1.0      0.0
   """
   # after merging we don't need key column (axis=1) anymore
   print(pd.merge(df_3, df_2, on="student", how="left"))
   """
      student    year  sem  discount
   0        1  2000.0  1.0       0.1
   1        2  2000.0  2.0       0.2
   2        2  2001.0  1.0       0.2
   3        3  2001.0  2.0       1.0
   4        4     NaN  NaN       NaN
   5        5     NaN  NaN       NaN
   """
   # cross join aka cartesian product
   df_1["key"], df_3["key"] = 1, 1
   df_cross = pd.merge(df_1, df_3, on="key").drop("key", axis=1)
   print(df_cross)
   """
       year  sem  fee  student
   0   2000    1  200        1
   1   2000    1  200        2
   2   2000    1  200        3
   3   2000    1  200        4
   4   2000    1  200        5
   ..   ...  ...  ...      ...
   15  2001    2  200        1
   16  2001    2  200        2
   17  2001    2  200        3
   18  2001    2  200        4
   19  2001    2  200        5
   """
   all_fees = pd.merge(df_cross, df_2, on=["student", "year", "sem"], how="left")
   print(all_fees)
   """
       year  sem  fee  student  discount
   0   2000    1  200        1       0.1
   1   2000    1  200        2       NaN
   2   2000    1  200        3       NaN
   3   2000    1  200        4       NaN
   4   2000    1  200        5       NaN
   ..   ...  ...  ...      ...       ...
   15  2001    2  200        1       NaN
   16  2001    2  200        2       NaN
   17  2001    2  200        3       1.0
   18  2001    2  200        4       NaN
   19  2001    2  200        5       NaN
   """
   all_fees.discount.fillna(0, inplace=True)
   all_fees["due"] = all_fees.fee * (1 - all_fees.discount)
   print(all_fees)
   """
       year  sem  fee  student  discount    due
   0   2000    1  200        1       0.1  180.0
   1   2000    1  200        2       0.0  200.0
   2   2000    1  200        3       0.0  200.0
   3   2000    1  200        4       0.0  200.0
   4   2000    1  200        5       0.0  200.0
   ..   ...  ...  ...      ...       ...    ...
   15  2001    2  200        1       0.0  200.0
   16  2001    2  200        2       0.0  200.0
   17  2001    2  200        3       1.0    0.0
   18  2001    2  200        4       0.0  200.0
   19  2001    2  200        5       0.0  200.0
   """

merge helper functions
----------------------
pd.merge_ordered
^^^^^^^^^^^^^^^^

.. code-block:: python

   # ffill = forward fill (take previous value if NaN)
   pd.merge_ordered(df_be, df_nl, on="date", suffixes=("_be", "_nl"), fill_method="ffill").head(10)

pd.merge_asof
^^^^^^^^^^^^^

A merge_asof() is similar to an ordered left-join except that we match on nearest key rather than equal keys. For each row in the left DataFrame, we select the last row in the right DataFrame whose on key is less than the left’s key. Both DataFrames must be sorted by the key

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.asof.html

get closest or partial match

.. code-block:: python

   df_both = pd.merge_ordered(df_be, df_nl, on="date", suffixes=("_be", "_nl"), fill_method="ffill")
   df_all = pd.merge_asof(df_both, df_bris, on="date").rename(columns={"temperature": "temperature_bxl"})
   df_all.plot("date", ["temperature_be", "temperature_nl", "temperature_bxl"])
   # on="date", tolerance=pd.Timedelta("14 days"), direction="neares"

tolerance
^^^^^^^^^

.. code-block:: python

   In [144]: pd.merge_asof(
      .....:     trades,
      .....:     quotes,
      .....:     on="time",
      .....:     by="ticker",
      .....:     tolerance=pd.Timedelta("10ms"),
      .....:     allow_exact_matches=False,
      .....: )
      .....: 
   Out[144]: 
                        time ticker   price  quantity    bid    ask
   0 2016-05-25 13:30:00.023   MSFT   51.95        75    NaN    NaN
   1 2016-05-25 13:30:00.038   MSFT   51.95       155  51.97  51.98
   2 2016-05-25 13:30:00.048   GOOG  720.77       100    NaN    NaN
   3 2016-05-25 13:30:00.048   GOOG  720.92       100    NaN    NaN
   4 2016-05-25 13:30:00.048   AAPL   98.00       100    NaN    NaN

pandas with scikit-learn
------------------------
https://www.youtube.com/watch?v=ylRlGCtAtiE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22

function list
=============

* `drop()` - removes the column or row that you pass in (You also have to specify the axis)
* `agg()` - aggregate function lets you compute summary statistics about each group
* `apply()` - Lets you apply a specific function to any/all elements in a Dataframe or Series
* `get_dummies()` - Helpful for turning categorical data into one hot vectors.
* `drop_duplicates()` - Lets you remove identical rows

.. code-block:: python
.. code-block:: python
.. code-block:: python
.. code-block:: python

