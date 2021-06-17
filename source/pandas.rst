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


basics
======

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

extracting rows & columns
=========================

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

   you can achieve the same result by using the loc function. loc is a veryyyy versatile function that can help you in a lot of accessing and extracting tasks


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

kaggle
======
https://www.kaggle.com/competitions

creating kaggle submissions CSV's
---------------------------------

.. code-block:: python

   import numpy as np
   import csv

   results = [[0,10],[1,15],[2,20]]
   results = pd.np.array(results) # panda numpy will be deprecated
   print(results)
   """
   [[ 0 10]
    [ 1 15]
    [ 2 20]]
   <ipython-input-37-27b9a7fe8db6>:5: FutureWarning: The pandas.np module is deprecated and will be removed from pandas in a future version. Import numpy directly instead
     results = pd.np.array(results)
   """

   firstRow = [['id', 'pred']]
   with open("result.csv", "w") as f:
       writer = csv.writer(f)
       writer.writerows(firstRow)
       writer.writerows(results)



use pandas with scikit-learn
----------------------------
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

