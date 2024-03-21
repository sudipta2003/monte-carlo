def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    l = len(zip_code)
    count = 0
    if l == 5:
        for i in zip_code:
            if i.isnumeric() == True:
                count += 1
        #print(count)
        if count == 5:
            return True
        else:
            return False
    else:
        return False

print(is_valid_zip("23454"))