#FizzBuzz.py by Kiliagan

def fizzbuzz(num):
	if num%3 == 0:
		print 'Fizz'
	elif num%5 == 0:
		print 'Buzz'
	else:
		print num

if __name__ == "__main__":
	i = 1
	while i <= 100:
		fizzbuzz(i)
		i+=1