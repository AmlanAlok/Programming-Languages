
// type variableName = value;

String name = "John";
System.out.println(name);

int myNum = 15;
System.out.println(myNum);

int myNum;
myNum = 15;
System.out.println(myNum);

final int myNum = 15;
myNum = 20;  // will generate an error: cannot assign a value to a final variable

int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";

// You can also assign the same value to multiple variables in one line
int x, y, z;
x = y = z = 50;
System.out.println(x + y + z);

char myVar1 = 65, myVar2 = 66, myVar3 = 67;
System.out.println(myVar1);   // A
System.out.println(myVar2);   // B
System.out.println(myVar3);   // C

String x = "10";
int y = 20;
String z = x + y;  // z will be 1020 (a String)

/*
https://www.w3schools.com/java/java_data_types.asp

Primitive data types - includes:
1. byte           1 byte	     Stores whole numbers from -128 to 127
2. short          2 bytes	    Stores whole numbers from -32,768 to 32,767
3. int            4 bytes	    Stores whole numbers from -2,147,483,648 to 2,147,483,647
4. long           8 bytes	    Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
5. float          4 bytes	    Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
6. double         8 bytes	    Stores fractional numbers. Sufficient for storing 15 decimal digits
7. boolean        1 bit	      Stores true or false values
8. char           2 bytes	    Stores a single character/letter or ASCII values

The char data type is used to store a single character. The character must be surrounded by single quotes, like 'A' or 'c'

Non-primitive data types (called reference types because they refer to objects)
1. String - The String data type is used to store a sequence of characters (text). String values must be surrounded by double quotes.
2. Arrays
3. Classes
  */

