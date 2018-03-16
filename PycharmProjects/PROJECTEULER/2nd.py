""" PROJECT EULER
SECOND PROBLEM
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
 first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.

"""
# function to check for the even fibonacci numbers and return their sum


def even_fibonacci():

    a = 1
    b = 1
    result = 0
    while a < 4000000:
        sum = a + b
        a = b
        b = sum
        if a % 2 == 0:
            result = result + a
    return result


def main():

    print(even_fibonacci())


if __name__ == "__main__":
    main()
