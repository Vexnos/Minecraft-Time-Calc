'''

    MinecraftTime.py

    Author: Vexnos
    Date: 2023-08-28

    Minecraft Time Calculator

'''
#-------Functions-------
def timeCalc(n, a):
    result = a * n + (a - 1) * (24000 - n)
    return result

#-------Main-Routine-------
if __name__ == "__main__":
    looping = True
    while looping:

        validating_time = True
        validating_rotations = True

        print('''
            #1 = Full Moon
            #2 = Waining Gibbous Moon
            #3 = Last Quarter Moon
            #4 = Waining Crescent Moon
            #5 = New Moon
            #6 = Waxing Crescent Moon
            #7 = First Quarter Moon
            #8 = Waxing Gibbous Moon
            #9 = Full Moon
        ''')

        # Validate the time
        while validating_time:

            # Attempt
            try:
                time = int(input("Enter your desired time (in ticks): "))

            # Failure
            except ValueError:
                print("Invalid value entered, please try again")
                continue

            # Success
            validating_time = False

        # Validate the rotations
        while validating_rotations:

            # Attempt
            try:
                rotations = int(input("\nEnter the amount of planetary rotations: "))

            # Failure
            except ValueError:
                print("Invalid value entered, please try again")
                continue

            # Success
            validating_rotations = False

        # Run the Calulator Function and Print the result
        result = timeCalc(time, rotations)
        print(f"\n{result}")

        loop_again = input("\nLoop again? (y/n): ")
        looping = loop_again.lower().startswith("y")