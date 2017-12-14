#Problem 2

n = input("Please enter a sentence: ")
def shout(sentence):
    sentence = sentence.upper() + "!!!"
    return sentence

print(shout(n))