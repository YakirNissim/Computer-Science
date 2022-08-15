import math


class GCD(object):

    @staticmethod
    def gcd(x, y):  # if GCD(x, y) = 1 then x and y  are relatively prime integers!
        if x < 0 or y < 0:
            print("Do not enter negative numbers!")
            return None
        else:
            if x > y:
                m = x
                n = y
            else:
                m = y
                n = x
            while n > 0:
                old_n = n
                n = m % n
                m = old_n
            return m


def main():  # test
    print("Please enter two integers to get their GCD")
    num1 = int(input("num1 = "))
    num2 = int(input("num2 = "))
    print(f"GCD({num1}, {num2}) = {GCD.gcd(num1, num2)}")
    return 0


if __name__ == '__main__':
    main()
