def main():
    file_contents = ""

    with open("frankenstein.txt") as f:
        file_contents = f.read()

    characterCount = countCharacters(file_contents)

    printReport(characterCount)

def countWords(text):
    textSplit = text.split()
    return len(textSplit)

def countCharacters(text):
    charCount = dict()

    for char in text:
        if char.lower() not in charCount:
            charCount[char.lower()] = 1
        else: 
            charCount[char.lower()] += 1
    
    return charCount

def printReport(characterCount):
    characterCountSorted = dict(sorted(characterCount.items()))

    charList = list(characterCountSorted.keys())
    countList = list(characterCountSorted.values())

    print("--- Begin report of books/frankenstein.txt ---")

    for i in range(len(charList)):
        if charList[i].isalpha():
            print(f"The '{charList[i]}' character was found {countList[i]} times")

    print("--- End report ---")

main()