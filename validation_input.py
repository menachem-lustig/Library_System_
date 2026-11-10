def valid_int(text):
    valid_num = False
    while not valid_num:
        try:
            num = int(input(text))
            if num >= 1:
                 valid_num = num
            else:
                print('The number must be positive.')
        except ValueError:
            print('Must be a number')
    return valid_num


def valid_str(text):
    valid_str = False
    while not valid_str:
        string = input(text).strip()
        if string:
            valid_str = string
        else:
            print('string cannot be empty')
    return valid_str

