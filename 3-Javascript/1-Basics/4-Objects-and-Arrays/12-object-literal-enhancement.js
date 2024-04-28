/**
 * Object literal enhancement allows us to pull global variables into objects and 
 * reduces typing by making the function keyword unnecessary
 * 
 * 
 */

const name = "Tallac"; 
const elevation = 9738;

const funHike = { name, elevation }; 

console.log(funHike); // {name: "Tallac", elevation: 9738}



////////

const skier = { 
    name,
    sound,
    powderYell() {
        let yell = this.sound.toUpperCase();
        console.log(`${yell} ${yell} ${yell}!!!`);
    },
    speed(mph) {
        this.speed = mph; console.log("speed:", mph);
    } 
};