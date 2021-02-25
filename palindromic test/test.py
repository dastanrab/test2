# Python program for the above approach

# Function to return true if
# S[i...j] is a palindrome
def isPalindrome(S, i, j):
# Iterate until i < j
while (i < j):
	# If unequal character encountered
	if (S[i] != S[j]):
	return False
	i += 1
	j -= 1

# Otherwise
return True

# Function to find for every index,
# longest palindromic substrings
# starting or ending at that index
def printLongestPalindrome(S, N):
# Stores the maximum palindromic
# substring length for each index
palLength = [0 for i in range(N)]

# Traverse the string
for i in range(N):
	# Stores the maximum length
	# of palindromic substring
	maxlength = 1

	# Consider that palindromic
	# substring ends at index i
	for j in range(i):
	# If current character is
	# a valid starting index
	if (S[j] == S[i]):
		# If S[i, j] is palindrome,
		if (isPalindrome(S, j, i)):
		# Update the length of
		# the longest palindrome
		maxlength = i - j + 1
		break

	# Consider that palindromic
	# substring starts at index i
	j = N-1
	while(j > i):
	# If current character is
	# a valid ending index
	if (S[j] == S[i]):
		# If str[i, j] is palindrome
		if (isPalindrome(S, i, j)):
		# Update the length of
		# the longest palindrome
		maxlength = max(j - i + 1, maxlength)
		break
	j -= 1

	# Update length of the longest
	# palindromic substring for index i
	palLength[i] = maxlength

# Print the length of the
# longest palindromic substring
for i in range(N):
	print(palLength[i],end = " ")

# Driver Code
if __name__ == '__main__':
S = "bababa"
N = len(S)
printLongestPalindrome(S, N)

# This code is contributed by SURENDRA_GANGWAR.
