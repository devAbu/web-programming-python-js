from functions import square  # we will get an error with importting the function
# from functions - import the entire functions module then use dot notation to access the square function: functions.square(i)

for i in range(10):
    print(f"The square of {i} is {square(i)}")
