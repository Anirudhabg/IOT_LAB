# 3 ->  Word and character count of a given string
inputStr=input("Enter a String: ")

wordCnt = len(inputStr.split())
charCnt = len(inputStr)

print("Word Count: ",wordCnt,"\nCharacter Count: ",charCnt)