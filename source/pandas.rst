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

.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

.. code-block:: python


.. code-block:: python


.. code-block:: python

