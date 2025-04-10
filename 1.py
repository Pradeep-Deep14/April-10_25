my_string = ['Love','Hope','Peace','Grace']
#Write a code to return the longest string in the list of strings above
#If there is a tie the  code should return the string with higher index

#using inbuilt function
longest_string = max(reversed(my_string), key=len)
print(longest_string)

#using loop
my_string = ['Love', 'Hope', 'Peace', 'Grace']

# Initialize variables to store the longest string and its length
longest_string = ""
max_length = 0

# Loop through the list from the end to the beginning
for i in range(len(my_string) - 1, -1, -1):
    current_string = my_string[i]
    current_length = len(current_string)
    
    # Update the longest string if the current one is longer
    if current_length > max_length:
        longest_string = current_string
        max_length = current_length

# Print the result
print(longest_string)