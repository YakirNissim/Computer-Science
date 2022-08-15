#include <iostream>;

using namespace std;

int GCD(int x, int y);
int input_and_check(string print_text);

int main() {
	int x, y;
	cout << "Please enter two integers to get their GCD" << endl;
	x = input_and_check("num1 = ");
	y = input_and_check("num2 = ");
	cout << "GCD(" << x << ", " << y << ") = " << GCD(x, y);
	return 0;
}

int input_and_check(string print_text) {
	int x = -1;
	cout << print_text;
	cin >> x;
	while (!cin.good() || x < 2) {
		cout << "The input you entered is incorrect!" << endl << "Please try again" << endl;
		cin.clear();
		cin.ignore(INT_MAX, '\n');
		cin >> x;
	}
	return x;
}

int GCD(int x, int y) {
	int m, n, old_n;

	if (x > y) {m = x; n = y;} else {m = y; n = x;}

	while (n > 0) {
		old_n = n;
		n = m % n;
		m = old_n;
	}
	return m;
}