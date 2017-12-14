#Problem 3a
def first_word(sentence):
    word = ""
    i = 0
    while(i < len(sentence) and sentence[i] != " "):
        word += sentence[i]
        i += 1
        #print(word)
    return word

#first_word("fox")
#first_word("the quick brown fox") # ==> the

#Problem 3b
def remove_first_word(sentence):
    front = len(first_word(sentence)) + 1
    back = sentence[front:]
    #print(back)
    return back

#remove_first_word("the quick brown fox") # ==> quick brown fox

#Problem 3c
def sentence_flipper(sentence):
    newSentence = ""
    while(sentence != ""):
        newSentence = first_word(sentence) + " " + newSentence
        sentence = remove_first_word(sentence)
        print(sentence)
        print(newSentence)
    return newSentence

#Problem 3d
def main():
    sentence = input("Please enter a phrase: ")
    print(sentence_flipper(sentence))

main()

