import csv

print("")
print("NOW MAIN TASK STARTS")
print("")

with open("vo.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for Ts, FS, LS, ES, CS, CN, events in reader:
        def creator(FS, LS, ES, CS, CN, events):
            if events != "":
                if events.count("Poster") != 0:
                    with open('nsslist/Poster.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Bingo") != 0:
                    with open('nsslist/Bingo.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Kavyanjali") != 0:
                    with open('nsslist/Kavyanjali.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Step") != 0:
                    with open('nsslist/Step.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])
                if events.count("Act") != 0:
                    with open('nsslist/Act.csv', 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                        filewriter.writerow([FS, LS, ES, CS, CN])


        if FS != "":
            creator(FS, LS, ES, CS, CN, events)

print("")
print("TASK SUCCESSFULLY COMPLETED")
