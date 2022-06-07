
/*

Problem

One of the most common uses of a queue is to keep a list of "work to be done". Just like doing housework, often new things get added to the TODO list while doing some other task. New jobs get added to the end of the queue, and when one is complete, the next one is taken from the top of the list.

Oliver is missing his favorite hat and is asking his friends at the dog park if they've seen it. Each dog either has seen it or suggests a list of other dogs to ask. Return the name of the dog who has seen the hat. Oliver starts out by asking his best friend. This function will take two parameters. The first is a map of dogs to a list of their friends. The second is Oliver's best friend, who Oliver will ask first.

Function Signature:
function findHat(dogs, bestFriend)

*/
//
// - set var dogs to ask
// - new Set = dogs already asked
//
// - next dog to ask
//
// function findHat(dogs, bestFriend) {
//   const dogsToAsk = [bestFriend];
//   const dogsAlreadyAsked = new Set();
//   while(dogsToAsk.length > 0) {
//     nextDogToAsk = dogsToAsk.pop();
//     if (dogsAlreadyAsked.has(nextDogToAsk)) {
//       continue;
//     }
//     if (dogs[nextDogToAsk][0] === 'HAT') {
//       return nextDogToAsk;
//     }
//     dogsAlreadyAsked.add(nextDogToAsk);
//
//     const newDogsToAsk = dogs[nextDogToAsk];
//     dogsToAsk.unshift(...newDogsToAsk);
//   }
//   throw new Error('Hat not found');
// }
//
// const dogs = {
//   'Carter': ['Fido', 'Ivy'],
//   'Ivy': ["HAT"], // Ivy has seen the hat
//   'Loki': ['Snoopy'],
//   'Pepper': ['Carter'],
//   'Snoopy': ['Pepper'],
//   'Fido': []
// };
// console.log(findToy(dogs, 'Loki'));

function findHat(dogs, bestFriend) {

  const dogsToAsk = [bestFriend]; // [ ]
  // console.log(dogsToAsk)
  const dogsAlreadyAsked = new Set(); // ( )

  while(dogsToAsk.length > 0) {
    let nextDogToAsk = dogsToAsk.pop(); // Loki
    if (dogsAlreadyAsked.has(nextDogToAsk)) {
      continue;
    }
    if (dogs[nextDogToAsk][0] === 'HAT') {
      return nextDogToAsk;
    }
    dogsAlreadyAsked.add(nextDogToAsk);

    const newDogsToAsk = dogs[nextDogToAsk];
    // console.log(newDogsToAsk)
    dogsToAsk.unshift(...newDogsToAsk);
  }
  throw new Error('Hat not found');
}

const dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], // Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
};
console.log(findHat(dogs, 'Loki'));
