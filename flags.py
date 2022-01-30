from turtle import Turtle


# ------- Ukraine -------
def ukraine(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Drawing the blue rectangle
	pen.color(0, 87, 183)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width / 2)

	pen.end_fill()

	# Drawing the yellow rectangle
	pen.color(255, 221, 0)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width / 2)

	pen.end_fill()


# ------- Indonesia -------
def indonesia(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Drawing the red rectangle
	pen.color(239, 51, 60)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width / 2)

	pen.end_fill()

	# Drawing the white rectangle
	pen.color(255, 255, 255)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width / 2)

	pen.end_fill()


# ------- Poland -------
def poland(pen: Turtle, height: int):
	if not height: height = 500
	width = int(1.6 * height)

	# Drawing the white rectangle
	pen.color(255, 255, 255)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width / 2)

	pen.end_fill()

	# Drawing the red rectangle
	pen.color(210, 39, 48)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width / 2)

	pen.end_fill()


# ------- Russia -------
def russia(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	pen.up()
	pen.goto(width / 2, height / 2)
	pen.down()

	# Drawing red rectangle
	pen.color(228, 24, 28)
	pen.begin_fill()

	pen.right(180)
	pen.forward(width)
	pen.left(90)
	pen.forward(height)
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height)

	pen.end_fill()

	# Drawing the blue rectangle
	pen.color(28, 53, 120)
	pen.begin_fill()

	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height * (2 / 3))
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height * (2 / 3))

	pen.end_fill()

	# Drawing the white rectangle
	pen.color(255, 255, 255)
	pen.begin_fill()

	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height / 3)
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height / 3)

	pen.end_fill()


# ------- Romania -------
def romania(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height
	blue = (0, 43, 127)
	red = (206, 17, 38)
	yellow = (252, 209, 22)

	# Setting up
	pen.up()
	pen.goto(width / 2, height / 2)
	pen.down()

	# Drawing the blue rectangle
	pen.color(blue)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width)

	pen.end_fill()

	# Drawing the yellow rectangle
	pen.color(yellow)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width * (2 / 3))
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width * (2 / 3))

	pen.end_fill()

	# Drawing the red rectangle
	pen.color(red)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)

	pen.end_fill()


# ------- Chad -------
def chad(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	pen.up()
	pen.goto(-1 * (width / 6), height / 2)
	pen.down()

	# Drawing blue rectangle
	pen.color(0, 38, 100)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)

	pen.end_fill()

	# Drawing the yellow rectangle
	pen.color(254, 203, 0)
	pen.begin_fill()

	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)

	pen.end_fill()

	# Drawing the red rectangle
	pen.up()
	pen.goto(width / 6, height / 2)
	pen.down()

	pen.color(198, 12, 48)
	pen.begin_fill()

	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)

	pen.end_fill()


# ------- France -------
def france(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Setting up
	pen.up()
	pen.goto(-1 * (width / 6), height / 2)
	pen.down()

	# Drawing blue rectangle
	pen.color(0, 35, 149)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)

	pen.end_fill()

	# Drawing the white rectangle
	pen.color(255, 255, 255)
	pen.begin_fill()

	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)

	pen.end_fill()

	# Drawing the red rectangle
	pen.up()
	pen.goto(width / 6, height / 2)
	pen.down()

	pen.color(237, 41, 57)
	pen.begin_fill()

	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)

	pen.end_fill()


# ------- Ireland -------
def ireland(pen: Turtle, height: int):
	if not height: height = 400
	width = 2 * height

	# Setting up
	pen.up()
	pen.goto(-1 * (width / 6), height / 2)
	pen.down()

	# Drawing green rectangle
	pen.color(0, 154, 68)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)

	pen.end_fill()

	# Drawing the white rectangle
	pen.color(255, 255, 255)
	pen.begin_fill()

	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)

	pen.end_fill()

	# Drawing the orange rectangle
	pen.up()
	pen.goto(width / 6, height / 2)
	pen.down()

	pen.color(255, 130, 0)
	pen.begin_fill()

	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width / 3)
	pen.right(90)
	pen.forward(height)

	pen.end_fill()


# ------- Colombia -------
def colombia(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Drawing the yellow rectangle
	pen.color(255, 205, 0)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width)
	pen.left(90)
	pen.forward(height / 2)
	pen.left(90)
	pen.forward(width / 2)

	pen.end_fill()

	# Drawing the red rectangle
	pen.color(200, 16, 46)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 2)
	pen.right(90)
	pen.forward(width / 2)

	pen.end_fill()

	# Drawing the blue rectangle
	pen.color(0, 48, 135)
	pen.begin_fill()

	pen.forward(width / 2)
	pen.right(90)
	pen.forward(height / 4)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 4)
	pen.right(90)
	pen.forward(width / 2)

	pen.end_fill()