from turtle import Turtle


# ------- Ukraine -------
def ukraine(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Drawing the blue rectangle
	flag.color(0, 87, 183)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width / 2)

	flag.end_fill()

	# Drawing the yellow rectangle
	flag.color(255, 221, 0)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width / 2)

	flag.end_fill()


# ------- Indonesia -------
def indonesia(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Drawing the red rectangle
	flag.color(239, 51, 60)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width / 2)

	flag.end_fill()

	# Drawing the white rectangle
	flag.color(255, 255, 255)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width / 2)

	flag.end_fill()


# ------- Poland -------
def poland(flag: Turtle, height: int):
	if not height: height = 500
	width = int(1.6 * height)

	# Drawing the white rectangle
	flag.color(255, 255, 255)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width / 2)

	flag.end_fill()

	# Drawing the red rectangle
	flag.color(210, 39, 48)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width / 2)

	flag.end_fill()


# ------- Russia -------
def russia(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	flag.up()
	flag.goto(width / 2, height / 2)
	flag.down()

	# Drawing red rectangle
	flag.color(228, 24, 28)
	flag.begin_fill()

	flag.right(180)
	flag.forward(width)
	flag.left(90)
	flag.forward(height)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height)

	flag.end_fill()

	# Drawing the blue rectangle
	flag.color(28, 53, 120)
	flag.begin_fill()

	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height * (2 / 3))
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height * (2 / 3))

	flag.end_fill()

	# Drawing the white rectangle
	flag.color(255, 255, 255)
	flag.begin_fill()

	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 3)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 3)

	flag.end_fill()


# ------- Romania -------
def romania(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	flag.up()
	flag.goto(width / 2, height / 2)
	flag.down()

	# Drawing blue rectangle
	flag.color(0, 43, 127)
	flag.begin_fill()

	flag.right(180)
	flag.forward(width)
	flag.left(90)
	flag.forward(height)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height)

	flag.end_fill()

	# Drawing the yellow rectangle
	flag.color(252, 209, 22)
	flag.begin_fill()

	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height * (2 / 3))
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height * (2 / 3))

	flag.end_fill()

	# Drawing the red rectangle
	flag.color(206, 17, 38)
	flag.begin_fill()

	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 3)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 3)

	flag.end_fill()


# ------- Chad -------
def chad(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	flag.up()
	flag.goto(-1 * (width / 6), height / 2)
	flag.down()

	# Drawing blue rectangle
	flag.color(0, 38, 100)
	flag.begin_fill()

	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)

	flag.end_fill()

	# Drawing the yellow rectangle
	flag.color(254, 203, 0)
	flag.begin_fill()

	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)

	flag.end_fill()

	# Drawing the red rectangle
	flag.up()
	flag.goto(width / 6, height / 2)
	flag.down()

	flag.color(198, 12, 48)
	flag.begin_fill()

	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)

	flag.end_fill()


# ------- France -------
def france(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	flag.up()
	flag.goto(-1 * (width / 6), height / 2)
	flag.down()

	# Drawing blue rectangle
	flag.color(0, 35, 149)
	flag.begin_fill()

	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)

	flag.end_fill()

	# Drawing the white rectangle
	flag.color(255, 255, 255)
	flag.begin_fill()

	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)

	flag.end_fill()

	# Drawing the red rectangle
	flag.up()
	flag.goto(width / 6, height / 2)
	flag.down()

	flag.color(237, 41, 57)
	flag.begin_fill()

	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)

	flag.end_fill()


# ------- Ireland -------
def ireland(flag: Turtle, height: int):
	if not height: height = 400
	width = 2 * height

	# Setting up
	flag.up()
	flag.goto(-1 * (width / 6), height / 2)
	flag.down()

	# Drawing green rectangle
	flag.color(0, 154, 68)
	flag.begin_fill()

	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)

	flag.end_fill()

	# Drawing the white rectangle
	flag.color(255, 255, 255)
	flag.begin_fill()

	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)

	flag.end_fill()

	# Drawing the orange rectangle
	flag.up()
	flag.goto(width / 6, height / 2)
	flag.down()

	flag.color(255, 130, 0)
	flag.begin_fill()

	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)
	flag.right(90)
	flag.forward(width / 3)
	flag.right(90)
	flag.forward(height)

	flag.end_fill()


# ------- Colombia -------
def colombia(flag: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Drawing the yellow rectangle
	flag.color(255, 205, 0)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width / 2)

	flag.end_fill()

	# Drawing the red rectangle
	flag.color(200, 16, 46)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width / 2)

	flag.end_fill()

	# Drawing the blue rectangle
	flag.color(0, 48, 135)
	flag.begin_fill()

	flag.forward(width / 2)
	flag.right(90)
	flag.forward(height / 4)
	flag.right(90)
	flag.forward(width)
	flag.right(90)
	flag.forward(height / 4)
	flag.right(90)
	flag.forward(width / 2)

	flag.end_fill()