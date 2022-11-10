// Objects

const person = {
    firstName: 'Kaio',
    lastName: 'Oliveira',
    age: '30',
    hobbies: ['F1', 'Transar', 'Dormir'],
    dog: {
        name: 'Margot',
        age: '0,5'
    }
}

// const firstName = person.firstName
// const lastName = person.lastName
// const age = person.age
// const hobbies = person.hobbies

const {firstName: primeiroNome, lastName, age, hobbies,dog} = person

console.log(primeiroNome)
console.log(lastName)
console.log(age)
console.log(hobbies[2])
console.log(dog)
