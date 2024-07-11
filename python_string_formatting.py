#This code is written using Python
#Topic: Python String Formating

#Example:01

txt=f"Good Morning Old Trafford People\n---End of Ex:01---\n"
print(txt)

#Example:02

price=44
tax=0.02
product_details=f"The product you are willing to buy is only {price+(price*tax)} dollar (TAX inclusive)\n---End of Ex:02---\n"
print(product_details)

#Example:03

print("What is the price?")
price=int(input())
if price < 5:
    Decision=f"Yes you can buy this shit"
elif price < 15:
    Decision=f"Buy but it's not necessary"
elif price < 25:
    Decision=f"Try not to buy"
else:
    Decision=f"Don't even dare to buy this"
    
print(Decision.upper())

#Example:04



