********
plotting
********

links
=====

* https://matplotlib.org/stable/gallery/index.html
* https://matplotlib.org/stable/users/index.html
* https://matplotlib.org/stable/api/animation_api.html#examples
* https://matplotlib.org/stable/api/pyplot_summary.html
* https://seaborn.pydata.org/
* http://seaborn.pydata.org/examples/

resources
=========

* https://www.youtube.com/watch?v=DAQNHzOcO5A

files
=====

.. only:: builder_html or readthedocs

   download csv :download:`here <files/csv/pandas_tut_read.csv>`

matplotlib
==========

first example
-------------

.. code-block:: python

   # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
   import matplotlib.pyplot as plt
   plt.clf()  # clear current figure
   # plt.style.use('dark_background')
   plt.title("learning to plot")
   x =[-3, -2, 5, 0]
   plt.xlabel("x")
   y = [1, 6, 4, 3]
   plt.ylabel("y")
   # axis -> [xmin, xmax, ymin, ymax]
   plt.axis([-4, 7, 0, 7])
   plt.grid(True)
   plt.plot(x, y, 'r--')  # red dashed line
   # plt.plot(label="lolz", color="red", marker='o', linestyle="dashed")
   plt.show()


.. code-block:: python

   # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
   import matplotlib.pyplot as plt
   import Toolkit
   plt.clf()  # clear current figure
   # plt.style.use('dark_background')
   plt.title("learning to plot")
   x = [-3, -2, 5, 0]
   plt.xlabel("x")
   y = [1, 6, 4, 3]
   plt.ylabel("y")
   # axis -> [xmin, xmax, ymin, ymax]
   plt.axis([-4, 7, 0, 7])
   plt.grid(True)
   plt.plot(x, y, 'r--')  # red dashed line
   # plt.plot(label="lolz", color="red", marker='o', linestyle="dashed")
   # plt.show()
   
   np = Toolkit.initiate_numpy()
   x = np.linspace(0, 2, 100)
   plt.clf()
   plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
   plt.plot(x, x**2, label='quadratic')  # etc.
   plt.plot(x, x**3, label='cubic')
   plt.xlabel('x label')
   plt.ylabel('y label')
   plt.title("Simple Plot")
   plt.legend()
   plt.show()

multiple plots
--------------

.. code-block:: python

   plt.clf()
   plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], "r-", [0, 100, 50, 0, 100], [0, 100, 130, 100, 0], "g--")
   plt.axis([-10, 110, -10, 140])
   plt.show()
   
   # or just call plot multiple times
   plt.clf()
   plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], "r-")
   plt.plot([0, 100, 50, 0, 100], [0, 100, 130, 100, 0], "g--")
   plt.axis([-10, 110, -10, 140])
   plt.show()


save plot
---------

.. code-block:: python

   import Toolkit
   np = Toolkit.initiate_numpy()

   x = np.linspace(start=-2, stop=2, num=10)  # num = # of samples to generate
   # [-2.  -1.55555556 -1.11111111 -0.66666667 -0.22222222  0.22222222  0.66666667  1.11111111  1.55555556  2. ]
   plt.clf()
   line1, line2 = plt.plot(x, "g--", x**2, "r--")
   line1.set_linewidth(3.0)
   line1.set_dash_capstyle("round")
   line2.set_alpha(0.2)
   plt.savefig("my_funky_func.png", transparent=True)
   plt.show()

subplots
--------

.. code-block:: python

   plt.clf()
   x = np.linspace(-1.4, 1.4, 30)
   plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
   plt.plot(x, x)
   plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
   plt.plot(x, x**2)
   plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd subplot = bottom left
   plt.plot(x, x**3)
   plt.subplot(2, 2, 4)  # 2 rows, 2 columns, 4th subplot = bottom right
   plt.plot(x, x**4)
   plt.show()

subplots across multiple grid cells
-----------------------------------

.. code-block:: python

   plt.clf()
   plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
   plt.plot(x, x)
   plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
   plt.plot(x, x**2)
   plt.subplot(2, 1, 2)  # 2 rows, *1* column, 2nd subplot = bottom
   plt.plot(x, x**3)
   plt.show()

complex subplots
----------------

.. code-block:: python

   """If you need more complex subplot positioning, you can use subplot2grid instead of subplot
   You specify the number of rows and columns in the grid
   then your subplot's position in that grid (top-left = (0,0))
   and optionally how many rows and/or columns it spans"""
   plt.clf()
   plt.subplot2grid((3, 3), (0, 0), rowspan=2, colspan=2)
   plt.plot(x, x**2)
   plt.subplot2grid((3, 3), (0, 2))
   plt.plot(x, x**3)
   plt.subplot2grid((3, 3), (1, 2), rowspan=2)
   plt.plot(x, x**4)
   plt.subplot2grid((3, 3), (2, 0), colspan=2)
   plt.plot(x, x**5)
   plt.show()

multiple figures
----------------

.. code-block:: python

   plt.clf()
   x = np.linspace(-1.4, 1.4, 30)
   
   plt.figure(1)
   plt.subplot(211)  # rows cols subplots
   plt.plot(x, x**2)
   plt.title("Square and Cube")
   plt.subplot(212)
   plt.plot(x, x**3)
   
   plt.figure(2, figsize=(10, 5))
   plt.subplot(121)
   plt.plot(x, x**4)
   plt.title("y = x**4")
   plt.subplot(122)
   plt.plot(x, x**5)
   plt.title("y = x**5")
   
   plt.figure(1)      # back to figure 1, current subplot is 212 (bottom)
   plt.plot(x, -x**3, "r:")
   plt.show()

statemachine active subplot tracking
------------------------------------

.. code-block:: python

   plt.clf()
   x = np.linspace(-2, 2, 200)
   fig1, (ax_top, ax_bottom) = plt.subplots(2, 1, sharex=True)
   fig1.set_size_inches(10, 5)
   line1, line2 = ax_top.plot(x, np.sin(3*x**2), "r-", x, np.cos(5*x**2), "b-")
   line3, = ax_bottom.plot(x, np.sin(3*x), "r-")
   ax_top.grid(True)
   
   fig2, ax = plt.subplots(1, 1)
   ax.plot(x, x**2)
   plt.show()

text drawing
------------

.. code-block:: python

   plt.clf()
   x = np.linspace(-1.5, 1.5, 30)
   px = 0.8
   py = px**2
   
   plt.plot(x, x**2, "b-", px, py, "ro")
   # specify the horizontal and vertical coordinates
   plt.text(0, 1.5, "Square function\n$y = x^2$", fontsize=20, color='blue', horizontalalignment="center")
   plt.text(px - 0.08, py, "Beautiful point", ha="right", weight="heavy")
   plt.text(px, py, "x = %0.2f\ny = %0.2f" % (px, py), rotation=50, color='gray')
   plt.show()

annotate
--------

.. code-block:: python

   plt.plot(x, x**2, px, py, "ro")
   plt.annotate("Beautiful point", xy=(px, py), xytext=(px-1.3,py+0.5),
                              color="green", weight="heavy", fontsize=14,
                              arrowprops={"facecolor": "lightgreen"})
   plt.show()

legends
-------

.. code-block:: python

   x = np.linspace(-1.4, 1.4, 50)
   plt.plot(x, x**2, "r--", label="Square function")
   plt.plot(x, x**3, "g-", label="Cube function")
   plt.legend(loc="best")
   plt.grid(True)
   plt.show()

Non linear scales
-----------------

.. code-block:: python

   # eg logarithmic or logit scales
   # https://matplotlib.org/stable/gallery/scales/scales.html
   x = np.linspace(0.1, 15, 500)
   y = x**3/np.exp(2*x)
   
   plt.figure(1)
   plt.plot(x, y)
   plt.yscale('linear')
   plt.title('linear')
   plt.grid(True)
   
   plt.figure(2)
   plt.plot(x, y)
   plt.yscale('log')
   plt.title('log')
   plt.grid(True)
   
   plt.figure(3)
   plt.plot(x, y)
   plt.yscale('logit')
   plt.title('logit')
   plt.grid(True)
   
   plt.figure(4)
   plt.plot(x, y - y.mean())
   plt.yscale('symlog', linthresh=0.05)
   plt.title('symlog')
   plt.grid(True)
   plt.show()

scatter
-------

.. code-block:: python

   plt.clf()
   f = plt.figure()
   f.clear()
   plt.close(f)
   for color in ['red', 'green', 'blue']:
       n = 100
       x, y = np.random.rand(2, n)
       scale = 500.0 * np.random.rand(n) ** 5
       plt.scatter(x, y, s=scale, c=color, alpha=0.3, edgecolors='blue')

   plt.grid(True)
   plt.show()


seaborn
=======
http://seaborn.pydata.org/examples/
scatterplot
-----------

.. code-block:: python

   import matplotlib.pyplot as plt
   import Toolkit
   import seaborn as sns

   pd = Toolkit.initiate_pandas(20, 20)
   df = pd.read_csv('files/csv/pokemon.csv', index_col=0)
   print(df.head())
   sns.lmplot(x='Attack', y='Defense', data=df,
              fit_reg=False,  # get rid of regression line
              hue='Stage')  # color by 'Stage' column
   # tweak axes using matplotlib
   plt.ylim(0, 200)
   plt.xlim(0, None)
   plt.show()


boxplot
-------

.. code-block:: python

   import matplotlib.pyplot as plt
   import Toolkit
   import seaborn as sns

   pd = Toolkit.initiate_pandas(20, 20)
   df = pd.read_csv('files/csv/pokemon.csv', index_col=0)
   # pre-format dataframe
   stats_df = df.drop(["Total", "Stage", "Legendary"], axis=1)
   sns.boxplot(data=stats_df)
   plt.show()


violin plot
-----------

shows distribution (violin thickness)

.. code-block:: python

   import matplotlib.pyplot as plt
   import Toolkit
   import seaborn as sns
   
   pd = Toolkit.initiate_pandas(20, 20)
   df = pd.read_csv('files/csv/pokemon.csv', index_col=0)
   sns.set_style("whitegrid")
   pkmn_type_colors = ['#78C850',  # Grass
                       '#F08030',  # Fire
                       '#6890F0',  # Water
                       '#A8B820',  # Bug
                       '#A8A878',  # Normal
                       '#A040A0',  # Poison
                       '#F8D030',  # Electric
                       '#E0C068',  # Ground
                       '#EE99AC',  # Fairy
                       '#C03028',  # Fighting
                       '#F85888',  # Psychic
                       '#B8A038',  # Rock
                       '#705898',  # Ghost
                       '#98D8D8',  # Ice
                       '#7038F8',  # Dragon
                      ]
   # Violin plot with Pokemon color palette
   sns.violinplot(x='Type 1', y='Attack', data=df,
                  palette=pkmn_type_colors) # set color palette
   plt.show()

swarm plot
----------

stacks points with similar values

.. code-block:: python

   # Swarm plot with Pokemon color palette
   sns.swarmplot(x='Type 1', y='Attack', data=df, 
                 palette=pkmn_type_colors)

overlaying plots
----------------

.. code-block:: python

   import matplotlib.pyplot as plt
   import Toolkit
   import seaborn as sns

   pd = Toolkit.initiate_pandas(20, 20)
   df = pd.read_csv('files/csv/pokemon.csv', index_col=0)
   sns.set_style("whitegrid")
   pkmn_type_colors = ['#78C850',  # Grass
                       '#F08030',  # Fire
                       '#6890F0',  # Water
                       '#A8B820',  # Bug
                       '#A8A878',  # Normal
                       '#A040A0',  # Poison
                       '#F8D030',  # Electric
                       '#E0C068',  # Ground
                       '#EE99AC',  # Fairy
                       '#C03028',  # Fighting
                       '#F85888',  # Psychic
                       '#B8A038',  # Rock
                       '#705898',  # Ghost
                       '#98D8D8',  # Ice
                       '#7038F8',  # Dragon
                      ]
   # Violin plot with Pokemon color palette
   # Swarm plot with Pokemon color palette
   sns.violinplot(x='Type 1', y='Attack', data=df,
                  inner=None,  # remove bars inside violins
                  palette=pkmn_type_colors) # set color palette
   sns.swarmplot(x='Type 1', y='Attack', data=df,
                 color='k',  # make swarm points black
                 alpha=0.7)  # slightly transparent
   plt.title('attack by type')
   plt.show()

melt columns
------------

- dataframe to melt
- ID vars to keep (pandas will melt all of the other ones)
- name new melted variable

.. code-block:: python

   # Melt DataFrame
   melted_df = pd.melt(stats_df, 
                       id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                       var_name="Stat") # Name of melted variable
   melted_df.head()


.. code-block:: python

   import matplotlib.pyplot as plt
   import Toolkit
   import seaborn as sns

   pd = Toolkit.initiate_pandas(20, 20)
   df = pd.read_csv('files/csv/pokemon.csv', index_col=0)
   stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
   print(stats_df.head())
   # Melt DataFrame
   melted_df = pd.melt(stats_df,
                       id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                       var_name="Stat") # Name of melted variable
   print(melted_df.head())
   """
            Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed
   #                                                                         
   1   Bulbasaur  Grass  Poison  45      49       49       65       65     45
   2     Ivysaur  Grass  Poison  60      62       63       80       80     60
   3    Venusaur  Grass  Poison  80      82       83      100      100     80
   4  Charmander   Fire     NaN  39      52       43       60       50     65
   5  Charmeleon   Fire     NaN  58      64       58       80       65     80

            Name Type 1  Type 2 Stat  value
   0   Bulbasaur  Grass  Poison   HP     45
   1     Ivysaur  Grass  Poison   HP     60
   2    Venusaur  Grass  Poison   HP     80
   3  Charmander   Fire     NaN   HP     39
   4  Charmeleon   Fire     NaN   HP     58
   """
   print(stats_df.shape)   # (151, 9)
   print(melted_df.shape)  # (906, 5)  x6 rows in stats_df (6 cols melted under Stat)


.. code-block:: python

   # separate swarm by Stat (HP, Attack, Defense..)
   # color points by pokemon type "Type 1"
   pkmn_type_colors = ['#78C850',  # Grass
                       '#F08030',  # Fire
                       '#6890F0',  # Water
                       '#A8B820',  # Bug
                       '#A8A878',  # Normal
                       '#A040A0',  # Poison
                       '#F8D030',  # Electric
                       '#E0C068',  # Ground
                       '#EE99AC',  # Fairy
                       '#C03028',  # Fighting
                       '#F85888',  # Psychic
                       '#B8A038',  # Rock
                       '#705898',  # Ghost
                       '#98D8D8',  # Ice
                       '#7038F8',  # Dragon
                      ]
   plt.figure(figsize=(12, 8))
   sns.swarmplot(x="Stat",
                 y="value",
                 data=melted_df,
                 hue="Type 1",
                 dodge=True,  # separate points by hue
                 palette=pkmn_type_colors,
                 size=5)  # size of marker points
   plt.ylim(0, 260)  # adjust y-axis
   plt.legend(bbox_to_anchor=(1, 1), loc=2)  # place legend box to right
   plt.title('attack by type')
   plt.show()

heatmap
-------

.. code-block:: python

   # Calculate correlations
   corr = stats_df.corr()

   # Heatmap
   sns.heatmap(corr)

histogram
---------

.. code-block:: python

   # Distribution Plot (a.k.a. Histogram)
   sns.distplot(df.Attack)

bar plot
--------

.. code-block:: python

   # Count Plot (a.k.a. Bar Plot)
   sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)

   # Rotate x-labels
   plt.xticks(rotation=-45)

factor plot
-----------

.. code-block:: python

   # Factor Plot
   g = sns.catplot(x='Type 1', 
                      y='Attack', 
                      data=df, 
                      hue='Stage',  # Color by stage
                      col='Stage',  # Separate by stage
                      kind='swarm') # Swarmplot

   # Rotate x-axis labels
   g.set_xticklabels(rotation=-45)

   # plt.xticks(rotation=-45) Doesn't work because only rotates last plot

density plot
------------

.. code-block:: python

   # Density Plot
   sns.kdeplot(df.Attack, df.Defense)

joint distribution plot
-----------------------

.. code-block:: python

   # Joint Distribution Plot
   sns.jointplot(x='Attack', y='Defense', data=df)


