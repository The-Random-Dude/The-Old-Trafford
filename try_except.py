#This code is written using Python
#Topic: Python String Formating

#Example:01

try:
    print(f)
except:
    print("An Error Occurred")
finally:
    print("Dont worry, even though it's an error Im still printing what is in this 'finally' braket \n--THE END OF THIS EX:01--\n")


#Example:01
#now let's dive into smth. harder
#It's about openning and closing a file regardless it opens or not

try:
    with open("ronaldo.txt", "w")as f:
        try:
            f.write("Yahoo! The file is working")
        except:
            print("File successfully opened but can't write")
except:
    print("We couldn't open the file\n--THE END OF EX:02--\n")
    
    
'''
This example 02 is OK but here is an optimized version of it. I am yet to cover this topic. Maybe later I'll come back to study it. Till then it's here---

try:
    with open("ronaldo.txt", "w") as f:
        f.write("Yahoo! The file is working")
except IOError as e:
    print(f"Error writing to file: {e}")
except Exception as e:
    print(f"Error: {e}")
else:
    print("File write successful")
'''
    
    
    
    
    
    
        