sentence = "This is a common inverview question"


unique = {*sentence}


time = {}
for i in unique:
    time[i] = 0

max1 = [sentence[0], 1]
for index, word in enumerate(sentence):
    time[word] += 1
    if time[word] > max1[1] and word != " ":
        max1 = [word, time[word]]


print(time)
print(max1)
