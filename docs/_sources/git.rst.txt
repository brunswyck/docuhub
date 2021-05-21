.. highlightlang:: rest
.. using headers 
   ##################
   H1: document title
   ##################
   
   Introduction text.
   
   
   *********
   Sample H2
   *********
   
   Sample content.
   
   
   **********
   Another H2
   **********
   
   Sample H3
   =========
   
   Sample H4
   ---------
   
   Sample H5
   ^^^^^^^^^
   
   Sample H6
   """""""""
   
   And some text.
   


###
GIT
###

*********************
initial configuration
*********************

setup new repo
==============

local to remote
---------------

.. code::

   echo "# demo" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git remote add origin git@github.com:brunswyck/demo.git
   git push -u origin master

user specific
=============

write to global ~/.gitconfig
----------------------------

.. code::

   git config --global user.name "dadude"
   git config --global user.email "dadude@users.noreply.github.com"
   git config --global core.editor "vim"
   git config --list


********
branches
********

remotes
=======

list existing remotes
---------------------

.. code::

   git remote -v


set remote
----------

using https
^^^^^^^^^^^

.. code::

   git remote set-url https://github.com/USERNAME/REPO.git

using SSH
^^^^^^^^^

.. code::

   git remote set-url git@github.com/USERNAME/REPO.git


show remote
-----------

.. code::

   git remote show origin
   * remote origin
      Fetch URL: git@github.com:brunswyck/hellobecode.git
     Push  URL: git@github.com:brunswyck/hellobecode.git
     HEAD branch: main
     Remote branches:
       gh-pages tracked
       main     tracked
     Local branch configured for 'git pull':
       main merges with remote main
     Local ref configured for 'git push':
       main pushes to main (up to date)


id merged branches into current branch (master)
-----------------------------------------------

.. code::

   git remote show origin
















changed gitignore but folder still in commit
--------------------------------------------

you added eg the folder env/ to your .gitignore file but when checking git status you see git still wants to commit all env/lib/... files
You can fix that by removing the folder from cache:

.. code::

   git rm -r --cached bin

force local changes on remote master with no merge
--------------------------------------------------

.. code::
  
   git push -f <remote> <branch>
   git push -f origin master

Force pushing with a "lease" allows the force push to fail if there are new commits on the remote that you didn't expect (technically, if you haven't fetched them into your remote-tracking branch yet), which is useful if you don't want to accidentally overwrite someone else's commits that you didn't even know about yet, and you just want to overwrite your own:

.. code::

   git push <remote> <branch> --force-with-lease

load .gitconfig file
--------------------

.. code::

   git config --local include.path "$PWD/.gitconfig"




