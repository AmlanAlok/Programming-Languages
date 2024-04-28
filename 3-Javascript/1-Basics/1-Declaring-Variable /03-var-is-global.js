/**
 * If a variable is created inside of an if/else block, that variable is not scoped to the block
 */

var topic = "JavaScript";

if (topic) {
    var topic = "React";        // this var will overwrite the value of the global var topic
    console.log("block", topic); // block React
}

console.log("global", topic); // global React