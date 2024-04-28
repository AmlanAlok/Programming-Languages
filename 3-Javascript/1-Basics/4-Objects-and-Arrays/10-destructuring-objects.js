
const sandwich = {
    bread: "dutch crunch",
    meat: "tuna",
    cheese: "swiss",
    toppings: ["lettuce", "tomato", "mustard"]
};
const { bread, meat } = sandwich;
console.log(bread, meat); // dutch crunch tuna


const sandwich2 = {
    bread: "dutch crunch",
    meat: "tuna",
    cheese: "swiss",
    toppings: ["lettuce", "tomato", "mustard"]
};
let { bread2, meat2 } = sandwich2;
bread2 = "garlic";
meat2 = "turkey";
console.log(bread2); // garlic 
console.log(meat2); // turkey
console.log(sandwich.bread, sandwich.meat); // dutch crunch tuna