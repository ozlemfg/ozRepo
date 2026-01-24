numbers = []

while True:
	try:
		number = int(input("Enter a number between 1 and 10: "))

		if number == 7:
			print("Game is over!")
			break
		if 1 <= number <= 10 and number:
			numbers.append(number)
			len(numbers)
			continue
		else:
			print("Enter a number between 1 and 10: ")

	except ValueError:
		print("Enter only number")
print(f"Number of entered valid numbers are: {len(number)}")


