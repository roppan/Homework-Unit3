# Initial variable to track game play

play = "y"

# Set start and last number
last_number = 0

# While we are still playing...
while play == "y":
    
    # Ask the user how many numbers to loop through
    x =int (input("How many numbers?"))
    x+=last_number
    

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range (last_number, x):

        # Print each number in the range
        print(f'{last_number}: last_number')
        print(f'{x}: x')
        
    # Set the next start number as the last number of the loop
    last_number = last_number + 1
    
play = input("Continue the chain:(y)es or (n)o? ") 
if play == "n":
    'break'
elif play =="y":
    'continue'
else:

    # Once complete... ask if the user wants to continue

    play = input("Choose y or n! no other option") 
    'continue'