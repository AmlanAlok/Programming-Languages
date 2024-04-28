

function logActivity(name="Shane McConkey", activity="skiing") {
    console.log( `${name} loves ${activity}` )
}

logActivity()

var defaultPerson = {
    name: {
      first: "Shane",
      last: "McConkey"
    },
    favActivity: "skiing"
}

function logActivity2(p=defaultPerson) {
    console.log(`${p.name.first} loves ${p.favActivity}`)
}

logActivity2()