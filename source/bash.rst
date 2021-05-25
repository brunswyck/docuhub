####
bash
####

************
bash customs
************

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


virtualenv
----------

documentation `virtualenvwrapper`_

.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

install
.. code::

   sudo apt-get install virtualenvwrapper


add to bashrc once virtualenvwrapper is installed

.. code::

   #Virtualenvwrapper settings:
   export WORKON_HOME=$HOME/venv
   VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
   source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
   
   (base) dadude@dahost ~/gits/docuhub (main)$ source ~/.bashrc
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/premkproject
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/postmkproject
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/initialize
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/premkvirtualenv
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/postmkvirtualenv
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/prermvirtualenv
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/postrmvirtualenv
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/predeactivate
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/postdeactivate
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/preactivate
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/postactivate
   virtualenvwrapper.user_scripts creating /home/dadude/.venvs/get_env_details


workon will work now

.. code::

   (base) dadude@dahost ~/gits/docuhub (main)$ workon 
   code
   deleteme
   desktop
   docu
   docuhub
   jupyter
   networking
   otp_client
   portfolio
   pytest
   testing_mocks
   
   (docu) (helloworld) dadude@dahost ~/gits/docuhub (main)$ workon docuhub
   (docuhub) (helloworld) dadude@dahost ~/gits/docuhub (main)$ 


.. code::

   mkvirtualenv new_venv_name
   lsvirtualenv
   rmvirtualenv name_of_your_env
   cpvirtualenv old_virtual_env new_virtual_env

