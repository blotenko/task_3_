

if __name__ == '__main__':
    #######################
    value = 12
    new_value  = (value)/2 if value <100 else (value)/(-1)
    print(new_value)
    #######################
    value1 = 122
    new_value1 = 1 if value1 < 100 else 0
    print(new_value1)
    #######################
    value1 = 122
    new_value1 = True if value1 < 100 else False
    print(new_value1)
    #######################
    my_str = "1234567"
    i=-1
    for symbol in my_str:
        i=i+1
        if i%2==0:
            print(symbol)
    #######################
    my_str = "qwer"
    new_str = my_str+my_str if len(my_str)<5 else my_str
    print(new_str)
    #######################
    my_str = "qwer"
    new_str = my_str + (my_str)[::-1] if len(my_str) < 5 else my_str
    print(new_str)

