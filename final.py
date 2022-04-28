import sys
import os
import turtle

BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600

def setup():
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(300, 300, 0, 0)
    screen = turtle.getscreen()
    screen.delay(delay=0)
    screen.setworldcoordinates(-300, -300, 300, 300)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    # pointer.done()
    return pointer

def read_star_information(filename):
    data = open(filename, "r")
    lines = data.readlines()

    dataset = []

    for line in lines:
        data = line.split(",")

        x = data[0]
        y = data[1]
        z = data[2]
        id1 = data[3]
        mag = data[4]
        id2 = data[5]
        names = data[-1]

        dataset.append([float(x), float(y), float(mag), names])

    print("Shape of the dataset", len(dataset), len(dataset[0]))

    dict_names = dict()

    for data in dataset:
        x = data[0]
        y = data[1]
        mag = data[2]
        names = data[3]

        names = names.split(";")
        for name in names:
            if name[-1] == "\n":
                name = name[:-1]
            dict_names[name] = [float(x), float(y), float(mag)]

    return dataset, dict_names

def draw_axis():
    # x
    t.goto(-300, 0)
    t.down()
    t.color("blue")
    # turtle.color("red")
    # t.dot(25, "red")
    # t.forward(600)
    t.goto(300, 0)
    # t.dot(25, "red")
    t.up()

    # y
    t.goto(0, 300)
    t.down()
    t.color("blue")
    t.goto(0, -300)
    t.up()

def draw_stars(star_data, plotNames=False):
    for data in star_data:
        x = data[0]
        y = data[1]
        mag = data[2]
        names = data[3]

        xx = x*300
        yy = y*300
        diam = 10/(mag+2)

        t.up()
        t.goto(xx, yy)
        if names[0] == "\n":
            print("... ... ... ... Grey")
            t.color("grey")
        else: 
            t.color("white")
        if plotNames:
            t.write(names.split(";")[0], font=("Arial", 5, "normal"))
        t.dot(diam, "white")

def get_edge_list(constellation_file_name):
    pair_list = open(constellation_file_name, "r")
    pairs = pair_list.readlines()

    edge_pair_list = []

    for a_pair in pairs:
        print(a_pair)
        kk = a_pair.split(",")
        if (len(kk) == 1): 
            constellation_name = kk[0]
            continue
        init, ender = kk
        if ender[-1] == "\n":
            ender = ender[:-1]
        edge_pair_list.append([init, ender])

    return constellation_name, edge_pair_list

def draw_constellation(constellation_name, edge_pair_list, star_dict, color):
    for a_pair in edge_pair_list:
        x1, y1, m1 = star_dict[a_pair[0]]
        x2, y2, m2 = star_dict[a_pair[1]]
    
        t.goto(x1*300, y1*300)
        t.down()
        t.color(color)
        t.goto(x2*300, y2*300)
        t.up()

if __name__ == '__main__':
    arg_list = sys.argv

    writeNames = False

    constellation_files = list()

    if len(arg_list) == 1:
        # python CPSC231F21A3Hudson.py
        print("Enter Star Location filename:", end="")
        stars_location_file = input()
        while (not os.path.isfile(stars_location_file)):
           print("No file exists like this. Please enter again.")
           print("Enter Star Location filename:", end="")
           stars_location_file = input()   

        while True:
            print("Enter constellation filename:", end="")
            a_constellation_file = input()
            if a_constellation_file == "": break
            while (not os.path.isfile(a_constellation_file)):
                print("No file exists like this. Please enter again.")
                print("Enter constellation filename:", end="")
                a_constellation_file = input()
            constellation_files.append(a_constellation_file)

    elif len(arg_list) == 2 and arg_list[1] == "-names":
        # python CPSC231F21A3Hudson.py -names
        print("Enter Star Location filename:", end="")
        stars_location_file = input()
        while (not os.path.isfile(stars_location_file)):
           print("No file exists like this. Please enter again.")
           print("Enter Star Location filename:", end="")
           stars_location_file = input()

        writeNames = True

        while True:
            print("Enter constellation filename:", end="")
            a_constellation_file = input()
            if a_constellation_file == "": break
            while (not os.path.isfile(a_constellation_file)):
                print("No file exists like this. Please enter again.")
                print("Enter constellation filename:", end="")
                a_constellation_file = input()
            constellation_files.append(a_constellation_file)

    elif len(arg_list) == 2:
        # python CPSC231F21A3Hudson.py <arg1>
        stars_location_file = arg_list[1]
        if (not os.path.isfile(stars_location_file)):
            sys.exit(1)

        while True:
            print("Enter constellation filename:", end="")
            a_constellation_file = input()
            if a_constellation_file == "": break
            while (not os.path.isfile(a_constellation_file)):
                print("No file exists like this. Please enter again.")
                print("Enter constellation filename:", end="")
                a_constellation_file = input()
            constellation_files.append(a_constellation_file)

    elif len(arg_list) == 3 and arg_list[2] == "-names":
        # python CPSC231F21A3Hudson.py <arg1> -names
        stars_location_file = arg_list[1]
        if (not os.path.isfile(stars_location_file)):
            sys.exit(1)

        writeNames = True

        while True:
            print("Enter constellation filename:", end="")
            a_constellation_file = input()
            if a_constellation_file == "": break
            while (not os.path.isfile(a_constellation_file)):
                print("No file exists like this. Please enter again.")
                print("Enter constellation filename:", end="")
                a_constellation_file = input()
            constellation_files.append(a_constellation_file)

    elif len(arg_list) == 3 and arg_list[1] == "-names":
        # python CPSC231F21A3Hudson.py -names <arg2>
        stars_location_file = arg_list[2]
        if (not os.path.isfile(stars_location_file)):
            sys.exit(1)

        writeNames = True

        while True:
            print("Enter constellation filename:", end="")
            a_constellation_file = input()
            if a_constellation_file == "": break
            while (not os.path.isfile(a_constellation_file)):
                print("No file exists like this. Please enter again.")
                print("Enter constellation filename:", end="")
                a_constellation_file = input()
            constellation_files.append(a_constellation_file)

    else:
        print("Exitting")
        exit(1) 

    print(stars_location_file)
    print(constellation_files)
    print(writeNames)

    star_data, star_dict = read_star_information(stars_location_file)
    print("STAR_DATA", star_data)
    print("STAR_DICT", star_dict)

    pointer = setup()
    t = pointer.Turtle()

    draw_axis()

    draw_stars(star_data, writeNames)

    colors = ["red", "green", "yellow"]
    color_index = 0

    for constellation_file in constellation_files:
        constellation_name, edge_pair_list = get_edge_list(constellation_file)
        print("CN, EPL\n", constellation_name, edge_pair_list)
        draw_constellation(constellation_name, edge_pair_list, star_dict, colors[color_index])
        color_index = (color_index+1)%3

    pointer.done()