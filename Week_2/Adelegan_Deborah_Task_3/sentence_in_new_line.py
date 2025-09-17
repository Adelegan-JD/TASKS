# TASK 12: Ask the user for a sentence and print each word on new line.
sentence = input("Write down a sentence: ")
split_sentence = sentence.split()
print(*split_sentence, sep='\n')
