// Using var
function exampleVar() {
  if (true) {
    var x = 10;
  }
  console.log(x); // Outputs 10 (not blocked by if statement)
}

// Using let
function exampleLet() {
  if (true) {
    let y = 20;
  }
  console.log(y); // ReferenceError: y is not defined (blocked by block scope)
}

//--------------------
// This demonstrates the difference between var and let regarding hoisting and initialization.

// Hoisting with var
console.log(x); // Output: undefined
var x = 5;
console.log(x); // Output: 5

// Hoisting with let
/*
They are not initialized until the interpreter reaches the line where the variable is declared. 
This is known as the "temporal dead zone," and attempting to access the variable before its declaration results in a `ReferenceError`.
*/

try {
    console.log(y); // ReferenceError: Cannot access 'y' before initialization
} catch (e) {
    console.log(e); // Output: ReferenceError
}
let y = 5;
console.log(y); // Output: 5

