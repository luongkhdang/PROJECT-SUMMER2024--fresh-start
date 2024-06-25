"""

dictionary
    emojy

"""

emojis = {
    ":)" : " emoji smiling",
    ":(" : "emoji sading"

}



message = input(">")
words = message.split(" ")

print(words)
output = ""
for word in words:
    output += emojis.get(word, word)

print(output)