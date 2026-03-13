Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... import random
... while True:
...     input("press Enter to roll the dice")
...     number = random.randint(1,6)
...     print("you got:",number)
...     choice = input("Roll again? (y/n): ")
...     if choice.lower() !="y":
...         break
... 
...     
... press Enter to roll the dice6
... '6'
... you got: 2
