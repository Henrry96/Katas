def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        return 
    elif num % 5 == 0:
        print("buzz")
        return 
    elif num % 3 == 0:
        print("fizz")
        return 
    else: print(num)
    return
    raise NotImplementedError
