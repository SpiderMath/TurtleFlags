from turtle import Turtle


# ------- Ukraine -------
def ukraine(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Colors
	blue = (0, 87, 183)
	yellow = (255, 221, 0)

	# Drawing the blue rectangle
	pen.color(blue)
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
	pen.color(yellow)
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

	# Colors
	red = (239, 51, 60)
	white = (255, 255, 255)

	# Drawing the red rectangle
	pen.color(red)
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
	pen.color(white)
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
	width = 1.6 * height

	# Colors
	white = (255, 255, 255)
	red = (210, 39, 48)

	# Drawing the white rectangle
	pen.color(white)
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
	pen.color(red)
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

	# Colors
	red = (228, 24, 28)
	blue = (28, 53, 120)
	white = (255, 255, 255)

	# Setting up
	pen.up()
	pen.goto(width / 2, height / 2)
	pen.down()

	# Drawing red rectangle
	pen.color(red)
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
	pen.color(blue)
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
	pen.color(white)
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

	# Colors
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

	# Colors
	blue = (0, 38, 100)
	red = (198, 12, 48)
	yellow = (254, 203, 0)

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


# ------- France -------
def france(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Colors
	blue = (0, 35, 149)
	white = (255, 255, 255)
	red = (237, 41, 57)

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

	# Drawing the white rectangle
	pen.color(white)
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


# ------- Ireland -------
def ireland(pen: Turtle, height: int):
	if not height: height = 400
	width = 2 * height

	# Colors
	green = (0, 154, 68)
	white = (255, 255, 255)
	orange = (255, 130, 0)

	# Setting up
	pen.up()
	pen.goto(width / 2, height / 2)
	pen.down()

	# Drawing the green rectangle
	pen.color(green)
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

	# Drawing the white rectangle
	pen.color(white)
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

	# Drawing the orange rectangle
	pen.color(orange)
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


# ------- Colombia -------
def colombia(pen: Turtle, height: int):
	if not height: height = 400
	width = 1.5 * height

	# Colors
	yellow = (255, 205, 0)
	red = (200, 16, 46)
	blue = (0, 48, 135)

	# Drawing the yellow rectangle
	pen.color(yellow)
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
	pen.color(red)
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
	pen.color(blue)
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


# ------- Estonia -------
def estonia(pen: Turtle, height: int):
	if not height: height = 350
	width = (11 / 7) * height

	# Colors
	blue = (0, 114, 206)
	black = (0, 0, 0)
	white = (255, 255, 255)

	# Setting up
	pen.up()
	pen.goto(width / 2, height / 2)
	pen.down()

	# Drawing the white rectangle
	pen.color(white)
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

	# Drawing the black rectangle
	pen.color(black)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height * (2 / 3))
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height * (2 / 3))
	pen.right(90)
	pen.forward(width)

	pen.end_fill()

	# Drawing the blue rectangle
	pen.color(blue)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height / 3)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 3)
	pen.right(90)
	pen.forward(width)

	pen.end_fill()

	# Separating background from flag
	pen.color(white)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height)
	pen.right(90)
	pen.forward(width)


# ------- Lithuania -------
def lithuania(pen: Turtle, height: int):
	if not height: height = 390
	width = (5 / 3) * height

	# Colors
	red = (190, 58, 52)
	green = (4, 106, 56)
	yellow = (255, 184, 28)

	# Setting up
	pen.up()
	pen.goto(width / 2, height / 2)
	pen.down()

	# Drawing the red rectangle
	pen.color(red)
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

	# Drawing the green rectangle
	pen.color(green)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height * (2 / 3))
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height * (2 / 3))
	pen.right(90)
	pen.forward(width)

	pen.end_fill()

	# Drawing the yellow rectangle
	pen.color(yellow)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height / 3)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 3)
	pen.right(90)
	pen.forward(width)

	pen.end_fill()


# ------- Luxembourg -------
def luxembourg(pen: Turtle, height: int):
	if not height: height = 390
	width = (5 / 3) * height

	# Colors
	blue = (81, 173, 218)
	white = (255, 255, 255)
	red = (234, 20, 29)

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

	# Drawing the white rectangle
	pen.color(white)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height * (2 / 3))
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height * (2 / 3))
	pen.right(90)
	pen.forward(width)

	pen.end_fill()

	# Drawing the red rectangle
	pen.color(red)
	pen.begin_fill()

	pen.right(90)
	pen.forward(height / 3)
	pen.right(90)
	pen.forward(width)
	pen.right(90)
	pen.forward(height / 3)
	pen.right(90)
	pen.forward(width)

	pen.end_fill()
