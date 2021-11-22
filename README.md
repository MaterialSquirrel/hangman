# hangman
Classic hangman command-line game with ASCII art

Hi! This game of Hangman was designed by MaterialSquirrel on GitHub.

Thanks for downloading! This is my first module designed and coded all on my
own (except the ASCII art and dictionary which were adapted from Github).
As a result, the code originally started out pretty messy, but I believe I've
cleaned it up quite nicely!

This game of classic Hangman was coded in Python 3.9.6. This folder contains
a main file, a dictionary file, and a file of the hangman ASCII art. To see how
the second two files were built, look inside the 'misc' folder.

The dictionary for this game contains up to 5000 of the most common words 
in English so that that no confusing words are used. Only words of a certain
minimum length are used, set by default to 6. Players are allowed 6 failures
before game ends.

There are two options to play:

======================================================================

PLAY .EXE ON WINDOWS

======================================================================
To play the game on a Windows machine, you go to 'dist' and run the .exe
file. This was built using pyinstaller.

======================================================================

PLAY .PY FROM COMMAND PROMPT

======================================================================

You must have Python installed. To check if it is installed on your
machine, open a command prompt and write "python". If you have it installed,
you will get a message informing you of which version. If version 2 or older,
update at python.org.

WINDOWS:
Go to your Windows logo and type in "cmd", then write the following commands:

>> cd Downloads
>> cd Hangman Game
>> python hangman.py

This also may work:
>> cd Downloads
>> cd Hangman Game
>> hangman.py

MAC:
Go to Applications > Utilities > Terminal and follow the instructions above.

Have fun!!

(I coded everything, except the dictionary and ASCII art are from Github.)
