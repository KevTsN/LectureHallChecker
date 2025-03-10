# Lecture Hall Checker

### Attention: as of February 11, 2025, Carleton's room schedule site (and the .ics files) no longer shows course or time details, effectively making this useless. 😥

This Python script checks what classes are happening inside Carleton University's lecture halls at the time the script runs. <br>
Download the **monthly** iCalendar files from the lecture halls you would like to use, then add them to the ScheduleFiles folder.<br>
These files are named by Carleton's building and room code (i.e. AB 000 or AB 0000), which is crucial to correctly displaying lecture hall code names.<br>
Merged classes will show two classes in the terminal, each with separate course codes.<br>


## Necessary Installations:
>**PiP is required**

If you don't have PiP in your environment, : <br>
Download *get-pip.py* from [Bootstrap get-pip.py](https://bootstrap.pypa.io/get-pip.py)<br>
Run "*python get-pip.py*"<br>
<r>
After that runs, run "*pip install -r requirements.txt*" in your environment terminal.

### Running the program:
Run *python checkSchedules.py* in your terminal.

### Setting Favourites:
*Favourites.txt* is a text file that holds one of your favourite courses on each line. These courses will show "FAVOURITE" above them when the program runs if they are shown.<br>
Run *python checkSchedules.py fav* in your terminal, and you will be shown your current favourite courses (from *Favourites.txt*). You will then be prompted to add new favourites, which will be added to Favourites.txt. The program will then run as normal, listing current courses/times.

### Viewing next lecture:
Run *python checkSchedules.py next* in your terminal, and the program will print out the next class that will happen in the lecture hall, in addition to the current one happening.

To view only the next class happening, run *python checkSchedules.py nextOnly*. If you run both nextOnly and next, it will only show the next class, with the former argument overriding the latter's usual behaviour.

>The system arguments "next", "nextOnly" and "fav" can all be used at the same time.
