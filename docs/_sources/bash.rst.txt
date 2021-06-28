####
bash
####
********
commands
********
grep
====

.. list-table::
   :widths: 10 90
   :header-rows: 1

   * - -h
     - no filename in result
   * - -n
     - linenumbers in result

find
====
examples
--------

.. code-block:: bash

   find . -name \*.php -type f -exec [cmd]
   # find all files, folders, symlinks, etc in the current directory recursively
   # Its filename must end with .php
   # Only search for files (not folders)
   # Execute a command on the results

   find . -name \*.php -type f -exec grep -Hn '$test' {} \+

   find -type f -iname '*.ipynb' -print0 | xargs -0 -n1 -P4 jupyter nbconvert --to markdown


.. code-block:: bash

   find . [args] -exec [cmd] {} \;
   find . [args] -print0 | xargs -0 [cmd]

options
-------

.. list-table::
   :widths: 10 90
   :header-rows: 1

   * - {}
     - placeholder for result of find
   * - \;
     - for each result execute cmd once
   * - \+
     - all **results are concatenated** and cmd is executed once as a parameter (eg for all files found when using grep
   * - -print0 (link to -0)
     - find prints all results to std (each seperated with ASCII NUL char '\000'
   * - -0 (link to -print0)
     - tell xargs the input will be seperated with ASCII NUL char '\000'
   * - -n1
     - tell xargs to execute cmd with only **1 argument** (eg for file found by find) 
   * - xargs -t
     - print each cmd prior to execution
   * - xargs -p
     - print each cmd and ask to execute it (permission)
   * - xargs -x
     - make xargs quit if # of arguments too high for system (see -s)


.. note:: -print0 and -0 are used in tandem. Results are given to xargs as a single string with no newline seperation. NUL char -> used to escape spaces in filenames

apply cmd to results
--------------------
exec
^^^^

.. note::

   - find|xargs will stop at error in piped cmd
   - find -exec returns exit code of find itself instead of subcommand and continues if an error occurs

.. code-block:: bash

   time find . -name \*.php -type f -exec grep -Hn '$test' {} \+

xargs
^^^^^

.. note::

   - use xargs when you want to stop when a cmd fails
   - find | xargs returns exit code of subcommand

.. code-block:: bash

   # -P4 = use 4 xargs processes for parallel execution
   find -type f -iname '*.ipynb' -print0 | xargs -0 -n1 -P4 jupyter nbconvert --to markdown

.. note::

   It depends on the subcommand whether you have to use \; for find and -n1 for xargs. If the subcommand is able to use multiple inputs, then use + and no -n1. If the subcommand can only take one argument, you have to use \; and -n1

*************
bashrc config
*************

prompt customs
==============

git
---

.. code-block:: bash

   # add before conda initialize!
   
   parse_git_branch() {
       git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'<                                          
   }
   export PS1="\u@\h \[\e[32m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "<  


so git + conda + python
^^^^^^^^^^^^^^^^^^^^^^^

in .bashrc file looks like this


.. code-block:: bash

   parse_git_branch() {
       git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
   }
   export PS1="\u@\h \[\e[32m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "
   # >>> conda initialize >>>
   # !! Contents within this block are managed by 'conda init' !!
   __conda_setup="$('/home/dadude/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
   if [ $? -eq 0 ]; then
       eval "$__conda_setup"
   else
       if [ -f "/home/dadude/anaconda3/etc/profile.d/conda.sh" ]; then
           . "/home/dadude/anaconda3/etc/profile.d/conda.sh"
       else
           export PATH="/home/dadude/anaconda3/bin:$PATH"
       fi
   fi
   unset __conda_setup
   # <<< conda initialize <<<
   #Virtualenvwrapper settings:
   export WORKON_HOME=$HOME/venv
   VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
   source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

*********
scripting
*********

examples
========

.. literalinclude:: code/bash/download_pdf.sh

file test operators
===================

http://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Conditional-Constructs

check file exists
-----------------

.. code-block:: bash

   FILE=/etc/docker
   if [ -f "$FILE" ]; then
       echo "$FILE does not exist."
   fi

   [ -d /etc/docker ] && echo "$FILE is a directory"


check multiple files
--------------------

.. code-block:: bash

   [ ! -f /etc/docker ] && echo "$FILE does not exist"
   
   if [ -f /etc/resolv.conf -a -f /etc/hosts ]; then
       echo "Both files exist."
   fi

   if [[ -f /etc/resolv.conf && -f /etc/hosts ]]; then
    echo "Both files exist."
   fi

   [ -f /etc/resolv.conf -a -f /etc/hosts ] && echo "Both files exist."

   [[ -f /etc/resolv.conf && -f /etc/hosts ]] && echo "Both files exist."


-b
 True if the FILE exists and is a special block file
-c
 True if the FILE exists and is a special character file.
-d
 True if the FILE exists and is a directory.
-e
 True if the FILE exists and is a file, regardless of type (node, directory, socket, etc)
-f
 True if the FILE exists and is a regular file (not a directory or device).
-G
 True if the FILE exists and has the same group as the user running the command.
-h
 True if the FILE exists and is a symbolic link.
-g
 True if the FILE exists and has set-group-id (sgid) flag set.
-k
 True if the FILE exists and has a sticky bit flag set.
-L
 True if the FILE exists and is a symbolic link.
-O
 True if the FILE exists and is owned by the user running the command.
-p
 True if the FILE exists and is a pipe.
-r
 True if the FILE exists and is readable.
-S
 True if the FILE exists and is a socket.
-s
 True if the FILE exists and has nonzero size.
-u
 True if the FILE exists, and set-user-id (suid) flag is set.
-w
 True if the FILE exists and is writable.
-x
 True if the FILE exists and is executable

loops
=====

conditional exit with break
---------------------------

.. code-block:: bash

   for I in 1 2 3 4 5
   do
     statements1      #Executed for all values of ''I'', up to a disaster-condition if any
     statements2
     if (disaster-condition)
     then
       break             #Abandon the loop
     fi
     statements3      #While good and, no disaster-condition
   done

   #!/bin/bash
   for file in /etc/*
   do
     if [ "${file}" == "/etc/resolv.conf" ]
     then
       countNameservers=$(grep -c nameserver /etc/resolv.conf)
       echo "Total  ${countNameservers} nameservers defined in ${file}"
       break
     fi
   done


make backup of all file names specified on command line. If .bak file exists, it will skip the cp command

.. code-block:: bash

   for I in 1 2 3 4 5
   do
     statements1      #Executed for all values of ''I'', up to a disaster-condition if any.
     statements2
     if (condition)
     then
       continue   #Go to next iteration of I in the loop and skip statements3
     fi
     statements3
   done
   
   #!/bin/bash
   FILES="$@"
   for f in $FILES
   do
           # if .bak backup file exists, read next file
       if [ -f ${f}.bak ]
       then
           echo "Skiping $f file..."
           continue  # read next file and skip the cp command
       fi
           # we are here means no backup file exists, just use cp command to copy file
       /bin/cp $f $f.bak
   done

for loop with array elements
----------------------------

.. code-block:: bash

   DB_AWS_ZONE=('us-east-2a' 'us-west-1a' 'eu-central-1a')

   for zone in "${DB_AWS_ZONE[@]}"
   do
     echo "Creating rds (DB) server in $zone, please wait ..."
     aws rds create-db-instance \
     --availability-zone "$zone"
     --allocated-storage 20 --db-instance-class db.m1.small \
     --db-instance-identifier test-instance \
     --engine mariadb \
     --master-username my_user_name \
     --master-user-password my_password_here
   done

loop with a shell variable
--------------------------

store important data in the shell variable, and we can use for a loop as follows to read the data:

.. code-block:: bash

   _admin_ip="202.54.1.33|MUM_VPN_GATEWAY 23.1.2.3|DEL_VPN_GATEWAY 13.1.2.3|SG_VPN_GATEWAY"
   for e in $_admin_ip
   do
      ufw allow from "${e%%|*}" to any port 22 proto tcp comment 'Open SSH port for ${e##*|}'
   done


loop with a number using range
------------------------------

.. code-block:: bash

   for i in {START..END}
   do
      commands
   done
   ## step value ##
   for i in {START..END..STEP}
   do
      commands
   done
   ## example: ping cbz01, cbz02, cbz03, and cbz04 using a loop ##
   for i in 0{1..4}
   do
       h="cbz${i}"
       ping -c 1 -q "$h" &>/dev/null 
       if [ $? -eq 0 ]
       then
           echo "server $h alive" 
       else
           echo "server $h dead or can not ping."
       fi
   done


loop with strings
-----------------

.. code-block:: bash

   PKGS="python-openssl  python3-aioopenssl  rsyslog-openssl"
   for p in $PKGS
   do
      echo "Installing $p package"
      sudo apk add "$p"
   done

.. code-block:: bash
.. code-block:: bash
.. code-block:: bash
.. code-block:: bash
.. code-block:: bash
.. code-block:: bash
.. code-block:: bash
