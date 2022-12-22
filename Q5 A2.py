def isWordPresent(sentence, word):
    s = sentence.split(" ")

    for i in s:

        if (i == word):
            return True
    return False

s = "I don't know my name"
word = "name"

if (isWordPresent(s, word)):
    print("Yes")
else:
    print("No")
