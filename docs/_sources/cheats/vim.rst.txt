***
vim
***

search replace
==============

visual mode replace
-------------------

.. code-block:: vim

   change_me::
   # ctrl-v to select change_me::
   # then hit ':' to enter command
   # \%V = last visual selection
   %s/\%Vchange_me/changed/g



copy pasting
============

using mark
----------

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

.. note:: specify lines relative to the current position with +n and -n

- yank range lines into register x `:[range]y[ank] [x]`
- the entire buffer `:%yank`


.. code-block:: bash

   # range from cursor -> +5 lines
   .,+5
   :+2y      " two lines after the current line
   :-2y      " two lines before the current line
   :-2,+2y   " two lines before the cursor and two lines after
   :.,+3     " yank current line and the next 3
   :-3,.yank " current line and the previous 3
   :4yank    " copy line 4

   :4t.      " copy line 4 to below current position
   :4t-      " copy line 4 to 1 line above
   :-27,-26y " copy the line at -27 lines current position


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

change case
-----------

.. code-block:: vim

   ctrl-v + u
   # lowercase line
   guu
   # lowercase text in that direction
   gu[motion]
   # uppercase with U
   guU
   gU[motion]
   # all lowercase
   ggguG
   # gg = goto 1st line, g=(action)start converting from here, till G = end of file

   # toggle case with ~
   g~[motion]

vimrc file
==========

setting up plugins
------------------

.. code-block:: bash


