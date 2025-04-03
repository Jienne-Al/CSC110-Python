'''Write a program that accepts some language as input from the user -
a phrase, a quote, a poem - and prints out the average word length for that input. For example>

user input = “All the news that’s fit to print”

program output = “The average word length equals 3.71 characters’’

Your output should not be simply the number 3.71 alone, that will not
earn full credit. Print out a complete sentence as shown.
Round your answer to two (2) decimal places.'''

phrase = input("Give me  phrase, a quote, a poem")
words=phrase.split()

total_characters = 0
for word in words:
    total_characters += len(word)

average_length = total_characters / len(words)

print(f"The average word length equals {average_length:.2f} characters.")

