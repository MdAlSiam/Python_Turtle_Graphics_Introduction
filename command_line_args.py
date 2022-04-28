import sys
import os

n = len(sys.argv)
print("Total arguments passed:", n)

arg_list = sys.argv

for i in range(0, n):
    print(arg_list[i], end = "|")

writeNames = False

constellation_files = list()
if len(arg_list) == 1:
    # 1
    print("Enter the stars-location-file:", end=" ")
    stars_location_file = input() # From the same folder
    # while not os.path.isfile(stars_location_file):
    #     print("No file exists like this. Please enter again.")
        

    while True:
        a_constellation_file = input()
        if a_constellation_file == "": break
        constellation_files.append(a_constellation_file)

elif len(arg_list) == 2 and arg_list[1] == "-names":
    # 2
    print("Enter the stars-location-file:", end=" ")
    stars_location_file = input() # From the same folder

    writeNames = True

    while True:
        a_constellation_file = input()
        if a_constellation_file == "": break
        constellation_files.append(a_constellation_file)

elif len(arg_list) == 2:
    # 3
    stars_location_file = arg_list[1]

    while True:
        a_constellation_file = input()
        if a_constellation_file == "": break
        constellation_files.append(a_constellation_file)

elif len(arg_list) == 3 and arg_list[2] == "-names":
    # 4
    stars_location_file = arg_list[1]

    writeNames = True

    while True:
        a_constellation_file = input()
        if a_constellation_file == "": break
        constellation_files.append(a_constellation_file)

elif len(arg_list) == 3 and arg_list[1] == "-names":
    # 5
    writeNames = True

    stars_location_file = arg_list[2]

    while True:
        a_constellation_file = input()
        if a_constellation_file == "": break
        constellation_files.append(a_constellation_file)

else:
    exit(1) 


    