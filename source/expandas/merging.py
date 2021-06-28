import Toolkit
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#
pd = Toolkit.initiate_pandas()


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
import matplotlib.pyplot as plt
plot = plt.plot(df_3)

# plt.clf()
plot2 = plt.plot(df_2)
plt.show
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