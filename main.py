from time import sleep
import turtle


red = "\x1b[91m"
green = "\x1b[92m"
yellow = "\x1b[93m"
blue = "\x1b[94m"
reset = "\x1b[0m"
# Not sure why I'll need a traffic signal but hey!


print(f"{blue}Hello there 👋")
print(f"{blue}A {yellow}🔥 warm 🔥{blue} welcome to {green}🐢 Turtle Flags {reset}!")
country_input = input(f"{yellow}Please enter the country's flag you want to see: {red}").lower()
flag = turtle.Turtle()


if country_input == "ukraine":
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


turtle.done()