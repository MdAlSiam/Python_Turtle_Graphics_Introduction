from os import name
import turtle

BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600

def setup():
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(300, 300, 0, 0)
    screen = turtle.getscreen()
    screen.delay(delay=0)
    screen.setworldcoordinates(-300, -300, 300, 300) # https://www.kite.com/python/docs/turtle.setworldcoordinates
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    # pointer.done()
    return pointer

# sc=turtle.Screen()
# sc.setup(800,800)

# for c in ["red", "purple", "orange", "green", "blue"]:
#     t.color(c) # color
#     # t.circle(10)
#     t.dot(10)
#     t.forward(50) # go forward 50 units
#     t.left(144) # turn left by 144 deg

# xs = [-100, -50, 0, 100, -100, 100]
# ys = [-100, 0, 0, 100, 100, -100]

# for i in range(len(xs)):
#     t.up()
#     t.goto(xs[i], ys[i])
#     t.dot(10)

data = open("./stars_named_big_dipper.dat", "r")
lines = data.readlines()

dataset = []

for line in lines:
    data = line.split(",")
    print(data, end = "ok")
    if (data[-1] != "\n"):
        print("Names: ", data[-1], end=" ")

    x = data[0]
    y = data[1]
    z = data[2]
    id1 = data[3]
    mag = data[4]
    id2 = data[5]
    names = data[-1]

    dataset.append([float(x), float(y), float(mag), names])

    print()

pointer = setup()
t = pointer.Turtle()

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

colors = [""]
color_index = 0

for data in dataset:
    print(data)
    x = data[0]
    y = data[1]
    mag = data[2]
    names = data[3]

    xx = x*300
    yy = y*300
    diam = 10/(mag+2)

    t.up()
    t.goto(xx, yy)
    t.color("white")
    t.write(names.split(";")[0], font=("Arial", 5, "normal"))
    t.dot(diam, "white")

pair_list = open("BigDipper-1.dat", "r")
pairs = pair_list.readlines()

for a_pair in pairs:
    print(a_pair)
    kk = a_pair.split(",")
    if (len(kk) == 1): continue
    init, ender = kk
    if (ender[-1] == "\n"): ender = ender[:-1]
    print("START>", init, ender)

    init_pos = [-1, -1]
    end_pos = [-1, -1]

    for data in dataset:
        names = data[3]
        names = names.split(";")
        for name in names:
            if name[-1] == "\n":
                name = name[:-1]
            if name == init:
                init_pos = [data[0], data[1]]
                break
    for data in dataset:   
        names = data[3]
        names = names.split(";")     
        for name in names:
            if name[-1] == "\n":
                name = name[:-1]
            if name == ender:
                end_pos = [data[0], data[1]]
                break
    print(">>", init, ender, init_pos, end_pos)

    t.goto(init_pos[0]*300, init_pos[1]*300)
    t.down()
    t.color("red")
    t.goto(end_pos[0]*300, end_pos[1]*300)
    t.up()

pointer.done()