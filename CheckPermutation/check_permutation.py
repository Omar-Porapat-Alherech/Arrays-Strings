# Brute force solution using dictionary, both strings -> dictionary with frequency
# Check if both dicts are the same
def check_permutation_brute_force(string_a, string_b):
    if len(string_a) == len(string_b):
        str_dict_a = {}
        str_dict_b = {}
        for letter in string_a:
            if letter in str_dict_a.keys():
                str_dict_a[letter] += 1
            else:
                str_dict_a[letter] = 1
        for letter in string_b:
            if letter in str_dict_b.keys():
                str_dict_b[letter] += 1
            else:
                str_dict_b[letter] = 1
        if str_dict_a == str_dict_b:
            return True
    return False


# Sort the strings them compare, if they are permutations they will be equal
def check_permutation_sort_comp(string_a, string_b):
    if len(string_a) == len(string_b):
        string_a = sorted(string_a)
        string_b = sorted(string_b)
        if string_a == string_b:
            return True
    return False


# Space Efficient go through one and decrease dict going through other
# Similar to the brute force except with one dict, can exit early if a value is about to go negative
def check_permutation_one_dict(string_a, string_b):
    if len(string_a) == len(string_b):
        str_dict = {}
        for letter in string_a:
            if letter in str_dict:
                str_dict[letter] += 1
            else:
                str_dict[letter] = 1
        for letter in string_b:
            if letter in str_dict:
                if str_dict[letter] == 0:
                    return False
                else:
                    str_dict[letter] -= 1
                    if str_dict[letter] == 0:
                        str_dict.pop(letter)
            else:
                return False
        return True
    return False


if __name__ == '__main__':
    result = check_permutation_brute_force('aacde', 'abcda')
    print(result)
    result = check_permutation_brute_force('aacde', 'abda')
    print(result)
    result = check_permutation_one_dict('bcdaa', 'bbaad')
    print(result)
    result = check_permutation_sort_comp('bcdaa', 'bdaac')
    print(result)
