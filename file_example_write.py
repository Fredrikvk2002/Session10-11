with open("journal.txt", "w") as journal:
    while True:  # Start a loop
        text = input("Enter a journal entry: (press q to quit): ")
        if text == "q":
            break  # Exit loop if "q" is entered
        journal.write(text.capitalize() + "\n")  # Write to file