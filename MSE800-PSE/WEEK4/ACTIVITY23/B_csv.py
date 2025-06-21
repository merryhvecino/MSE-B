# Open the file in read mode
with open('ACTIVITY23\sample_text.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list

    # Print first and last line if file is not empty
    if lines:
        print("First line:", lines[0].strip())
        print("Last line:", lines[-1].strip())
    else:
        print("The file is empty.")