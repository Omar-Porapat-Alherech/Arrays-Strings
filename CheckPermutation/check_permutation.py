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

# TODO Sort + compare
# Space Efficient go through one and decrease dict going through other
if __name__ == '__main__':
    result = check_permutation_brute_force('aacde', 'abcda')
    print(result)
