import icalendar
from pathlib import Path
import datetime
import sys
import re


if __name__ == "__main__":
    ics_path = Path("ScheduleFiles/")

    ics_pths = [pth for pth in ics_path.iterdir()
                if pth.suffix == '.ics']

    today = datetime.datetime.now(datetime.timezone.utc)
    #handling favourite courses from Favourites.txt


    favouritesList = []
    ff = open("Favourites.txt", "r+") 

    for fav in ff:
        fav = fav.split('\n', 1)[0]
        favouritesList.insert(len(favouritesList), fav)

    if(len(sys.argv) > 1 and sys.argv[1] == "fav"):
        #inserting favourites before running program
        newFavsList = []
        print("FAVOURITES LIST: ")
        for fav in favouritesList:
            print(fav)
        
        print("Enter in favourite coruse, or type \"q\" or \"quit\" to exit")
        newFav = "";

        while(newFav != "q" and newFav != "quit"):
            newFav= input("Enter favourite course: ")

            if(newFav in favouritesList):
                print("Cannot add duplicate course to favourites\n")
            elif(newFav in ["q", "quit"]): 
                print("Done adding courses\n")
                break
        
            elif (not re.search("^[A-Z]{4}[0-9]{4}$", newFav)):
                print("The course you entered is not in proper Carleton course code format \n")
            else:
                newFavsList.append(newFav)
    

        ff = open("Favourites.txt", "a")

        for nf in newFavsList:
            favouritesList.append(nf);
            ff.write(nf)
            ff.write("\n")
            print("{newf} has been added to favourite courses".format(newf=nf))

    ff.close()

    #ok done 
    favouritesSet = set(favouritesList)
    
    for path in ics_pths:
        with path.open() as f:
            calendar = icalendar.Calendar.from_ical(f.read())

        for event in calendar.walk('VEVENT'):
            startDt = event['DTSTART'].dt
            endDt = event['DTEND'].dt
            if startDt <= today <= endDt:
            
                summary = str(event.get("SUMMARY"))
                summary = summary.split(">", 1)
                toSplit = summary[-1].split("<",1)[0]
                toSplit = toSplit.split("-")
                course = toSplit[-1]

                if(course[-1]=="F" or course[-1]=="W"):
                    course = course.split(" ")[0]
                
                endTime = endDt.time().strftime("%I:%M %p")
                startTime = startDt.time().strftime("%I:%M %p")

                if(course in favouritesSet):
                    print("FAVOURITE");
                
                print("{courseName} is currently in {hallName}".format(courseName=course, hallName = path.stem))
                minStart = int( (today-startDt).total_seconds() / 60 )
                minEnd = int( (endDt - today).total_seconds() / 60)

                print("They started at {fst}, which was {fsm} minutes ago.".format(fst=startTime, fsm = minStart))
                print("They will end at {fet}, which is {fem} minutes from now.\n".format(fet = endTime, fem = minEnd))
                                                                            
                                                                    

