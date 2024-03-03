# My reentry into Python
## Introduction
In the first second, I was completly lost only understanding the simple commands
```py
    from turtle import *

    forward(n)
    left(m)
```
When we had to draw the side of a die that shows a five, my inner perfectionist came out and made a mess of a code:
```py
    from turtle import *

    forward(2)
    left(90)
    penup()
    forward(2)
    dot(10)
    right(180)
    forward(2)
    left(90)
    pendown()

    forward(76)
    left(90)

    penup()
    forward(2)
    dot(10)
    right(180)
    forward(2)
    left(90)
    pendown()

    forward(2)
    left(90)
    forward(76)

    penup()
    left(90)
    forward(2)
    dot(10)
    right(180)
    forward(2)
    left(90)
    pendown()

    forward(2)
    left(90)
    forward(76)

    penup()
    left(90)
    forward(2)
    dot(10)
    right(180)
    forward(2)
    left(90)
    pendown()

    forward(2)
    left(90)
    forward(38)

    penup()
    left(90)
    forward(40)
    dot(10)
    right(180)
    forward(40)
    left(90)
    pendown()
    forward(36)

    hideturtle()
```
This code........literally repeats itself 3 times. I'm not quite happy about this code, but I won't bother making it any shorter as that's where my perfectionism ends :)

