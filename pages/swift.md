# [Swift Programming](https://alwinwoo.github.io/pages/swift.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/swift.md)

# Basics
* Variables, Constants, Boolean, Comments, Print

```code
// similar to PHP, C etc. just no semi-colon at the end

var age = 30 (int variable)
var age : Int = 30 (declare age as Int type, set as 30) - Int, Float, Double, String 
var weight = 10.0 (double variable)

var fat = false (boolean) - another example below

let age = 30 (constant)

Int(weight) - convert double to int, or vice versa

// write comment

print(age)
print(7 / 4) not the same as print (7.0 / 4.0), the first will show whole numbers
when multiplying, variables must be same type ie. int, float or double
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

* Arrays

```code
var movies = ["Move 1","DC"]
var movie : [Any] = [.... ] (accepts anything, if declare String)

movie[0] shows first "Move 1", same as PHP

movie.append("Batman")        // adds to the end of the array
movie.insert("Batman", at: 0) // inserts into the start of the array
movie.remove(at: 0)           // removes from the start of the array

movie.count                   // count number of items in array
