#Problem 3

def counter(string):
    result = ""
    counter = 0
    for i in range(len(string)-1):
        if(string[i] == "1"):
            if(string[i+1] == "1"):
                counter += 1
            elif(string[i+1] == "0"):
                counter += 1
                result += str(counter) + " 1's \n"
                counter = 0

        elif(string[i] == "0"):
            if(string[i+1] == "0"):
                counter += 1
            if(string[i+1] == "1"):
                counter += 1
                result += str(counter) + " 0's \n"
                counter = 0

    result += str(counter+1) + " " + string[-1] +"'s"
    #print(one_counter,zero_counter)
    print(result)

def main():
    string = input("Please enter a string of 1s and 0s: ")
    counter(string)

main()