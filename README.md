This program is a simulation of an electronic memory game.

I didn't want to complicate the program too much. The important
is that you can play and learn a little more
about Python and ncurses and that you understand the logic.

Note:

- To run the program use Python3
- In Debian, install the "sox" package via apt-get
to be able to reproduce the beeps through the "play"
- play is a command line utility (shell). For
test play directly from the terminal copy and paste the line below:

play --no-show-progress --null -t alsa --channels 1 synth.5 sine 1000