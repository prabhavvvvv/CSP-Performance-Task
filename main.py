import turtle as trtl
p = trtl.Turtle()

def main(x, y):
    x = -10
    y = 0
    colors = ["red", "blue", "green", "pink", "yellow"]
    print(colors)

    new_color = "purple"
    colors.append(new_color)
    print()

    if len(colors) > 5:
        print("There are enough infinity stones")
    else:
        colors.append("black")

    while True:
        color_chooser = input("What color do you want Thanos's infinity gauntlet to be?: ")
        if color_chooser in colors:
            print("Now drawing a", color_chooser, "Thanos gauntlet")
            break
        else:
            print("Invalid color choice, please try again")

    p.penup()
    p.goto(x, y)
    p.setheading(-90)
    p.pendown()
    p.circle(100, extent = 180)
    p.left(40)
    p.forward(40)
    p.right(40)


main(-100, 0)

wn = trtl.Screen()
wn.mainloop()
