#This fucntion will check for the length of the input
def greater(digit):
    length = len(digit)
    
    #checking fo the length
    while length > 4:
        #Getting the user input as a string then coverting it into a list
        digit = list(input("Input a number with digits less than or equal to 4 : "))
        length = len(digit) #Getting the length of the input list
    
    #returning the results    
    return digit,length


#checking the input for constraints
def inputVal(digit):
    digit,length = greater(digit) #Sending the input to check whether its lager than 4 or not

    #checking whether the input is equallent to the digit range constraint
    while True:  
        trueCount = 0 
        
        #Will loop the input and increase the trueCount depending whether the condition is true or false
        for y in digit:
            if y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' :
                trueCount += 1
  
        #If the trueCount is equal to the length of the input digit, this will break the loop and return the results        
        if trueCount == length:
            break
        
        #if trueCount is not equal to length, get the input again and send for length verification
        else:
            digit = list(input("Input a number with digits less than or equal to 4 : "))
            digit,length = greater(digit)
    
    #returning the results
    return digit,length


#Relavant array creation function
def getArray(s):
    #selection of the array to be sent
    if s == '2':
        set1 = ["a","b","c"] #Array being created
        return set1
    
    elif s == '3':
        set2 = ["d","e","f"]#Array being created
        return set2
    
    elif s == '4':
        set3 = ["g","h","i"]#Array being created
        return set3
    
    elif s == '5':
        set4 = ["j","k","l"]#Array being created
        return set4
    
    elif s == '6':
        set5 = ["m","n","o"]#Array being created
        return set5
    
    elif s == '7':
        set6 = ["p","q","r","s"]#Array being created
        return set6
     
    elif s == '8':
        set7 = ["t","u","v"]#Array being created
        return set7
    
    else:
        set8 = ["w","x","y","z"]#Array being created
        return set8


#The letter sorting function
def sorter(array,len,arrIndex):
    listA = [] #declaring the list to store the final output
    len -= 1
    
    #recursive loop to sort and store the elements
    for x in getArray(array[arrIndex]):
        
        #base case
        if len == 0:
            listA.append(x)

        #recursive relation
        else:
            listB = sorter(array,len,arrIndex+1)
            for p in listB:
                listA.append(x + p)
        
    return listA #returning the produced list

#Main program
arrIndex = 0 #variable declaration

#Getting the user input as a string then coverting it into a list
digit = list(input("Input a number with digits less than or equal to 4 : "))
length = len(digit) #Getting the length of the input list

#Checking for empty inputs
if length == 0:
    print(digit)

else:
    digit,length = inputVal(digit) #getting the input validated according to constraints
    print(sorter(digit,length,arrIndex)) #Displaying the results

#########################################        
########## End of the program ###########
#########################################
########## Amaal Edirisinghe ############
#########################################
#########################################
########## Y2S2 - Cyber_Sec  ############
#########################################
