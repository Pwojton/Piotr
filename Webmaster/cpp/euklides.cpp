/*
 * euklides.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

int main(int argc, char **argv)
{
	int a, b;
    cout << "Podaj dwe liczby";
    cin >> a >> b;
    int nwd = nwd1(a, b);
    cout << "NWD(" << a << "," << b << ") =" << nwd << endl; 
	return 0;
}

