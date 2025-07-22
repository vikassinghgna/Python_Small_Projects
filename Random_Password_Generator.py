import random
import string
charvalues = string.ascii_letters + string.digits + string.punctuation
password =""
for i in range(12) :
   password+= random.choice(charvalues)
print("Password is :",password)