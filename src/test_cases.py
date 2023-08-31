import random
import string


# n = 10
# # print(n)
# for i in range(n):
# 	print (random.randint(100000,100000000))
# print(".")


# n = 30
# word = [*'asdfghjkl']
#
# lowercase_letters = [*string.ascii_letters[:26]]
# special_characters = [*" ,.?!_-"]
# other_letters = [letter for letter in lowercase_letters if letter not in word]
# # print(other_letters)
#
# sum = 0
# for i in range(n):
# 	all_letters = []
# 	just_from_word = random.randint(0, 1)
# 	just_from_word = 0
# 	sum+=just_from_word
# 	letters = random.randint(2, len(word))
# 	for l in word[:letters]:
# 		for j in range(random.randint(1, 3)):
# 			all_letters.append(l if j%2==0 else l.upper())
# 	if just_from_word == 0:
# 		letters = random.randint(2, len(other_letters))
# 		for l in other_letters[:letters]:
# 			for j in range(random.randint(1, 3)):
# 				all_letters.append(l if j%2==0 else l.upper())
# 	letters = random.randint(2, len(special_characters))
# 	for l in special_characters:
# 		for j in range(random.randint(1, 3)):
# 			all_letters.append(l)
# 	random.shuffle(all_letters)
# 	print ("".join(all_letters))
# print("#")
# print(sum)


def is_valid_move(m, n, i, j):
	return 0 <= i < m and 0 <= j < n


def next_move(row, column, command):
	if command == 'Z':
		row += 1
		column -= 1
	elif command == 'X':
		row += 1
	elif command == 'C':
		column += 1
		row += 1
	elif command == 'A':
		column -= 1
	elif command == 'D':
		column += 1
	elif command == 'Q':
		row -= 1
		column -= 1
	elif command == 'W':
		row -= 1
	elif command == 'E':
		row -= 1
		column += 1

	return row, column


m = 4
n = 6
print(m)
print(n)
allowed_commands = ['Z', 'X', 'C', 'A', 'D', 'Q', 'W', 'E']
for i in range(m):
	row = []
	for j in range(n):
		row.append(str(random.randint(1, 10)))
	print(" ".join(row))

row = random.randint(0, m - 1)
col = random.randint(0, n - 1)

print (f"{row} {col}")

cmds = 10
final_commands = []

for i in range(cmds):
	command = random.choice(allowed_commands)
	row1,col1 = next_move(row,col,command)
	# while not is_valid_move(m,n,row,col):
	# 	command = random.choice(allowed_commands)
	# 	row1, col1 = next_move(row, col, command)
	row = row1
	col = col1
	final_commands.append(str(command))

print("".join(final_commands))

