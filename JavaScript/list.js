// List

const names = ['Kaio', 'Joao', 'Julia',10,false]

const joao = names[1]
console.log(joao)


names.push('Pedro') // Adiciona ao início da lista
names.unshift('Zezo') // Adiciona ao final da lista
names.pop() // Remove o ultimo valor da lista
names.pop()
names.pop()

names[3] = "Paulinha"

console.log(names.indexOf('Paulinha'))

console.log(names)

console.log(names.sort())

const numbers = [1,2,3,4,5]

const numbersMultipliedByTwo = numbers.map(function(number){
    return number*2
})

console.log(numbersMultipliedByTwo)

const ages = [8,13,27,30,22,40]

const evenAges = ages.filter(function(age){
    return age % 2 === 0
})

console.log(evenAges)

const sumOfAges = ages.reduce(function(age,accumulator){
    return accumulator+age
},0)

console.log(sumOfAges)
