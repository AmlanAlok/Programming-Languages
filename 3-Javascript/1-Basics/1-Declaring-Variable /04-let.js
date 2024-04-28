/**
 * With the let keyword, we can scope a variable to any code block. 
 * Using let protects the value of the global variable
 */

var topic = "JavaScript";

if (topic) {
    let topic = "React";        // this create a new var topic with block scope
    console.log("block", topic); // React
}

console.log("global", topic); // JavaScript