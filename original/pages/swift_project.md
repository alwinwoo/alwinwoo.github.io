# [Swift Programming](https://alwinwoo.github.io/pages/swift.html)
[home](https://alwinwoo.github.io/) | [Project](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/swift_project.md) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/swift.md)

# My Project

```swift
import Foundation

enum character_class {
    case fighter
    case cleric
    case thief
    case mage
}

struct character {
    var name      : String
    var charclass : character_class 
    var hp        : Int
    var max_hp    : Int
    var XP        : Int
}

var my_character = character(name:"Nozomi",charclass:.fighter,hp:10,max_hp:10,XP:0)
```


