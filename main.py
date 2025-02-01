

def main():
	print('--- Start Report ---')
	
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
		get_words(file_contents)

		char_counts = get_char_counts(file_contents)
		print_char_counts(char_counts)
	
	print('--- End Report ---')

def get_words(body):
	print(len(body.split()))

def get_char_counts(body):
	char_counts = {}
	for c in body.lower():
		if c not in char_counts:
			char_counts[c] = 1
		else:
			char_counts[c] += 1

	return char_counts	

def print_char_counts(char_counts):
	alpha_chars = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for char in char_counts:
		if char in alpha_chars:
			print(f"The '{char}' character was found {char_counts[char]} times")

main()
