####
bash
####

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


