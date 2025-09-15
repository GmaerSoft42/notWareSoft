# TypeTest v1

Flask application that is a simple typing test. Type as much words in 60 seconds. ~~Make sure to not do any mistakes because a goblin might spawn out of the program and steal all your passwords (jk)~~

I know the words.json file is a terrible selection, currently trying to find a better one. Let me know if you have any suggestions.

## MODULES REQUIRED:

1/ `flask`

2/ For MAIN.PY (command line version), `msvcrt`

## How to INSTALL and RUN

You can use the convenient NSIS installer in this folder named TYPE.EXE, or you can download every single file (if you do this make sure that the directory structure is the same as in this repo or you may encounter serious typing errors!).

To RUN the program, use the `WEBSITERUN.BAT` file or type `flask --app webmain.py run` at the command line (make sure to change directory to make sure your command line is in the same directory as the program. If you don't want to change directory, you must specify the full file path. The format must be full (all directories up to the base directory, like / or C:\)with the drive name included if the program file is not in the same directory as your current command line.)

Then go to any convenient browser and go to 127.0.0.1:5000 or [click here!](http://127.0.0.1:5000)
