#We are making a program for handling books

name=(input("enter your name: "))
date,month,year=(input("enter today's dd-mm-yy:")).split("-")
day=(input("enter today's day: "))
token=int(input("enter token no: "))
days=int(input("enter number of days you will return book in: "))

genre1=['Think and Grow’, ‘Choose Yourself’, ‘The Alchemist’, ‘Awaken The Giant Within’, ‘The Power of Thinking Big']
genre2=['The Diary Of A Young Girl’, ‘Pride And Prejudice’, ‘The Treasure Island’, ‘Wuthering Heights']

a= genre1
c= genre2
genre=eval(input("enter genre of chosen book: "))
tp=10
quantity=int(input("enter no of books borrowed: "))
booknames=input("enter names of the book: ")
        
while(quantity>0):
    quantity=quantity-1
 
if genre==a and token in range(1,51):
    tokenprice=10*tp
elif genre==c and token in range(51,101):
    tokenprice=20*tp
else:
    print("token no and genre are not right")
 
print()
print("borrower name:",name.upper())
print("the token no is:",token)
print("the genres are:",genre1+genre2)
print("choosen genre and the books name are:",genre,booknames)

if genre==a and token in range(1,51):
    tokenprice=tokenprice+days
    print("date:",date,"-",month,"-",year)
    print("day:",day,"you have to return the book within",days,"days")
    print("the token price for your book is:",tokenprice)
elif genre==c and token in range(51,101):
    tokenprice=tokenprice+days
    print("date:",date,"-",month,"-",year)
    print("day:",day,"you have to return the book within",days,"days")
    print("the token price for your book is:",tokenprice)
print()
print("have a good read :)".upper())
