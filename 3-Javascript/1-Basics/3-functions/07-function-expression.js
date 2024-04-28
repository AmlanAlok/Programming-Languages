/**
 * You can only invoke the function after it is defined in func expressions.
 * It is not hoisted.
 */

// logCompliment();        // ReferenceError: Cannot access 'logCompliment' before initialization


const createCompliment = function(firstName, message) { 
    return `${firstName}: ${message}`;
};

console.log(createCompliment("You're so cool", "Molly"));

// function expression
const logCompliment = function() { 
    console.log("You're doing great!");
};

logCompliment();

const logCompliment2 = function(firstName, message) { 
    console.log(`${firstName}: ${message}`);
};

logCompliment2("Molly", "You're so cool");
