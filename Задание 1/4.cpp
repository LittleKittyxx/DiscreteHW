#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class Array
{
private:
    int array[MAX], size = 0;

public:
    Array(int n)
    {
        for (int i = 0; i < n; i++)
        {
            array[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << array[i] << " ";
        }
        cout << "\n\n";
    }

    int findIndex(int x)
    {
        for (int i = 0; i < size; i++)
        {
            if (array[i] == x)
                return i;
        }
        return -1;
    }

    void add(int x)
    {
        if (findIndex(x) != -1)
        {
            cout << "Value is already in array\n\n";
            return;
        }

        if (size == MAX)
        {
            cout << "Array is full\n\n";
            return;
        }

        array[size++] = x;
        cout << "value is added\n\n";
    }

    void del(int value)
    {
        int idx = findIndex(value);
        if (idx == -1)
        {
            cout << "Array doesn't contain the value\n\n";
            return;
        }

        for (int i = idx; i < size - 1; i++)
        {
            array[i] = array[i + 1];
        }
        size--;

        cout << "Value is deleted\n\n";
    }

    void contains(int x)
    {
        if (findIndex(x) == -1)
        {
            cout << "Array doesn't contain the value\n\n";
        }
        else
        {
            cout << "Array contains the value\n\n";
        }
    }

    bool isEmpty()
    {
        return size == 0;
    }
};

void print_menu()
{
    cout << "1 - Print Queue\n";
    cout << "2 - Add value\n";
    cout << "3 - Delete item by value\n";
    cout << "4 - Containts a value\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n\n";
    cout << "Enter your choise: ";
}

int main()
{
    srand(time(NULL));
    Array a(10);

    for (;;)
    {
        print_menu();
        int k;
        cin >> k;

        switch (k)
        {
        case 1:
            a.print();
            break;

        case 2:
            int x;
            cout << "Enter value: ";
            cin >> x;
            a.add(x);
            break;

        case 3:
            int y;
            cout << "Enter value: ";
            cin >> y;
            a.del(y);
            break;

        case 4:
            int z;
            cout << "Enter value: ";
            cin >> z;
            a.contains(z);
            break;

        case 5:
            a.isEmpty() ? cout << "Array is Empty\n\n" : cout << "Array is'n Empty\n\n";
            break;

        case 0:
            return 0;
            break;

        default:
            cout << "Wrong choise\n\n";
            break;
        }
    }
}