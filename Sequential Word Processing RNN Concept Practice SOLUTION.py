# Programming Exercise 8-1: Sequential Word Processing Solution

# Ask the user for a sentence
sentence = input()

# Split the sentence into individual words
words = sentence.split()

# This variable will store the running "memory"
memory = ""

# Loop through the words one at a time
for i in range(len(words)):
    # Update the memory by adding the current word
    if memory == "":
        memory = words[i]
    else:
        memory = memory + " " + words[i]
    
    # Print the step number and the current memory
    print(f"Step {i+1}: {memory}")
