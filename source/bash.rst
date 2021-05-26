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

.. code::

   # add before conda initialize!
   
   parse_git_branch() {
       git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'<                                          
   }
   export PS1="\u@\h \[\e[32m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "<  


so git + conda + python
^^^^^^^^^^^^^^^^^^^^^^^

in .bashrc file looks like this

.. code::

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
