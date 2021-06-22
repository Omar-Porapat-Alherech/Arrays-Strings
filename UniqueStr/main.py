from Poralib


# Brute force solution o(n^2) For every element we iterate through the array again n * n = o(n^2)
# This assumes uppercase and lowercase values are the same 'A' == 'a' = true
# Assumption that the string contains only letters therefore if len(str) > 27 -> A letter must have been used
# more than once, and therefore is a repeat.
def is_string_unique(input_string):
    input_string = input_string.lower()
    if len(input_string) > 27:
        return False
    for letter_1 in range(0, len(input_string) - 1):
        for letter_2 in range(letter_1 + 1, len(input_string)):
            if input_string[letter_1] == input_string[letter_2]:
                return False
    return True


# Using built in python function alternative
# This assumes uppercase and lowercase values are the same 'A' == 'a' = true
# Assumption that the string contains only letters
# set removes duplicates, if the original string is the same size as the set
def is_string_unique_python_ds(input_string):
    if len(input_string) > 27:
        return False
    input_string = input_string.lower()
    return len(input_string) == len(set(input_string))


def is_string_unique_bitmap(input_string):
    bitmap = int(0)
    for letter in input_string:
        bin_val = ord(letter) - ord('a')
        if (bitmap & (1 << bin_val)) > 0:
            return False
        bitmap |= (1 << bin_val)
    return True


# TODO Complete sort_and_search implementation.
def is_string_unique_sort_and_search(input_string):
    return


if __name__ == '__main__':
    result = is_string_unique('abcde')
    print(result)
    result = is_string_unique_python_ds('abaababab')
    print(result)
    result = is_string_unique_bitmap('abcde')
    print(result)
