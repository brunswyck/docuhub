#!/usr/bin/bash
# http://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Conditional-Constructs
FILE="$HOME/.ansible/ansible.cfg"
if test -f "$FILE"; then
  echo "$FILE was found, moving on .."
else
  echo "$FILE was not found!"
fi
