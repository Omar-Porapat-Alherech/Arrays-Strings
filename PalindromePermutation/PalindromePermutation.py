def dict_counter(input_str):
    my_dict = {}
    for character in input_str:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1
    return my_dict

# Kinda brute force, loading o(n),  + iterating o(n)
def find_odd_after_counter(input_dict):
    found = False
    for _, value in input_dict.items():
        if value % 2 == 1:
            if (found):
                return False
            found = True
    return found

# Calculate during filling so we don't need to go through the array once while loading and again checming
def find_odd_while_counter(input_dict):
    my_dict = {}
    odd_counter = 0
    for character in input_str:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1
        if my_dict[character] % 2 == 1:
            odd_counter += 1
        else:
            odd_counter -= 1
    return odd_counter <= 1

# Saves Space with bitmap
def bitmap_sol(input_str):
    bitmap = 0
    for letter in input_str:
        index = ord(letter) - ord('a')
        mask = 1 << index
        # Exclusive or, because 2 will cancel out as x % 2 -> 0, and there can only be one letter with odd instances
        bitmap ^= mask
    return bitmap & (bitmap - 1) == 0





if __name__ == '__main__':
    input_str = "Tact Coa".replace(' ', '').lower()
    filled_dict = dict_counter(input_str)
    result = find_odd_after_counter(filled_dict)
    print(result)
    result = find_odd_while_counter(input_str)
    print(result)
    result = bitmap_sol(input_str)
    print(result)
