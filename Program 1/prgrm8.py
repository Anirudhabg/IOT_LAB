# 8 -> Read a file line by line and print the word count of each line 
with open('info.txt','r') as file:
    index = 1
    for line in file:
        count = 0
        words = line.split()
        count += len(words)
        print("Words at line ",index," is: ",count)
        index += 1