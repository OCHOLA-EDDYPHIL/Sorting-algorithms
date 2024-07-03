#include<iostream> // Include the standard input-output stream library
using namespace std; // Use the standard namespace

// Function to swap the content of two integers
void swapping(int &a, int &b) {
    int temp;
    temp = a;
    a = b;
    b = temp;
}

// Function to perform selection sort on an array
void selectionSort(int *array, int size) {
    int i, j, imin;
    // Loop through each element of the array except the last one
    for(i = 0; i < size-1; i++) {
        imin = i; // Assume the current position is the minimum
        // Find the index of the minimum element in the unsorted portion
        for(j = i+1; j < size; j++)
            if(array[j] < array[imin])
                imin = j;

        // Swap the found minimum element with the element at the current position
        swapping(array[i], array[imin]);
    }
}

int main() {
    int n; // Variable to store the size of the array
    n = 5; // Size of the array
    int arr[5] = {12, 19, 55, 2, 16}; // Initialize the array with 5 elements

    // Print the array before sorting
    cout << "Array before Sorting: ";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    // Call the selectionSort function to sort the array
    selectionSort(arr, n);

    // Print the array after sorting
    cout << "Array after Sorting: ";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0; // Return 0 to indicate successful execution
}
