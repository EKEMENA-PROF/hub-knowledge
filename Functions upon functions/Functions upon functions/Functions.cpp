#include <iostream>
#include<string>
#include <vector>
#include <cmath>
using namespace std;
// Pass by Value (Old-Fashioned Function)
void oldFunction(int num) {  // 'num' is a copy of the original variable
    cout << "Inside oldFunction, before modification: " << num << endl;
    num = num * 2;  // Modify the copy
    cout << "Inside oldFunction, after modification: " << num << endl;
}

// Pass by Reference (Modern Function)
void modernFunction(int& num) {  // 'num' is a reference to the original variable
    cout << "Inside modernFunction, before modification: " << num << endl;
    num = num * 2;  // Modify the original variable directly
    cout << "Inside modernFunction, after modification: " << num << endl;
}
// Function to print an array
void printArray(int arr[], int size) {
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}

int main() {

        int value1 = 10;
        int value2 = 10;

        // Demonstrating Pass by Value (Old)
        cout << "Before calling oldFunction: " << value1 << endl;
        oldFunction(value1);
        cout << "After calling oldFunction: " << value1 << " (Unchanged)" << endl << endl;

        // Demonstrating Pass by Reference (Modern)
        cout << "Before calling modernFunction: " << value2 << endl;
        modernFunction(value2);
        cout << "After calling modernFunction: " << value2 << " (Changed)" << endl;
		int practiceArray[] = { 1, 2, 3, 4, 5 };
		printArray(practiceArray, 5);

        
    }




