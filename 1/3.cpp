#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class List
{
private:
    int list[MAX], size = 0;

public:
    List(int n)
    {
        for (int i = 0; i < n; i++)
        {
            list[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << list[i] << " ";
        }
        cout << "\n\n";
    }

    void insert(int index, int x)
    {
        size++;

        for (int i = size; i > index; i--)
        {
            list[i] = list[i - 1];
        }

        list[index] = x;
    }

    void remove(int index)
    {
        for (int i = index; i < size; i++)
        {
            list[i] = list[i + 1];
        }

        size--;
    }

    int indexOf(int x)
    {
        for (int i = 0; i < size; i++)
        {
            if (list[i] == x)
            {
                return i;
            }
        }
        return -1;
    }

    bool isEmpty()
    {
        return size == 0;
    }
};

void print_menu()
{
    cout << "1 - Print Queue\n";
    cout << "2 - Insert value by index\n";
    cout << "3 - Delete value by index\n";
    cout << "4 - Index of value\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n\n";
    cout << "Enter your choise: ";
}

int main()
{
    srand(time(NULL));
    List l(10);
    
    for (;;)
    {
        print_menu();
        int k;
        cin >> k;

        switch (k)
        {
        case 1:
            l.print();
            break;

        case 2:
            int i;
            int x;
            cout << "Enter x: ";
            cin >> x;
            cout << "Enter index: ";
            cin >> i;
            l.insert(i, x);
            break;

        case 3:
            int y;
            cout << "Enter index: ";
            cin >> y;
            l.remove(y);
            break;

        case 4:
            int z;
            cout << "Enter value: ";
            cin >> z;
            cout << "Index " << z << " = " << l.indexOf(z) << "\n\n";
            break;

        case 5:
            l.isEmpty() ? cout << "List is Empty\n\n" : cout << "List is'n Empty\n\n";
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