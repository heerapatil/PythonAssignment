#11.Write a program that accepts a sentence and calculate the number of letters and digits
s = raw_input("Enter the Sentence")
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]

'''OUTPUT:
Enter the Sentenceheera123LETTERS 5DIGITS 3
'''
