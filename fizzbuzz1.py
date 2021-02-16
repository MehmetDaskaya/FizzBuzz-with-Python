def fizzbuzz(input):
    if input %3 == 0 and input %5 == 0:
        return  "FizzBuzz"
    elif input %5==0:
        return "Buzz"
    elif input %3 ==0:
        return "Fizz"
    return input

print(" FizzBuzz is a primary-school level game.\n You will type a number and if that number can be evenly divided by 3 it will be named Fizz,\n if the number which you have typed can be evenly divided by 5 it will be named Buzz,\n if it can be divided evenly by both 3 and 5 it will be named FizzBuzz.")
number = int(input("Please enter a number according to the rules above.\n"))
print(fizzbuzz(number))
