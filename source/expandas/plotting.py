# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
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
