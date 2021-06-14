****
tmux
****
session control
===============

.. list-table:: sessions
   :widths: 20 80
   :header-rows: 1

   * - tmux new-session
     - :new # start a new session
   * - tmux new -s becode
     - :new -s becode  # start new session with name becode
   * - tmux kill-ses -t becode
     - tmux kill-session -t becode  # kill/delete session becode
   * - tmux kill-session -a
     - kill/delete all sessions but the current
   * - tmux kill-session -a -t becode
     - kill/delete all sessions but becode
   * - ctrl + b $
     - rename session
   * - ctrl + b d
     - detach from session
   * - attach -d
     - detach others on the session (Maximize window by detach other clients)
   * - tmux ls
     - tmux list-sessions
   * - ctrl + b s
     - show all sessions
   * - tmux attach-session
     - attach to last session
   * - tmux a -t mysession
     - tmux attach -t mysession
   * - tmux attach-session -t mysession
     - attach to a session with the name mysession
   * - ctrl + b (
     - move to previous session
   * - ctrl + b )
     - move to next session


.. list-table:: windows
   :widths: 20 80
   :header-rows: 1

   * - ctrl + b c
     - create window
   * - ctrl + b ,
     - rename current window
   * - ctrl + b &
     - close current window
   * - ctrl + b p
     - previous window
   * - ctrl + b n
     - next window
   * - ctrl + b 0...9
     - switch/select window by number
   * - :swap-window -s 2 -t 1
     - reorder window, swap window 2(src) and 1(dest)
   * - :swap-window -t -1
     - move current window to the left by one position


.. list-table:: panes
   :widths: 20 80
   :header-rows: 1

   * - ctrl + b ;
     - toggle last active pane
   * - ctrl + b %
     - split pane vertically
   * - ctrl + b "
     - split pane horizontally
   * - ctrl + b {
     - move the current pane left
   * - ctrl + b }
     - move the current pane right
   * - ctrl + b <up>  Ctrl + b <down>
     - 
   * - ctrl + b <right>  Ctrl + b <left>
     - switch to pane in that direction
   * - ctrl + b q
     - show pane numbers
   * - ctrl + b q 0...9
     - switch/select pane by number
   * - ctrl + b z
     - toggle pane zoom
   * - ctrl + b !
     - convert pane into a window
   * - ctrl + b <up>
     - 
   * - ctrl + b ctrl + <up>
     - 
   * - ctrl + b <down>
     - 
   * - ctrl + b ctrl + <down>
     - resize current pane **height** (holding 2nd key is optional)
   * - ctrl + b <right>
     - 
   * - ctrl + b ctrl + <right>
     - 
   * - ctrl + b <left>
     - 
   * - ctrl + b ctrl + <left>
     - resize current pane **width** (holding 2nd key is optional)
   * - ctrl + b x
     - close current pane


.. list-table:: copy mode
   :widths: 20 80
   :header-rows: 1

   * - setw -g mode-keys vi
     - use vi keys in buffer
   * - ctrl + b [
     - enter copy mode
   * - ctrl + b PgUp
     - enter copy mode and scroll one page up
   * - q
     - quit mode
   * - g
     - go to top line
   * - g
     - go to bottom line
   * - scroll up
     - 
   * - scroll down
     - 
   * - h
     - move cursor left
   * - j
     - move cursor down
   * - k
     - move cursor up
   * - l
     - move cursor right
   * - w
     - move cursor forward one word at a time
   * - b
     - move cursor backward one word at a time
   * - /
     - search forward
   * - ?
     - search backward
   * - n
     - next keyword occurance
   * - n
     - previous keyword occurance
   * - spacebar
     - start selection
   * - esc
     - clear selection
   * - enter
     - copy selection
   * - ctrl + b ]
     - paste contents of buffer_0
   * - :show-buffer
     - display buffer_0 contents
   * - :capture-pane
     - copy entire visible contents of pane to a buffer
   * - :list-buffers
     - show all buffers
   * - :choose-buffer
     - show all buffers and paste selected
   * - :save-buffer buf.txt
     - save buffer contents to buf.txt
   * - :delete-buffer -b 1
     - delete buffer_1

.. list-table:: other
   :widths: 20 80
   :header-rows: 1

   * - ctrl + b :
     - enter command mode
   * - :set -g OPTION
     - set option for all sessions
   * - :setw -g OPTION
     - set option for all windows
   * - tmux info
     - show every session, window, pane, etc...
   * - ctrl + b ?
     - show shortcuts

.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash


.. code-block:: bash

