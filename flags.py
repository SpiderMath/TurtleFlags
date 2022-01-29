from turtle import Turtle


def ukraine(flag: Turtle):
	width = 600
	height = 400
	flag.color("blue")
	flag.begin_fill()

	# Drawing the blue rectangle
	flag.forward(width / 2)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width)
	flag.left(90)
	flag.forward(height / 2)
	flag.left(90)
	flag.forward(width)

	flag.end_fill()

	flag.color("yellow")
	flag.begin_fill()

	# Drawing the yellow rectangle
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width)
	flag.right(90)
	flag.forward(height / 2)
	flag.right(90)
	flag.forward(width)

	flag.end_fill()
