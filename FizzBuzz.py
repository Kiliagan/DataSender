#FizzBuzz.py by Kiliagan

def fizzbuzz(num):
	output = ''
	if num%3 == 0:
		output+= 'Fizz'
	if num%5 == 0:
		output+= 'Buzz'
	if num%7 == 0:
		output+= 'Dazz'
	if output == '':
		output+= str(num)
	print output
if __name__ == "__main__":
	i = 1
	while i <= 110:
		fizzbuzz(i)
		i+=1