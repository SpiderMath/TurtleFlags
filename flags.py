from turtle import Turtle

# ------- Ukraine -------
def ukraine(flag: Turtle):
	width = 600
	height = 400

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
def indonesia(flag: Turtle):
	width = 600
	height = 400

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
