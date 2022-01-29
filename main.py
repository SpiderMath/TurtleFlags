from time import sleep
import turtle
import flags


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
turtle.Screen().colormode(255)
turtle.bgcolor("black")

if country_input == "ukraine":
	flags.ukraine(flag)
elif country_input == "indonesia":
	flags.indonesia(flag)


turtle.done()