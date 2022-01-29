from time import sleep
import turtle
import flags


red = "\x1b[91m"
green = "\x1b[92m"
yellow = "\x1b[93m"
blue = "\x1b[94m"
reset = "\x1b[0m"
# Not sure why I'll need a traffic signal but hey!
list_of_supported_countries = ["indonesia", "ukraine"]


print(f"{blue}Hello there 👋")
print(f"{blue}A {yellow}🔥 warm 🔥{blue} welcome to {green}🐢 Turtle Flags {reset}!")
country_input = input(f"{yellow}Please enter the country's flag you want to see: {red}").lower()
if not country_input in list_of_supported_countries:
	print("Given country not supported / doesn't exist")
	exit()


unit = input(f"{yellow}Please enter the base unit of the flag (Optional): {red}").replace(" ", "")

if len(unit) == 0:
	unit = 200
else:
	try:
		unit = int(unit)
	except:
		print(f"Invalid unit provided. Please provide a number as the unit, else do not (default value = 100)")
		exit()


# Some stuff I gotta define
flag = turtle.Turtle()
turtle.Screen().colormode(255)
turtle.bgcolor("black")

if country_input == "ukraine":
	flags.ukraine(flag, unit)
elif country_input == "indonesia":
	flags.indonesia(flag, unit)


turtle.done()