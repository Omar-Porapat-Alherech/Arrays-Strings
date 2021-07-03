# Counts the # of strings, calculates the length of the final array, and works backwards
# to avoid the issue of overwriting something you may need later w/o another variable
def URLify(input_str):
    input_str = input_str.strip()
    input_str_len = len(input_str)
    num_spaces = input_str.count(" ")
    future_len =  input_str_len + num_spaces * 2
    input_str_list = [None] * future_len
    # " " -> "%20" means adding two indices per space found 1 + 2  = 3
    for item in range(0, input_str_len):
        input_str_list[item] = input_str[item]

    for index in range(input_str_len - 1, -1, -1):
        if input_str_list[index] != " ":
            input_str_list[future_len-1] = input_str_list[index]
            future_len -= 1
        else:
            input_str_list[future_len-1] = '0'
            input_str_list[future_len-2] = '2'
            input_str_list[future_len-3] = '%'
            future_len -= 3
    return input_str_list


if __name__ == '__main__':
    result = URLify(input_str="Mr John Smith    ")
    print(''.join([str(ele) for ele in result]))
