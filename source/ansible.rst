#######
ansible
#######

************
installation
************

.. graphviz::

     digraph example {
         a [label="sphinx", href="https://sphinx-doc.org", target="_top"];
         b [label="other"];
         a -> b;
     }

prepwork
========

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible-with-pip

environments
------------

.. code-block:: bash
  
   # go to desired conda environment
   conda activate base

   # create a pip environment to admin servers
   mkvirtualenv srvmgmt
   workon srvmgmt

   # doublecheck pip you are using
   pip --version
   pip 20.0.2 from /home/dadude/venv/srvmgmt/lib/python3.8/site-packages/pip (python 3.8)

   # upgrade pip
   pip3 install --upgrade pip


install packages
----------------

.. code-block:: bash
  
   pip install ansible
   # Successfully installed MarkupSafe-2.0.1 PyYAML-5.4.1 ansible-4.0.0 ansible-core-2.11.1
   # cffi-1.14.5 cryptography-3.4.7 jinja2-3.0.1 packaging-20.9 pycparser-2.20
   # pyparsing-2.4.7 resolvelib-0.5.4

   pip install ansible-lint

post install
------------

.. code-block:: bash

   ansible all -m ping --ask-pass
   pip install argcomplete

   # Installing bash completion script ~/.bash_completion.d/python-argcomplete
   $(which activate-global-python-argcomplete) --user

   # or sudo $(which activate-global-python-argcomplete)
   # for system wide config in /etc/bash_completion.d/python-argcomplete

configuration
=============

If you installed Ansible from pip or from source, you may want to create this file in order to override default settings in Ansible

.. code-block:: bash

   # curl -O [filename] <url>
   # use -L or --location to follow a redirect
   # https://github.com/ansible/ansible/blob/devel/examples/ansible.cfg
   curl -O https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg

   (srvmgmt) (becode) dadude@dahost ~/.ansible


hosts
-----

https://github.com/ansible/ansible/blob/devel/examples/hosts.yaml


host groups
^^^^^^^^^^^

.. code-block:: yaml

   all:
     hosts:
         green.example.com:
             ansible_ssh_host: 191.168.100.32
             anyvariable: value
         blue.example.com:
         192.168.100.1:
         192.168.100.10:


   webservers:
     hosts:
        alpha.example.org:
        beta.example.org:
        192.168.1.100:
        192.168.1.110:
     vars:
       http_port: 8080


   # webservers host group = also part of testing & other (gamma3)
   # hosts in child group inherits aal vars from parent
   # testing group contains:
   # gamma1.example.org gamma2.example.org gamma3.example.org
   # www001.example.com www002.example.com www003.example.com
   # www004.example.com www005.example.com www006.example.com
   webservers:
     hosts:
       gamma1.example.org:
       gamma2.example.org:
   testing:
     hosts:
       www[001:006].example.com:
     vars:
       testing1: value1
     children:
       webservers:
   other:
     children:
       webservers:
         gamma3.example.org

error handling
==============

https://docs.ansible.com/ansible/latest/user_guide/playbooks_error_handling.html#controlling-what-defines-failure

