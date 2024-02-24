command = input('Type Help > ')

while not command.lower() == "quit":
    command = input("""Type 'Start'--To Start The Car
Type 'Stop'--To Stop The Car
Type 'quit'--To Exit
>""")
    if command.lower() == "start":
        print("Car Started...Ready To Go.")
    elif command.lower() == "stop":
        print("Car Stopped...")
    else:
        if not command.lower() == 'quit':
            print("I don't Understand.")
