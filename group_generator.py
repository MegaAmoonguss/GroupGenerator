import random

def main():
	with open('Classes/' + input('Enter block: ').upper() + '.txt') as file:
		students = [name.rstrip() for name in file.readlines() if not name.startswith('#')]

	print('Enter the number of groups (' + str(len(students)) + ' students):')
	num_groups = int(input())
	groups = []

	if num_groups > len(students):
		print('\nPlease enter a number less than or equal to the number of students.')
		return
		
	for _ in range(num_groups):
		groups.append([])

	random.shuffle(students)

	for i in range(len(students)):
		groups[i % num_groups].append(students[i])
			
	print('\nGroups:')
	for group in groups:
		print(group)
	print('\nPress any key to exit...')
	input()

if __name__ == '__main__':
	main()