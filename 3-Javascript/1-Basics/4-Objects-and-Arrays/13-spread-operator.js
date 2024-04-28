

const peaks = ["Tallac", "Ralston", "Rose"]; 
const canyons = ["Ward", "Blackwood"]; 
const tahoe = [...peaks, ...canyons];

console.log(tahoe.join(", ")); // Tallac, Ralston, Rose, Ward, Blackwood

const peaks2 = ["Tallac", "Ralston", "Rose"]; 
const [last2] = peaks2.reverse();
console.log(last2); // Rose
console.log(peaks2.join(", "));


const peaks3 = ["Tallac", "Ralston", "Rose"]; 
const [last3] = [...peaks3].reverse();
console.log(last3); // Rose
console.log(peaks3.join(", ")); // Tallac, Ralston, Rose


function directions(...args) {
    let [start, ...remaining] = args;
    let [finish, ...stops] = remaining.reverse();
    console.log(`drive through ${args.length} towns`);
    console.log(`start in ${start}`);
    console.log(`the destination is ${finish}`);
    console.log(`stopping ${stops.length} times in between`);
}

directions("Truckee", "Tahoe City", "Sunnyside", "Homewood", "Tahoma");
