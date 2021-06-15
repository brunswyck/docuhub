*****
numpy
*****
links
=====

- https://numpy.org/doc
- https://www.guru99.com/numpy-tutorial.html
- https://www.w3schools.com/python/numpy_intro.asp
- https://cs231n.github.io/python-numpy-tutorial

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

numpractice
===========

print numpy version and the configuration
-----------------------------------------

.. code-block:: python

   import numpy as np
   print(np.version.full_version)
   print(np.version.full_version)
   1.20.3

create a null vector of size 10
-------------------------------

.. code-block:: python

   import numpy as np
   x = np.zeros(10)
   print(x)
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

find memory size of any array
-----------------------------

.. code-block:: python

   x.size  # 10
   x.itemsize  # 8 in bytes
   print(x.size * x.itemsize)

nbytes: attribute gives total bytes consumed by the elements of the NumPy array
-------------------------------------------------------------------------------

.. code-block:: python

   print(f"mem size of numpy array: {x.nbytes}")
   80
   mem size of numpy array: 80

get the docs on numpy add function
----------------------------------

.. code-block:: python

   print(np.info(np.add))
   add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
   """
   Add arguments element-wise.

   Parameters
   ----------
   x1, x2 : array_like
       The arrays to be added.
       If ``x1.shape != x2.shape``, they must be broadcastable to a common
       shape (which becomes the shape of the output).
   out : ndarray, None, or tuple of ndarray and None, optional
       A location into which the result is stored. If provided, it must have
       a shape that the inputs broadcast to. If not provided or None,
       a freshly-allocated array is returned. A tuple (possible only as a
       keyword argument) must have length equal to the number of outputs.
   where : array_like, optional
       This condition is broadcast over the input. At locations where the
       condition is True, the `out` array will be set to the ufunc result.
       Elsewhere, the `out` array will retain its original value.
       Note that if an uninitialized `out` array is created via the default
       ``out=None``, locations within it where the condition is False will
       remain uninitialized.
   **kwargs
       For other keyword-only arguments, see the
       :ref:`ufunc docs <ufuncs.kwargs>`.

   Returns
   -------
   add : ndarray or scalar
       The sum of `x1` and `x2`, element-wise.
       This is a scalar if both `x1` and `x2` are scalars.

   Notes
   -----
   Equivalent to `x1` + `x2` in terms of array broadcasting.

   Examples
   --------
   >>> np.add(1.0, 4.0)
   5.0
   >>> x1 = np.arange(9.0).reshape((3, 3))
   >>> x2 = np.arange(3.0)
   >>> np.add(x1, x2)
   array([[  0.,   2.,   4.],
          [  3.,   5.,   7.],
          [  6.,   8.,  10.]])

   The ``+`` operator can be used as a shorthand for ``np.add`` on ndarrays.

   >>> x1 = np.arange(9.0).reshape((3, 3))
   >>> x2 = np.arange(3.0)
   >>> x1 + x2
   array([[ 0.,  2.,  4.],
          [ 3.,  5.,  7.],
          [ 6.,  8., 10.]])
   """

create a vector with values ranging from 10 to 49
-------------------------------------------------

.. code-block:: python

   # https://numpy.org/doc/stable/reference/generated/numpy.arange.html
   # numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)¶
   x = np.arange(10, 50, 1)
   x
   array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
          27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
          44, 45, 46, 47, 48, 49])

Reverse a vector (first element becomes last)
---------------------------------------------

.. code-block:: python

   # https://numpy.org/doc/stable/reference/generated/numpy.flip.html?highlight=reverse
   import copy
   A = np.arange(8).reshape((2, 4))
   print(A)
   B = copy.deepcopy(np.flip(A))
   B
   [[0 1 2 3]
    [4 5 6 7]]
   array([[7, 6, 5, 4],
          [3, 2, 1, 0]])

create 3x3 matrix w values ranging from 0 to 8
----------------------------------------------

.. code-block:: python

   A = np.array([np.arange(0,3), np.arange(3, 6), np.arange(6, 9)])
   # now with reshape
   # https://numpy.org/doc/stable/reference/generated/numpy.reshape.html?highlight=reshape#numpy.reshape
   B = np.arange(0, 9, 1).reshape(3, 3)
   B
   array([[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]])

Find indices of non-zero elements from [1,2,0,0,4,0]
----------------------------------------------------

.. code-block:: python

   # https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html
   x = np.array([1,2,0,0,4,0])
   np.nonzero(x)
   (array([0, 1, 4]),)

create a 3x3 identity matrix
----------------------------

.. code-block:: python

   X
   X = np.identity(3)
   X
   array([[1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 1.]])

create a 3x3x3 array with random values
---------------------------------------

.. code-block:: python

   X = np.random.rand(3,3)
   print(X)
   Y = np.random.rand(3,3,3)
   Y
   [[0.98332566 0.84116444 0.75410407]
    [0.9790408  0.15237009 0.35937882]
    [0.60683975 0.3339919  0.41256535]]
   array([[[0.76573681, 0.29366637, 0.47391383],
           [0.71257996, 0.62837487, 0.95957082],
           [0.92516253, 0.38340549, 0.74710955]],

          [[0.02144192, 0.00834815, 0.48610525],
           [0.00178446, 0.91594102, 0.9474838 ],
           [0.21823699, 0.77754962, 0.5684341 ]],

          [[0.04352024, 0.91370673, 0.52169201],
           [0.55976612, 0.54704399, 0.29708297],
           [0.43227997, 0.94912278, 0.79186423]]])

create a 10x10 array with random values and find the min max values
-------------------------------------------------------------------

.. code-block:: python

   X = np.random.rand(10, 10)
   x_min, x_max = X.min(), X.max()
   X, x_min, x_max
   (array([[0.68245006, 0.33805442, 0.64817297, 0.7701081 , 0.43707238,
            0.47236216, 0.52916113, 0.12676572, 0.02807957, 0.92689844],
           [0.59196201, 0.93834978, 0.88414265, 0.89950303, 0.6424275 ,
            0.83488977, 0.73490878, 0.10112525, 0.53945921, 0.86992843],
           [0.72687907, 0.91081264, 0.73671922, 0.84801847, 0.28416749,
            0.44848551, 0.92801694, 0.10887357, 0.16693172, 0.33413767],
           [0.03412656, 0.37407818, 0.96190285, 0.60326469, 0.10789708,
            0.53779934, 0.43094553, 0.94931895, 0.77332064, 0.23077922],
           [0.51224525, 0.43105436, 0.72417317, 0.41080638, 0.11075047,
            0.5238756 , 0.91185676, 0.36304757, 0.7213532 , 0.1998049 ],
           [0.81966608, 0.36168062, 0.24690469, 0.23518279, 0.04569355,
            0.99256271, 0.17775566, 0.29407587, 0.46219508, 0.92000002],
           [0.58264479, 0.3913255 , 0.1487941 , 0.93989212, 0.93152326,
            0.63672583, 0.49067863, 0.99631981, 0.22439821, 0.13945929],
           [0.11131928, 0.699683  , 0.00827745, 0.33092946, 0.54675461,
            0.44746111, 0.48443178, 0.25829608, 0.40651901, 0.34711342],
           [0.64217007, 0.29458234, 0.63254603, 0.38620369, 0.73063494,
            0.47140773, 0.80645127, 0.56806584, 0.37139742, 0.63902335],
           [0.90009945, 0.48907321, 0.37904051, 0.80038649, 0.79737416,
            0.10121237, 0.77313591, 0.16813614, 0.43280661, 0.74821215]]),
    0.00827744590659174,
    0.996319810057414)

create a random vector of size 30 and find mean value
-----------------------------------------------------

.. code-block:: python

   X = np.random.random_sample(30)
   mean_value = X.mean()
   X, mean_value
   (array([0.97879743, 0.99007651, 0.62769786, 0.79962993, 0.76487594,
           0.28558696, 0.80630438, 0.01818697, 0.50862024, 0.9552484 ,
           0.51288462, 0.01863474, 0.34000259, 0.59681974, 0.59793668,
           0.2089018 , 0.79393369, 0.64916354, 0.01968166, 0.05974539,
           0.61850869, 0.50107583, 0.61428685, 0.96729492, 0.59925488,
           0.89414214, 0.15592456, 0.89784793, 0.7398289 , 0.70381768]),
    0.5741570486620552)

create a 2d array with 1s on the border and 0s inside
-----------------------------------------------------

.. code-block:: python

   A = np.ones((5,5))
   A[1:-1, 1:-1] = 0  # all but first and last in row and column
   A
   array([[1., 1., 1., 1., 1.],
          [1., 0., 0., 0., 1.],
          [1., 0., 0., 0., 1.],
          [1., 0., 0., 0., 1.],
          [1., 1., 1., 1., 1.]])

add a border (filled with 0's) around an existing array
-------------------------------------------------------

.. code-block:: python

   A, Y
   # numpy.pad(array, pad_width, mode='constant', **kwargs)  
   A = np.ones((3, 3))
   Y = np.pad(A, pad_width=1, mode='constant', constant_values=0)
   A, Y
   (array([[1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.]]),
    array([[0., 0., 0., 0., 0.],
           [0., 1., 1., 1., 0.],
           [0., 1., 1., 1., 0.],
           [0., 1., 1., 1., 0.],
           [0., 0., 0., 0., 0.]]))

results of np.nan expressions
-----------------------------

.. code-block:: python

   ```python
   0 * np.nan
   np.nan == np.nan
   np.inf > np.nan
   np.nan - np.nan
   np.nan in set([np.nan])
   0.3 == 3 * 0.1
   ```
   # document examples here
   # https://numpy.org/doc/stable/user/misc.html
   X = np.nan
   X == np.nan  # is always False! Use special numpy functions
   False

create a 5x5 matrix with values 1,2,3,4 just below the diagonal
---------------------------------------------------------------

.. code-block:: python

   A = np.random.rand(5,5)
   A # so that would be on position row,col (1,0)(2,1)(3,2)(4,3)
   sub_diagonal_positions = range(1,5,1)
   for x in sub_diagonal_positions:
       print(f"(row,col): {x},{x-1}")
   A
   (row,col): 1,0
   (row,col): 2,1
   (row,col): 3,2
   (row,col): 4,3
   array([[0.47562091, 0.8459493 , 0.70160341, 0.32535192, 0.35934161],
          [0.84101674, 0.14958274, 0.55761373, 0.78466964, 0.53366355],
          [0.14600348, 0.41870539, 0.16958068, 0.37412754, 0.88409359],
          [0.70830397, 0.30946462, 0.53519198, 0.75792345, 0.93940042],
          [0.65121911, 0.12916815, 0.31555863, 0.51943925, 0.48102947]])

create a 8x8 matrix and fill with a checkerboard pattern
--------------------------------------------------------

.. code-block:: python

   x = np.zeros((8,8),dtype=int)
   x[1::2,::2] = 1  # fill with 1 from row 1 -> till 1+2+2...
   x[::2,1::2] = 1  # fill with 1 from row 0 -> till 0+2+2...
   x
   array([[0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0]])

given a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
---------------------------------------------------------------------------

.. code-block:: python

   A = np.random.randint(1,20, size=(6,7,8))
   indices_wanted = [0,99]  # as check also show first value
   bingo = np.take(A, indices_wanted)
   # x = np.where(A == bingo)
   A, bingo
   """
   (array([[[14,  7, 14,  7, 17,  6, 17,  1],
            [10, 12, 13,  9,  8,  8,  2, 16],
            [ 7, 10, 12,  9, 11,  7,  8,  5],
            [ 4, 10,  6, 11, 18, 12, 12, 10],
            [ 2, 17,  1, 11, 18, 19, 16,  7],
            [ 9,  2, 17, 19, 15, 17, 19,  5],
            [11,  9, 10, 14,  9, 17,  3, 10]],

           [[12, 12,  8, 18,  3, 16, 10, 17],
            [ 1,  6,  9, 16, 18,  7, 17, 19],
            [17,  6,  8,  7, 19,  2, 16,  1],
            [12,  1,  7,  9, 15, 18,  6,  5],
            [ 4,  2,  9,  6, 13, 19,  9,  3],
            [17, 19,  6,  4,  6,  9, 18,  9],
            [ 3,  1, 18, 11,  2, 16, 19, 19]],

           [[13,  3,  6, 18,  9,  9,  7, 13],
            [ 3,  4,  7, 11, 18, 14,  8, 13],
            [19,  2, 10, 19,  3, 15, 13, 11],
            [ 6,  5, 13,  2,  6, 19, 15,  7],
            [ 2, 12, 13, 11,  4,  6,  5, 17],
            [ 6, 15, 19, 12, 12, 11, 19,  4],
            [11, 13, 12, 13, 16,  2,  9, 13]],

           [[ 9, 19, 19,  1,  7, 10, 15, 19],
            [ 7,  4, 17, 11, 13, 13,  6,  3],
            [13,  6, 17,  7,  3, 19, 15,  6],
            [ 2, 11,  1, 15, 13,  3, 13,  7],
            [ 2, 12,  7, 12,  4, 11,  4, 19],
            [ 8,  2, 15,  3, 12,  7, 10,  8],
            [ 4,  5, 18, 12, 19,  9,  7, 18]],

           [[ 5, 18, 16,  9, 13,  9, 10, 18],
            [17, 13, 17, 11, 16, 11,  4,  8],
            [18, 19,  5, 14,  5, 14,  2,  2],
            [12, 19,  8, 16, 15,  9,  5,  9],
            [11, 19, 13, 19,  6,  2,  3,  1],
            [ 3,  7, 19,  8, 11, 19,  3,  3],
            [13, 19,  8, 18,  4,  4, 14, 15]],

           [[ 6, 18, 14,  3,  4, 13, 15, 14],
            [ 2,  1,  9,  5,  2, 19,  4, 15],
            [ 8,  9,  9, 19,  7, 15, 19,  9],
            [ 2, 12, 18, 18, 15, 14,  9, 12],
            [14, 14,  9, 17,  1,  5,  1,  4],
            [15,  5,  1, 11,  3,  6, 10, 14],
            [10,  2, 16, 13, 11, 10, 12,  7]]]),
    array([14,  4]))"""

checkerboard
------------

.. code-block:: python

   """
   Create a checkerboard 8x8 matrix using the tile function
   https://numpy.org/doc/stable/reference/generated/numpy.tile.html
   use Numpy's tile function to get checkerboard array of size n*m where n and m should be even numbers"""

   def create_checkboard(n,m):
       list_0_1 = np.array([ [ 0, 1], [ 1, 0] ])
       checkerboard = np.tile(list_0_1, ( n//2, m//2)) 
       print(checkerboard.shape)
       return checkerboard

   create_checkboard(4,6)
   (4, 6)
   array([[0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0]])

normalize a 5x5 random matrix
-----------------------------

.. code-block:: python

   x = np.random.random((5,5))
   print(f"before normalize: {x}")

   xmax, xmin = x.max(), x.min()
   x = (x - xmin)/(xmax - xmin)
   x
   """
   before normalize: [[0.61887892 0.48893607 0.5047862  0.74653032 0.09313412]
    [0.30621631 0.83629173 0.98807878 0.16518118 0.97542081]
    [0.1876475  0.04579762 0.67820882 0.38155519 0.90372504]
    [0.08171901 0.63700914 0.96842558 0.9939399  0.02900476]
    [0.11294267 0.6768546  0.24658038 0.02097271 0.77710329]]
   """
   array([[0.61451837, 0.4809652 , 0.49725571, 0.74571642, 0.07416633],
          [0.29316878, 0.83797176, 0.99397603, 0.14821514, 0.98096638],
          [0.17130566, 0.02551464, 0.67549669, 0.37060086, 0.90727862],
          [0.06243406, 0.63315232, 0.9737768 , 1.        , 0.00825521],
          [0.09452524, 0.67410484, 0.23187592, 0.        , 0.77713883]])

create custom dtype describing RGBA color as four unsigned bytes
----------------------------------------------------------------

.. code-block:: python

   color = np.dtype([("r", np.ubyte),
                     ("g", np.ubyte),
                     ("b", np.ubyte),
                     ("a", np.ubyte)])
   color
   dtype([('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')])

multiply 5x3 matrix by a 3x2 matrix (real matrix product)
---------------------------------------------------------

.. code-block:: python

   x = np.arange(15).reshape((5, 3))
   y = np.arange(6).reshape((3, 2))
   np.dot(x, y)

   array([[ 10,  13],
          [ 28,  40],
          [ 46,  67],
          [ 64,  94],
          [ 82, 121]])

in normal array negate elements that are between 3 and 8, in place
------------------------------------------------------------------

.. code-block:: python

   x = np.arange(11)
   print(x)
   x[(x >= 3) & (x <= 8)] = -1
   x
   [ 0  1  2  3  4  5  6  7  8  9 10]
   array([ 0,  1,  2, -1, -1, -1, -1, -1, -1,  9, 10])

output of the following script
------------------------------

.. code-block:: python


   print(sum(range(5),-1))  # 9
   from numpy import *
   print(sum(range(5),-1))
   9
   10

consider integer vector Z, which  of these expressions are legal
----------------------------------------------------------------

.. code-block:: python

   Z**Z
   2 << Z >> 2
   Z <- Z
   1j*Z
   Z/1/1
   Z<Z>Z
   Z = np.arange(3)

   Z ** Z       # = [0^0, 1^1, 2^2] = [1, 1, 4]
   2 << Z >> 2  # = [0, 1, 2]
   Z < - Z      # = [False, False, False]
   1j * Z       # = [0 + 0.j, 0 + 1.j, 0 + 2.j]
   Z / 1 / 1    # = [0, 1, 2] # array([0., 1., 2.])
   # Z < Z > Z    # ValueError


np.nan
------

.. code-block:: python

   # results of the following expressions
   ```
   np.array(0) / np.array(0)
   np.array(0) // np.array(0)
   np.array([np.nan]).astype(int).astype(float)
   ```
   np.array(0) / np.array(0)
   ```
   <ipython-input-162-3585dcb7ab9b>:1: RuntimeWarning: invalid value encountered in true_divide
     np.array(0) / np.array(0)
   ```
   nan

   np.array(0) // np.array(0)
   ```
   <ipython-input-163-4764261090d0>:1: RuntimeWarning: divide by zero encountered in floor_divide
     np.array(0) // np.array(0)
   ```
   0

   np.array([np.nan]).astype(int).astype(float)
   array([-9.22337204e+18])


round x decimals from zero in a float array
-------------------------------------------

.. code-block:: python

   # https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round
   data = np.random.uniform(-10, +10, 12)
   np.round(data, 2)  # round to 2 decimals
   array([ 9.05, -9.04,  8.09, -5.67,  5.4 , -3.2 , -0.67, -1.7 , -2.66,
           8.66, -1.95,  5.56])

find common values between two arrays
-------------------------------------

.. code-block:: python

   X = np.random.randint(0,10,10)
   print(X)
   Y = np.random.randint(0,10,10)
   print(Y)
   print(np.intersect1d(X, Y))
   [0 7 6 1 7 2 0 0 1 0]
   [8 0 5 4 7 2 2 5 7 0]
   [0 2 7]

.. code-block:: python

.. code-block:: python
.. code-block:: python
.. code-block:: python
.. code-block:: python
.. code-block:: python
