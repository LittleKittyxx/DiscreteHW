#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int MAX = 100;

class Queue
{
private:
    int queue[MAX], size = 0;

public:
    Queue(int n)
    {
        for (int i = 0; i < n; i++)
        {
            queue[i] = rand() % 90 + 10;
        }
        size = n;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << queue[i] << " ";
        }
        cout << "\n\n";
    }

    void enqueue(int x)
    {
        if (size == MAX)
        {
            cout << "Queue is full\n\n";
        }
        else
        {
            queue[size++] = x;
            cout << "value is added\n\n";
        }
    }

    void dequeue()
    {
        size--;

        for (int i = 0; i < size; i++)
        {
            queue[i] = queue[i + 1];
        }
    }

    int first()
    {
        return queue[0];
    }

    bool isEmpty()
    {
        return size == 0;
    }
};

void print_menu()
{
    cout << "1 - Print queue\n";
    cout << "2 - Add value\n";
    cout << "3 - Delete first value\n";
    cout << "4 - Print first value\n";
    cout << "5 - Check size\n";
    cout << "0 - Exit\n\n";
    cout << "Enter your choise: ";
}

int main()
{
    srand(time(NULL));
    Queue q(10);
    
    for (;;)
    {
        print_menu();
        int k;
        cin >> k;

        switch (k)
        {
        case 1:
            q.print();
            break;

        case 2:
            int x;
            cout << "Enter x: ";
            cin >> x;
            q.enqueue(x);
            break;

        case 3:
            q.dequeue();
            break;

        case 4:
            cout << "First value:" << q.first()
                 << endl
                 << endl;
            break;

        case 5:
            q.isEmpty() ? cout << "Queue is empty\n\n" : cout << "Queue is'n empty\n\n";
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