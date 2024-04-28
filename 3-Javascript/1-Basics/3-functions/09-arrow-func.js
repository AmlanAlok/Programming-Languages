/**
 * Arrow functions are a useful new feature of ES6. 
 * With arrow functions, you can create functions without using the function keyword. 
 * You also often do not have to use the return keyword
 * 
 * Arrow functions do not block off the scope of this (Pg 17)
 */

// const lordify = function(firstName) { 
//     return `${firstName} of Canterbury`;
// };

// console.log(lordify("Dale")); // Dale of Canterbury  //ReferenceError: Cannot access 'lordify' before initialization

const lordify = firstName => `${firstName} of Canterbury`;

console.log(lordify("Dale"));

// // Typical function
// const lordify2 = function(firstName, land) { 
//     return `${firstName} of ${land}`;
// };

// Arrow Function
const lordify2 = (firstName, land) => `${firstName} of ${land}`; 

console.log(lordify2("Don", "Piscataway")); // Don of Piscataway
console.log(lordify2("Todd", "Schenectady")); // Todd of Schenectady


const lordify3 = (firstName, land) => { 
    if (!firstName) {
        throw new Error("A firstName is required to lordify"); 
    }
    if (!land) {
        throw new Error("A lord must have a land");
    }
    return `${firstName} of ${land}`; 
};

console.log(lordify3("Kelly", "Sonoma")); // Kelly of Sonoma console.log(lordify("Dave")); // ! JAVASCRIPT ERROR


// how to return an object in arrow functions
const person = (firstName, lastName) => ({ 
    first: firstName,
    last: lastName
});