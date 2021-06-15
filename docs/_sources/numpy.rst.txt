*****
numpy
*****
vocabulary
==========

- each dimension = an axis
- number of axes = the rank
 - a 3x4 matrix is an array of rank 2 (2-dimensional)
 - first axis has length 3, second length 4
  ::

    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])
- list(axis length) = shape of array
 - matrix shape = (3, 4)
 - rank is equal to shape's length
- size of an array = total number of elements = product axis lengths (3*4=12)

creating arrays
===============

np.array
--------

create an array numpy with two rows and three columns

.. code-block:: python

   A = np.array([[1,2,3],[4,5,6]])
   # array([[1, 2, 3],
   #        [4, 5, 6]])

show dimensions
^^^^^^^^^^^^^^^

.. code-block:: python

   A.shape
   # (2, 3)


np.zeros
--------

.. code-block:: python

   zeros = np.zeros((2,3))
   # array([[0., 0., 0.],
   #        [0., 0., 0.]])

np.ones
-------

.. code-block:: python

   ones = np.ones((2,3))
   # array([[1., 1., 1.],
   #        [1., 1., 1.]])

np.arange
---------

.. code-block:: python

   np.arange(10)
   # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

.. note::

   Like the range() function in python, we can also indicate the start point,
   the end point and the step.
   **np.arange(start, end, step)**

.. code-block:: python

   np.arange(0, 10, 2)
   # array([0, 2, 4, 6, 8])


np.linspace
-----------

must have same distance/space between values
create 5 values between 0 and 1 evenly spaced

.. code-block:: python

   np.linspace(0, 1, 5)
   # array([0.  , 0.25, 0.5 , 0.75, 1.  ])


np.eye
------

returns identity matrix (diagonal 1s & 0s elsewhere)

.. code-block:: python

   np.eye(3)
   # array([[1., 0., 0.],
   #       [0., 1., 0.],
   #       [0., 0., 1.]])

shape ndim size
---------------

.. code-block:: python

   a = np.zeros((3,4))
   # array([[0., 0., 0., 0.],
   #        [0., 0., 0., 0.],
   #        [0., 0., 0., 0.]])
   a.shape
   # (3, 4)
   a.ndim # equal to len(a.shape), which is the rank
   # 2
   a.size
   # 12

np.concatenate
--------------

concatenate or join arrays

.. code-block:: python

   x = np.array([1, 2, 3])
   y = np.array([3, 2, 1])

   np.concatenate([x, y])
   # array([1, 2, 3, 3, 2, 1])


If the arrays are multidimensional, you can use either vstack  (vertical) or  hstack  (horizontal).

.. note:: stack em horizontally or stack em vertically :)

.. code-block:: python

   x = np.array([1, 2, 3])
   grid = np.array([[9, 8, 7], [6, 5, 4]])

   np.vstack([x, grid])
   # array([[1, 2, 3],
   #        [9, 8, 7],
   #        [6, 5, 4]])

N-dimensional arrays
--------------------

create 3D array rank 3
with shape (2, 3, 4)

.. code-block:: python

   np.ones((2, 3, 4))
   # [[[1. 1. 1. 1.]
   #   [1. 1. 1. 1.]
   #   [1. 1. 1. 1.]]
   # 
   #  [[1. 1. 1. 1.]
   #   [1. 1. 1. 1.]
   #   [1. 1. 1. 1.]]]

   type(np.ones((2,3,4)))
   # numpy.ndarray

np.full
-------

create array with given shape and given value

.. code-block:: python

   np.full((3,4), np.pi)

   # array([[3.14159265, 3.14159265, 3.14159265, 3.14159265],
   #        [3.14159265, 3.14159265, 3.14159265, 3.14159265],
   #        [3.14159265, 3.14159265, 3.14159265, 3.14159265]])


np.empty
--------

uninitialized array (content comes from memory and is not predictable)

.. code-block:: python

   np.empty((2,3))
   # array([[0.4875119 , 0.78426035, 0.71177185, 0.58423021],
   #        [0.89637291, 0.25875126, 0.20124882, 0.03091878],
   #        [0.1340354 , 0.05263092, 0.76936044, 0.54766349]])

array data
==========
np.dtype
--------

Available data types include int8, int16, int32, int64, uint8|16|32|64, float16|32|64 and complex64|128  

Check out the documentation for the full list.
https://numpy.org/doc/stable/reference/arrays.dtypes.html

ndarrays have to have the same data type
you can check with the dtype attribute

.. code-block:: python

   c = np.arange(1, 5)
   print(c.dtype, c)
   # int64 [1 2 3 4]

   c = np.arange(1.0, 5.0)
   print(c.dtype, c)
   # float64 [1. 2. 3. 4.]

   d = np.arange(1, 5, dtype=np.complex64)
   print(d.dtype, d)
   # complex64 [1.+0.j 2.+0.j 3.+0.j 4.+0.j]

itemsize
--------

The itemsize attribute returns the size (in bytes) of each item:

.. code-block:: python

   e = np.arange(1, 5, dtype=np.complex64)
   e.itemsize
   # 8

data buffer
-----------
An array's data is actually stored in memory as a flat (one dimensional) byte buffer  
It is available via the data attribute (you will rarely need it, though).

.. code-block:: python

   f = np.array([[1,2],[1000, 2000]], dtype=np.int32)
   f.data
   # <memory at 0x7f8765b175f0>

dive into arrays
----------------

.. code-block:: python

   np.random.seed(0)
   x1 = np.random.randint(10, size=6)  
   x1
   # array([5, 0, 3, 3, 7, 9])


Print the first 5 elements of an array:

.. code-block:: python

   print(x1[:5])
   # [5 0 3 3 7]


Print the elements from the 6th and on of an array:

.. code-block:: python

   print(x1[5:])  
   # [9]


Print every two elements of an array:

.. code-block:: python

   print(x1[::2])
   # [5 3 7]

arithmetic operations
=====================
operators
---------

.. code-block:: python

   a = np.array([14, 23, 32, 41])
   b = np.array([5,  4,  3,  2])
   print("a + b  =", a + b)
   print("a - b  =", a - b)
   print("a * b  =", a * b)
   print("a / b  =", a / b)
   print("a // b  =", a // b)
   print("a % b  =", a % b)
   print("a ** b =", a ** b)
   # a + b  = [19 27 35 43]
   # a - b  = [ 9 19 29 39]
   # a * b  = [70 92 96 82]
   # a / b  = [ 2.8         5.75       10.66666667 20.5       ]
   # a // b  = [ 2  5 10 20]
   # a % b  = [4 3 2 1]
   # a ** b = [537824 279841  32768   1681]

matrix addition & subtraction
-----------------------------

.. note::

   they must have the same dimensions
   ValueError: operands could not be broadcast together with shapes (2,3) (2,2)
   3 columns and 2 columns can't be added

.. code-block:: python

   A = np.array([[1,2,3],[4,5,6]])
   B = np.array([[7,8,9],[10,11,12]])
   C = A + B
   C
   # array([[ 8, 10, 12],
   #       [14, 16, 18]])


.. code-block:: python

   A = np.array([[1,2,3],[4,5,6]])
   B = np.array([[7,8,9],[10,11,12]])
   C = A - B
   C
   # array([[-6, -6, -6],
   #        [-6, -6, -6]])

matrix multiplication
---------------------

multiple all values

.. code-block:: python

   C = A * 2
   C
   # array([[ 2,  4,  6],
   #        [ 8, 10, 12]])

.. warning:: columns in A must be equal to rows in B

.. code-block:: python

   A = np.array([[1,2,3],[4,5,6]])
   B = np.array([[1,2],[3,4],[5,6]])
   print(A.shape, B.shape)
   # (2, 3) (3, 2)

   C = A.dot(B)
   C
   # array([[22, 28],
   #        [49, 64]])

.. note::

  if  columns/rows don't correspond you get following error  
   ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)

.. code-block:: python

To solve the problem we can make a transposition

.. code-block:: python

   BT = B.T
   BT.shape
   # (3, 2)

We can now perform the multiplication

.. code-block:: python

   A.dot(BT)
   # array([[14, 32],
   #       [32, 77]])

broadcasting
============
https://numpy.org/doc/stable/user/basics.broadcasting.html

first rule
----------

If the arrays do not have the same rank, then a 1 will be prepended to the smaller ranking arrays until their ranks match.

.. code-block:: python

   h = np.arange(5).reshape(1, 1, 5)
   h
   # array([[[0, 1, 2, 3, 4]]])

Now let's try to add a 1D array of shape (5,) to this 3D array of shape (1,1,5). Applying the first rule of broadcasting!

.. code-block:: python

   h + [10, 20, 30, 40, 50]  # same as: h + [[[10, 20, 30, 40, 50]]]
   # array([[[10, 21, 32, 43, 54]]])

second rule
-----------

two dimensions are compatible when one of them is 1

.. code::

   A      (2d array):  5 x 4
   B      (1d array):      1
   Result (2d array):  5 x 4
   
   A      (2d array):  5 x 4
   B      (1d array):      4
   Result (2d array):  5 x 4
   
   A      (3d array):  15 x 3 x 5
   B      (3d array):  15 x 1 x 5
   Result (3d array):  15 x 3 x 5
   
   A      (3d array):  15 x 3 x 5
   B      (2d array):       3 x 5
   Result (3d array):  15 x 3 x 5
   
   A      (3d array):  15 x 3 x 5
   B      (2d array):       3 x 1
   Result (3d array):  15 x 3 x 5

.. code-block:: python

   k = np.arange(6).reshape(2, 3)
   k
   # array([[0, 1, 2],
   #        [3, 4, 5]])

Let's try to add a 2D array of shape (2,1) to this 2D ndarray of shape (2, 3). NumPy will apply the second rule of broadcasting:

.. code-block:: python

   k + [[100], [200]]  # same as: k + [[100, 100, 100], [200, 200, 200]]
   # array([[100, 101, 102],
   #        [203, 204, 205]])

Combining rules 1 & 2, we can do this:

.. code-block:: python

   k + [100, 200, 300]  # after rule 1: [[100, 200, 300]], and after rule 2: [[100, 200, 300], [100, 200, 300]]
   # array([[100, 201, 302],
   #        [103, 204, 305]])

And also, very simply:

.. code-block:: python

   k + 1000  # same as: k + [[1000, 1000, 1000], [1000, 1000, 1000]]
   # array([[1000, 1001, 1002],
   #        [1003, 1004, 1005]])

examples
--------

.. code::

   >>> x = np.arange(4)
   >>> xx = x.reshape(4,1)
   >>> y = np.ones(5)
   >>> z = np.ones((3,4))
   
   >>> x.shape
   (4,)
   
   >>> y.shape
   (5,)
   
   >>> x + y
   ValueError: operands could not be broadcast together with shapes (4,) (5,)
   
   >>> xx.shape
   (4, 1)
   
   >>> y.shape
   (5,)
   
   >>> (xx + y).shape
   (4, 5)
   
   >>> xx + y
   array([[ 1.,  1.,  1.,  1.,  1.],
          [ 2.,  2.,  2.,  2.,  2.],
          [ 3.,  3.,  3.,  3.,  3.],
          [ 4.,  4.,  4.,  4.,  4.]])
   
   >>> x.shape
   (4,)
   
   >>> z.shape
   (3, 4)
   
   >>> (x + z).shape
   (3, 4)
   
   >>> x + z
   array([[ 1.,  2.,  3.,  4.],
          [ 1.,  2.,  3.,  4.],
          [ 1.,  2.,  3.,  4.]])

Broadcasting provides a convenient way of taking the outer product (or any other outer operation) of two arrays. The following example shows an outer addition operation of two 1-d arrays:

.. code::

   >>> a = np.array([0.0, 10.0, 20.0, 30.0])
   >>> b = np.array([1.0, 2.0, 3.0])
   >>> a[:, np.newaxis] + b
   array([[  1.,   2.,   3.],
          [ 11.,  12.,  13.],
          [ 21.,  22.,  23.],
          [ 31.,  32.,  33.]])


Here the newaxis index operator inserts a new axis into a, making it a two-dimensional 4x1 array. Combining the 4x1 array with b, which has shape (3,), yields a 4x3 array.

math and stats functions
========================

ndarray methods
---------------
Some functions are simply ndarray methods, for example:

.. code-block:: python

   a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
   print(a)
   print("mean =", a.mean())
   # [[-2.5  3.1  7. ]
   #  [10.  11.  12. ]]
   # mean = 6.766666666666667

.. note:: this computes the mean of all elements in the ndarray, regardless of its shape

Here are a few more useful ndarray methods:

.. code-block:: python

   for func in (a.min, a.max, a.sum, a.prod, a.std, a.var):
       print(func.__name__, "=", func())
   min = -2.5
   max = 12.0
   sum = 40.6
   # prod = -71610.0
   # std = 5.084835843520964
   # var = 25.855555555555554

These functions accept an optional argument axis which lets you ask for the operation to be performed on elements along the given axis. For example:

.. code-block:: python

   c=np.arange(24).reshape(2,3,4)
   c
   """
   array([[[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]],

          [[12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23]]])"""

   c.sum(axis=0)  # sum across matrices
   """
   array([[12, 14, 16, 18],
          [20, 22, 24, 26],
          [28, 30, 32, 34]])"""

   c.sum(axis=1)  # sum across rows
   """
   array([[12, 15, 18, 21],
          [48, 51, 54, 57]])"""

   c.sum(axis=(0,2))  # sum across matrices and columns
   # array([ 60,  92, 124])

   0+1+2+3 + 12+13+14+15, 4+5+6+7 + 16+17+18+19, 8+9+10+11 + 20+21+22+23
   # (60, 92, 124)

universal functions
===================

wrappers
--------

NumPy also provides fast elementwise functions called universal functions, or ufunc. They are vectorized wrappers of simple functions. For example square returns a new ndarray which is a copy of the original ndarray except that each element is squared:


.. code-block:: python

   a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
   np.square(a)
   array([[  6.25,   9.61,  49.  ],
          [100.  , 121.  , 144.  ]])

Here are a few more useful unary ufuncs:

.. code-block:: python

   print("Original ndarray")
   print(a)
   for func in (np.abs, np.square, np.exp, np.sign, np.ceil, np.modf, np.isnan, np.cos):
       print("\n", func.__name__)
       print(func(a))

::

  Original ndarray
  [[-2.5  3.1  7. ]
   [10.  11.  12. ]]
  
   absolute
  [[ 2.5  3.1  7. ]
   [10.  11.  12. ]]
  
   square
  [[  6.25   9.61  49.  ]
   [100.   121.   144.  ]]
  
   exp
  [[8.20849986e-02 2.21979513e+01 1.09663316e+03]
   [2.20264658e+04 5.98741417e+04 1.62754791e+05]]
  
   sign
  [[-1.  1.  1.]
   [ 1.  1.  1.]]
  
   ceil
  [[-2.  4.  7.]
   [10. 11. 12.]]
  
   modf
  (array([[-0.5,  0.1,  0. ],
         [ 0. ,  0. ,  0. ]]), array([[-2.,  3.,  7.],
         [10., 11., 12.]]))
  
   isnan
  [[False False False]
   [False False False]]
  
   cos
  [[-0.80114362 -0.99913515  0.75390225]
   [-0.83907153  0.0044257   0.84385396]]

.. code-block:: python
.. code-block:: python
.. code-block:: python
.. code-block:: python
.. code-block:: python
.. code-block:: python
