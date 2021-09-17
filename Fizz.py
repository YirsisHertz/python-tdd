def fizzbuzz(value):
    if value % 15 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return value

if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))


    print(fizzbuzz("c"))
