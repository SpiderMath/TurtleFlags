from time import sleep
import turtle
import flags


red = "\x1b[91m"
green = "\x1b[92m"
yellow = "\x1b[93m"
blue = "\x1b[94m"
reset = "\x1b[0m"
# Not sure why I'll need a traffic signal but hey!
list_of_supported_countries = ["indonesia", "ukraine", "poland", "russia", "romania", "chad", "france", "ireland", "colombia", "estonia"]


print(f"{blue}Hello there 👋")
print(f"{blue}A {yellow}🔥 warm 🔥{blue} welcome to {green}🐢 Turtle Flags {reset}!")
country_input = input(f"{yellow}Please enter the country's flag you want to see: {red}").lower()
if not country_input in list_of_supported_countries:
	print("Given country not supported / doesn't exist")
	exit()


height = input(f"{yellow}Please enter the height of the flag (Optional): {red}").replace(" ", "")

if len(height) == 0:
	height = None
else:
	try:
		height = int(height)
	except:
		print(f"Invalid height provided. Please provide a number as the height, else do not (default value = 100)")
		exit()


# Some stuff I gotta define
pen = turtle.Turtle()
turtle.Screen().colormode(255)
turtle.bgcolor((0, 0, 0))

if country_input == "ukraine":
	flags.ukraine(pen, height)
elif country_input == "indonesia":
	flags.indonesia(pen, height)
elif country_input == "poland":
	flags.poland(pen, height)
elif country_input == "russia":
	flags.russia(pen, height)
elif country_input == "romania":
	flags.romania(pen, height)
elif country_input == "chad":
	flags.chad(pen, height)
elif country_input == "france":
	flags.france(pen, height)
elif country_input == "ireland":
	flags.ireland(pen, height)
elif country_input == "colombia":
	flags.colombia(pen, height)
elif country_input == "estonia":
	flags.estonia(pen, height)

# Finishing stuff
pen.hideturtle()
turtle.done()