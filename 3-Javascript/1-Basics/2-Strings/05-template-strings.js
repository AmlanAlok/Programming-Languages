
let firstName = 'first'
let middleName = 'middle'
let lastName = 'last'

console.log(lastName + ", " + firstName + " " + middleName);

/**
 * With a template, we can create one string and insert the variable values by surrounding 
 * them with ${ }
 * 
 * Template strings honor whitespace
 */

console.log(`${lastName}, ${firstName} ${middleName}`);
