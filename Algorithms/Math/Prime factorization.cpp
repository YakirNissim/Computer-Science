#include <iostream>
#include <math.h>

using namespace std;

int input_and_check(string print_text);
void prime_numbers(int prime_numbers_arr[], int num);
void prime_factorization(int prime_factorization_arr[], int num);

int main() {
	int num = 0;
	num = input_and_check("please enter number");
	int* prime_factorization_arr;
	prime_factorization_arr = (int*)malloc((num + 1) * sizeof(int));
	if (prime_factorization_arr == NULL)
		return 1;
	prime_factorization(prime_factorization_arr, num);
	cout << endl;
	return 1;
}

int input_and_check(string print_text) {
	int x = -1;
	cout << print_text << endl;
	cin >> x;
	while (!cin.good() || x < 2) {
		cout << "The input you entered is incorrect!" << endl << "Please try again" << endl;
		cin.clear();
		cin.ignore(INT_MAX, '\n');
		cin >> x;
	}
	return x;
}

void prime_numbers(int prime_numbers_arr[], int num) {
	int sqrt_num = (sqrt(num) + 0.5);
	for (int i = 0; i < num+1; ++i) prime_numbers_arr[i] = 1;
	prime_numbers_arr[0] = prime_numbers_arr[1] = 0;
	
	for (int prime = 2; prime <= sqrt_num; ++prime) {
		if (prime_numbers_arr[prime])
			for (int i = 2 * prime; i <= num; i += prime) prime_numbers_arr[i] = 0;
	}
}

void prime_factorization(int prime_factorization_arr[], int num) {
	int temp = num;
	prime_numbers(prime_factorization_arr, num);
	if (prime_factorization_arr[num]) {cout << num << " is prime number"; return;}
	cout << "the factorization is" << endl << num << " = ";
	for (int i = 0; i <= num; ++i)
		if (prime_factorization_arr[i] && temp % i == 0) {
			int pwer = 0;
			while (temp % i == 0) { ++pwer; temp = temp / i; }
			cout << i << '^' << pwer;
			if (temp < 2) break;
			cout << " * ";
		}

}