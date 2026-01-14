- Operator overloading allows an operator to work with user-defined data types, for example using + to add two objects.

#### Example

```cpp
class A {
public:
    int x;

    A(int a = 0) {
        x = a;
    }

    A operator + (A obj) {
        A temp;
        temp.x = x + obj.x;
        return temp;
    }
};

A a1(5), a2(10);
A a3 = a1 + a2;
```

Explanation (one line for exam):

> Here the `+` operator is overloaded to add two objects of class `A` by adding their data members.
