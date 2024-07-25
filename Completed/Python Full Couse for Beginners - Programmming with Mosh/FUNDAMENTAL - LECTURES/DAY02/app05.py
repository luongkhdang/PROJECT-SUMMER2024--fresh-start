"""

dictionary
    emojy

"""

def emoji_reader(message):
    emojis = {
        ":)" : " emoji smiling",
        ":(" : "emoji sading"

    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output



message = input(">")
print(emoji_reader(message))