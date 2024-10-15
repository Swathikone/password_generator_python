import random
import string


def generate_password(no_letters,no_int,no_char):
		
	password=(random.choices(string.ascii_letters,k=no_letters)+random.choices(string.digits,k=no_int)+random.choices(string.punctuation,k=no_char))
	random.shuffle(password)
	ans="".join(password)
	return ans

	

#take in no of letters
no_letters=int(input("enter no of letters "))
#take in no of integers
no_int=int(input("enter how many numbers "))
#take in no of special characters
no_char=int(input("enter no of  special characters "))
answer=generate_password(no_letters,no_int,no_char)


print("suggested password : ",answer)
