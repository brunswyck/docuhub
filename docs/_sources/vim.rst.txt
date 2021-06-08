###
vim
###

*************
tips n tricks
*************

copy pasting
============

using mark
----------

.. code-block:: bash

   .. code-block:: bash

   # mark as k
   mk

   # go to end of section you want to copy
   # ' means till (so yank till k mark):
   y'k

   # cut till mark
   d'k

   " is into
   ' is till

"ay'k" means `into a yank till k`

.. note:: **.** means line at cursor position

.. code-block:: bash

   # range from cursor -> +5 lines
   .,+5


copy a block
------------

.. code-block:: bash

   # mark block start x
   mx
   
   # goto end of block
   use move keys
   
   # mark block end y
   my
   
   # move to block start
   `x
   
   # yank up to block end
   y`y
   
   # or cut the block
   d`y


******
.vimrc
******

setting up vim
==============

setting up plugins
------------------

.. code-block:: bash


