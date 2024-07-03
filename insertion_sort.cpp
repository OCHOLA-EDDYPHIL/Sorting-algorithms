// remove from list
#include <iostream>
#include <list>

using namespace std;

int main() {
    int myints[] = {17, 89, 7, 14};
    list<int> mylist(myints, myints + 4);
    mylist.remove(89);
    cout << "mylist contains:";
    for (list<int>::iterator it = mylist.begin(); it != mylist.end();
         ++it) {
        cout << " " << *it;
//        cout << endl;
    }
    return 0;
}