***
git
***
git log
=======
Revision ranges
---------------

.. code-block:: bash

   git log master             # branch
   git log origin/master      # branch, remote
   git log v1.0.0             # tag

   git log master develop

   git log v2.0..master       # reachable from *master* but not *v2.0*
   git log v2.0...master      # reachable from *master* and *v2.0*, but not both


Basic filters
-------------

.. code-block:: bash

   -n, --max-count=2
       --skip=2

.. code-block:: bash

   --since="1 week ago"
   --until="yesterday"

.. code-block:: bash

   --author="Rico"
   --committer="Rico"

Search
------

.. code-block:: bash

   --grep="Merge pull request"   # in commit messages
   -S"console.log"               # in code
   -G"foo.*"                     # in code (regex)

.. code-block:: bash

   --invert-grep
   --all-match                   # AND in multi --grep

Limiting
--------


.. code-block:: bash

   --merges
   --no-merges

.. code-block:: bash

   --first-parent          # no stuff from merged branches

.. code:: bash

   --branches="feature/*"
   --tags="v*"
   --remotes="origin"

Simplification
--------------

.. code:: bash

   git log -- app/file.rb          # only file
       --simplify-by-decoration    # tags and branches

Ordering
--------

.. code:: bash

   --date-order
   --author-date-order
   --topo-order              # "smart" ordering
   --reverse

Formatting
----------

.. code-block:: bash

   --abbrev-commit
   --oneline
   --graph

Custom formats
--------------

.. code:: bash

   --pretty="format:%H"

