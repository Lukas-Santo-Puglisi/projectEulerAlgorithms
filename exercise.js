// Task: Task: Implement a function in JavaScript using ES6+ syntax that converts a map of key-value pairs into an object. The function should be named mapToObject and take a Map as an argument. Demonstrate using this function by converting a map containing a few sample key-value pairs into an object and then print the resulting object.

function mapToObject(myMap){
  resultObject = {}
  const iterator1 = myMap[Symbol.iterator()]
  for (const item of iterator1){
    resultObject[item[0]] = item[1]

  }
  return resultObject
}

