# [Swift Programming](https://alwinwoo.github.io/pages/swift.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/swift.md)

# Basics

```code
import Foundation
```

* Variables, Constants, Boolean, Comments, Print

```code
// similar to PHP, C etc. just no semi-colon at the end

var age = 30 (int variable)
var age : Int = 30    (declare age as Int type, set as 30) - Int, Float, Double, String 
var age : Int? = 30   (declare as an optional Int)
var weight = 10.0 (double variable)

var fat = false (boolean) - another example below

let age = 30 (constant)

Int(weight) - convert double to int, or vice versa

// write comment

print(age)
print(7 / 4) not the same as print (7.0 / 4.0), the first will show whole numbers
when multiplying, variables must be same type ie. int, float or double
```

* Arrays

```code
var movies = ["Move 1","DC"]
var movie : [Any] = [.... ] (accepts anything, if declare String)

movie[0] shows first "Move 1", same as PHP

movie.append("Batman")        // adds to the end of the array
movie.insert("Batman", at: 0) // inserts into the start of the array
movie.remove(at: 0)           // removes from the start of the array

movie.count                   // count number of items in array
```

* If.. else... or statements

```code
if fat == true {
  print("you need to lose weight")
} else {
  print("you are okay")
}

// multiple condition
if height >=50 && weight >= 100, || and == work

// alternative way
var loseweight = fat == true

if loseweight {
  print("you need to lose weight")
}
```

* For Loop

```code

// print 10 Hellos
for _ in 1...10 {
  print("Hello")
}

// print 1 to 10
for number in 1...10 {
  print(number)
}

// print name of movies
var movies = ["Batman", "Spiderman","Ali-baba"]

for movie in movies {
  print(movie)
}

// print array of lucky numbers
var rank = 1
luckynumbers = [5,12,134,134134,135135,31513134]

for number in luckynumbers {
  print("\(rank). \(number)")
  rank += 1
}

for x in 0..luckynumbers.count {
  print("\(x+1). \(luckynumbers[x]")
}

// create array of random numbers
var str ="["

for _ in 1.. 100 {
  str += "\(Int.random(in: 0...10_000)),"
}

str += "]"

print(str)
```

* Tuples and Sets

```code
var dog = ("Fido",8)                  // Tuple
var dog = (String,Int) = ("Fido",8)   // fixes type
print(dog.0)                          // displays Fido
print(dog.1)                          // displays 8

var luckynumbers : Set = [134,345,1315,13,135,13,513,5135]  

// set must have unique numbers, has no order
// luckynumbers[0] will display an error
// luckynumbers.contains(134) will result in true
// luckynumbers.insert(555)
// luckynumbers.insert(134) will result in inserted = false
// if used as constant (set), then luckynumbers cannot be changed
```

* Dictionaries

// dictionaries have keys and values, case sensitive

var words = ["bang":"boys are not good"]      // like php keys
print(words["bang"])                          // will show the value

words["knock"] = "hit on the head"            // will add a new entry into words
words.removeValue(forKey:"bang")              // will remove "bang" key and value

# Functions

```code
func hello(person : String) {
  print("Hello \(person)!")
}

hello(person : "Sam")

func addTwoNumbers(num1 : Int, num2 : Int) -> Int {
  print(num1 + num2)
  return num1 + num 2
}

var num3 = addTwoNumbers(num1 : 1, num2 : 8)
var num4 = addTwoNumbers(num1 : num3, num2 : addTwoNumbers(num1 : 1, num2 : 8))

```

# Optionals

// either have a value or nil

var age : Int? = 30     // will display Optional(30)

print (Int(age))        // will print 30, which is an integer
print (age!)            // forces to show that it is not nil, but if it's nil, the app will crash

if age != nil {         // protects against crash
  print(age!)
}

if let age = Int(age) { // age returns nil if creating the constant fails
  print(age)
} else {
  print("Invalid age")
}

# Classes

# Developing for Apple Apps

```code
import UIKit
```
