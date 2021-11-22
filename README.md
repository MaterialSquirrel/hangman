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

<h2>PLAY .EXE ON WINDOWS</h2>

To play the game on a Windows machine, go to 'dist' and run the .exe
file. This was built using pyinstaller.

<h2>PLAY .PY FROM COMMAND PROMPT</h2>

You must have Python installed. To check if it is installed on your
machine, open a command prompt and write "python". If you have it installed,
you will get a message informing you of which version. If version 2 or older,
update at python.org.

<h3>WINDOWS:</h3>
Go to your Windows logo and type in "cmd", then write the following commands:

&gt;&gt; cd Downloads<br />
&gt;&gt; cd Hangman Game<br />
&gt;&gt; python hangman.py<br />

This also may work:

&gt;&gt; cd Downloads<br />
&gt;&gt; cd Hangman Game<br />
&gt;&gt; hangman.py<br />

<h3>MAC:</h3>
Go to Applications > Utilities > Terminal and follow the instructions above.

Have fun!!

(I coded everything, except the dictionary and ASCII art are from Github.)

<h2>A note about the /misc folder:</h2>

Two files in this section were used to change .txt files into .py files.
Originally I had called the .txt files from the program, but then when I
compiled a single executable using pyinstaller, the .exe program would not
function if the .txt files were missing. Having only .py files produces
a much cleaner, single executable.

Using 'dictionary_read.py', I converted a 'dictionary.txt' to
'dictionary.json'. I did it this way in order to automate the creation of
a properly syntaxed list. I then pasted that list into a file
called 'dictionary.py'.

Using 'build_hangmans.py', I converted 7 different .txt files to
7 different .json outputs, each containing a string. I did it this
way in order to properly capture all the characters and whitespace.
I then pasted each one together into a dictionary in 'man_art.py'.

I could have left these both in the main hangman.py file, but I left them
separate in an attempt to stay organized.
