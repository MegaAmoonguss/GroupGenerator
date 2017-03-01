import os
import random

def main():
	try:
		with open("Classes/" + input("Enter block: ").upper() + ".txt") as file:
			students = [name.rstrip() for name in file.readlines() if not name.startswith('#')]
	except:
		print("Invalid block.")
		print("\nPress any key to exit...")
		input()
		exit()

	num_groups = int(input("Enter the number of groups (" + str(len(students)) + " students): "))
	groups = []

	if num_groups > len(students):
		print("\nPlease enter a number less than or equal to the number of students.")
		print("\nPress any key to exit...")
		input()
		exit()

	for _ in range(num_groups):
		groups.append([])

	random.shuffle(students)

	for i in range(len(students)):
		groups[i % num_groups].append(students[i])

	s = ""
	for i in range(len(groups)):
		s += "Group " + str(i+1) + ": "
		for j in range(len(groups[i])):
			if j == len(groups[i]) - 1:
				s += groups[i][j] + "\n"
			else:
				s += groups[i][j] + ", "

	print("\n" + s)

	choice = input("Would you like to save the groups? (y/n) ")
	if choice == "y":
		worked = save(s)
		while not worked:
			worked = save(s)

	print("\nPress any key to exit...")
	input()

def save(s):
	filename = ""
	while not filename:
		filename = input("Enter a name for the groups: ")
		if not filename:
			print("Name cannot be empty.\n")

	if not os.path.isdir("Groups"):
		os.mkdir("Groups")

	if os.path.isfile("Groups/" + filename + ".txt"):
		override = input("Groups/" + filename + ".txt already exists.\nOverride? (y/n) ")
		if override != "y":
			return False

	try:
		with open("Groups/" + filename + ".txt", "w") as file:
			file.write(s)
	except OSError:
		print("Invalid file name.\n")
		return False
	print("Wrote groups to Groups/" + filename + ".txt.")
	return True

if __name__ == "__main__":
	main()
