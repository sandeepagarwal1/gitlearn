age=24
age2=4
age3=5
age4=5

# define a function named count_vowels
def count_vowels(string):
    # initialize a variable to store the vowel count
    vowel_count = 0
    # loop through each character in the string
    for char in string:
        # check if the character is a vowel
        if char.lower() in "aeiou":
            # increment the vowel count by one
            vowel_count += 1
    # return the vowel count
    return vowel_count

# call the function with different values of string
print(count_vowels("hello")) # prints 2
print(count_vowels("python")) # prints 1

