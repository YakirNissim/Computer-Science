import math


class PrimeFactorization(object):
    num = None
    prime_factorization_arr = []

    @classmethod
    def factorization(cls, data):
        if data > 2:
            cls.num = data
            cls.prime_factorization_arr = [True if i > 1 else False for i in range(data + 1)]
            cls.prime_numbers()
            if cls.prime_factorization_arr[data]:
                return f"{cls.num } is prime number!"
            string_return = f"the factorization is:\n {cls.num} = "
            for i in range(cls.num - 1):
                if cls.prime_factorization_arr[i] and data % i == 0:
                    pwer = 0
                    while data % i == 0:
                        pwer += 1
                        data = data / i
                    string_return += f"{i}^{pwer}"
                    if data < 2:
                        break
                    string_return += " * "
            return string_return

        else:
            return "The input you entered is incorrect!"

    @classmethod
    def prime_numbers(cls):
        sqrt_num = int(math.sqrt(cls.num))
        if math.sqrt(cls.num) > sqrt_num:
            sqrt_num += 1
        for prime in range(2, sqrt_num+1):
            if cls.prime_factorization_arr[prime]:
                for i in range(2*prime, cls.num+1, prime):
                    cls.prime_factorization_arr[i] = False


def main():  # test
    num = int(input("please enter number\nnum = "))
    print(PrimeFactorization.factorization(num))
    return 0


if __name__ == '__main__':
    main()
