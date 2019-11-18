#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This calculates celsius to fahrenheit


def temperature():
    try:
        # input
        celsius = int(input("What is the Celsius temperature: "))

        # process
        fahrenheit = (celsius * 1.8) + 32

        # output
        print("The temperature in Fahrenheit is " + str(fahrenheit) + "°")
    except ValueError:
        print("Invalid input.")


def main():
    temperature()


if __name__ == "__main__":
    main()
