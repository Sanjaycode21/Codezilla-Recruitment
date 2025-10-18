a = input("Enter a word: ")
l = []
# THIS PROGRAM USES LOOP TO REVERSE THE ENTERED STRING
# I ALSO WANNA MENTION THAT THIS CAN ALSO BE DONE USING a[::-1] WITHOUT USING BUILTIN FUNCTIONS
# THIS PROGRAM USES A FOR LOOP TO REVERSE, SINCE IT WAS MENTIONED IN THE QUESTION
for i in a:
    l.append(i)
print("Reversed word is: ",end = '')
for i in range(-1,-len(l)-1,-1):
    print(l[i], end = '')