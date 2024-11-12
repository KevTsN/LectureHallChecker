# Lecture Hall Checker

This Python script checks what classes are happening inside Carleton University's lecture halls at the time the script runs. <br>
Download the **monthly** iCalendar files from the lecture halls you would like to use, then add them to the ScheduleFiles folder.<br>
[Link to lecture hall schedules](https://booking.carleton.ca/index.php?p=RoomSearch&r=1) <br>

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
*Favourites.txt* is a text file that holds one of your favourite courses on each line. These courses will show "FAVOURITE" abvoe them when the program runs if they are shown.<br>
Run *python checkSchedules.py fav* in your terminal, and you will be shown your current favourite courses (from *Favourites.txt*). You will then be prompted to add new favourites, which will be added to Favourites.txt. The program will then run as normal, listing current courses/times.

### Viewing next lecture:
Run *python checkSchedules.py next* in your terminal, and the program will print out the next class that will happen in the lecture hall, in addition to the current one happening.

>The system arguments "next" and "fav" can both be used at the same time.