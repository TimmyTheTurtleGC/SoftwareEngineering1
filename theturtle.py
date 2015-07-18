'''
Welcome to Software Engineering 1 - Timmy the Turtle
I'm calling it 1. Maybe there will be more.

This isn't a lesson in programming - that would be Software Engineering 101 
and probably be located somewhere on campus assuming there's any space left on
campus to hide anything. I'm throwing you straight into it. I've given you
most the code, and you just need to complete one method.

There is no need to download this file to run it. You can run this code by 
copying and pasting everything into the demo section on
http://www.skulpt.org/ or https://trinket.io/ (no registration needed to use the demo tools),
and if all else fails, you can manually do everything with a pen, a protractor, and some graph 
paper, though you may find it a bit tedious.

This exercise requires you to write a caesar cipher in python. What's python?
Python is a programming language - one of many such languages that attempt to
make computers do what we want, but really anyone that's worked with computers
long enough knows you can only hope they do what you want. You can read more here:
https://www.python.org/ (which also has an place to run code in the browser, but
can't run the turtle library used here).

Why python and not <insert some other language here>? To really meet the requirements
to hide this cache, I can't force you to have to install software (though I can apparently
make you shoot a rope 30 feet up a tree and force you to climb that for a smile - I didn't,
don't worry), so I needed something I could point you to a couple websites and run
everything in your browser.

I also have to admit, I only have a passing familiarity with python as I'm a Java programmer,
so every time you think to yourself "Why didn't he just do <x>?" that's why.

Please do not contact me about syntax errors or why your code doesn't run. Instead, I
encourage you to follow the sage advice of one of my professors 
(best read in a deep voice with a thick accent): "Google it."

Do contact me about why you can't find the cache once you have the coordinates.

Also: Indentation is 4 spaces, no tabs.
'''

import turtle
from time import sleep

def main():
    testCaesar()
    showMeTheWayTimmy()
    clueThemIn()
    
    sleep(10)
 

def caesar(text, n):
    '''
    This function encrypts or decrypts ASCII text by shifting each character by n letters.
    Upper case must stay uppercase. Lower case must stay lower case. All other characters,
    such as whitespace, numbers, or symbols should not shift, but still be included in the output.
    For example caesar("Ab C2", 1) should return "Bc D2", and caesar(caesar("Ab C2", 1), 25)
    should return "Ab C2" Any two caesar calls with shifts that total 26 will return the
    original text. A caesar shift of 13 is equivalent to rot13.
    '''
    # TODO: You need to add a caesar cipher that meets the specification
    cipherText = ""
    return cipherText


def showMeTheWayTimmy():
    steps = caesar("jhS(Hrej8Evh@HT#NVA33ubaSHsj48hfhvbsSFGWgs^VjksdfhjkwfWEHWFH4388fhWFHSFB^IFBsksuguierguvbjv/SGHRfhsk%DHDj4!xgdu6kawshw8FHSE^&^UKEBGIWSVDJSK%^Y&Jwohf1", 23)
    i = 0
    timmy = turtle.Turtle()
    width = timmy.getscreen().window_width()
    height = timmy.getscreen().window_height()
    timmy.color('blue')
    
    timmy.penup();
    timmy.goto(-width/2 + ord(steps[i]) - 94, height/2 - ord(steps[i]) + 63)
    i+=1
    timmy.setheading(ord(steps[i])-11)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-50)
    i+=1
    timmy.setheading(ord(steps[i]) + 275)
    i+=1
    timmy.forward(ord(steps[i])-24)
    i+=1
    timmy.setheading(ord(steps[i])-21)
    i+=1
    timmy.forward(ord(steps[i])-68)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 93, height/2 - ord(steps[i]) + 93)
    i+=1
    timmy.setheading(ord(steps[i])+214)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-51)
    i+=1
    timmy.left(ord(steps[i])-25)
    i+=1
    timmy.forward(ord(steps[i])-81)
    i+=1
    timmy.backward(ord(steps[i])-54)
    i+=1
    timmy.left(ord(steps[i])+21)
    i+=1
    timmy.forward(ord(steps[i])-66)
    i+=1
    timmy.backward(ord(steps[i])-5)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 55, height/2 - ord(steps[i]) + 65)
    i+=1
    timmy.setheading(ord(steps[i])-83)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-78)
    i+=1
    timmy.right(ord(steps[i])+39)
    i+=1
    timmy.forward(ord(steps[i])-21)
    i+=1
    timmy.right(ord(steps[i])-24)
    i+=1
    timmy.forward(ord(steps[i])-111)
    i+=1
    timmy.right(ord(steps[i])-30)
    i+=1
    timmy.forward(ord(steps[i])-50)
    
    steps = caesar(steps, 12)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 31, height/2 - ord(steps[i]) + 71)
    timmy.color('red')
    i+=1
    timmy.setheading(ord(steps[i])+82)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-105)
    i+=1
    timmy.left(ord(steps[i])+38)
    i+=1
    timmy.forward(ord(steps[i])-41)
    i+=1
    timmy.left(ord(steps[i])-23)
    i+=1
    timmy.forward(ord(steps[i])-101)
    i+=1
    timmy.right(ord(steps[i])-23)
    i+=1
    timmy.forward(ord(steps[i])-86)
    i+=1
    timmy.right(ord(steps[i])-17)
    i+=1
    timmy.forward(ord(steps[i])-88)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 46, height/2 - ord(steps[i]) + 56)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-79)
    i+=1
    timmy.forward(ord(steps[i])-70)
    i+=1
    timmy.right(ord(steps[i])+20)
    i+=1
    timmy.forward(ord(steps[i])-97)
    i+=1
    timmy.right(ord(steps[i])-8)
    i+=1
    timmy.forward(ord(steps[i])-84)
    i+=1
    timmy.left(ord(steps[i])+21)
    i+=1
    timmy.forward(ord(steps[i])-100)
    i+=1
    timmy.left(ord(steps[i])-26)
    i+=1
    timmy.forward(ord(steps[i])-88)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 99, height/2 - ord(steps[i]) + 69)
    timmy.pendown()
    i+=1
    timmy.dot(ord(steps[i]) - 108)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 93, height/2 - ord(steps[i]) + 73)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-25)
    i+=1
    timmy.forward(ord(steps[i])-86)
    i+=1
    timmy.left(ord(steps[i])-12)
    i+=1
    timmy.forward(ord(steps[i])-101)
    i+=1
    timmy.left(ord(steps[i])+20)
    i+=1
    timmy.forward(ord(steps[i])-63)
    i+=1
    timmy.left(ord(steps[i])+9)
    i+=1
    timmy.forward(ord(steps[i])-60)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 69, height/2 - ord(steps[i]) + 69)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-81)
    i+=1
    timmy.forward(ord(steps[i])-42)
    i+=1
    timmy.right(ord(steps[i])+39)
    i+=1
    timmy.forward(ord(steps[i])-26)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) -46, height/2 - ord(steps[i]) + 46)
    i+=1
    timmy.setheading(ord(steps[i])-111)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-103)
    i+=1
    timmy.right(ord(steps[i])+20)
    i+=1
    timmy.forward(ord(steps[i])-49)
    i+=1
    timmy.right(ord(steps[i])+9)
    i+=1
    timmy.forward(ord(steps[i])-56)
    i+=1
    timmy.right(ord(steps[i])+11)
    i+=1
    timmy.forward(ord(steps[i])-45)
    
    steps = caesar(steps, 3)
    
    timmy.penup()
    timmy.color('green')
    i+=1
    timmy.goto(-width/2 + ord(steps[i]) - 84, height/2 - ord(steps[i]) + 44)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])+205)
    i+=1
    timmy.forward(ord(steps[i])-47)
    i+=1
    timmy.setheading(ord(steps[i])-8)
    i+=1
    timmy.forward(ord(steps[i])-91)
    i+=1
    timmy.setheading(ord(steps[i])+171)
    i+=1
    timmy.forward(ord(steps[i])-91)
    i+=1
    timmy.setheading(ord(steps[i])-33)
    i+=1
    timmy.forward(ord(steps[i])-80)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 93, height/2 - ord(steps[i]) + 53)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-117)
    i+=1
    timmy.forward(ord(steps[i])-103)
    i+=1
    timmy.right(ord(steps[i])-10)
    i+=1
    timmy.forward(ord(steps[i])-85)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 93, height/2 - ord(steps[i]) + 53)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-104)
    i+=1
    timmy.forward(ord(steps[i])-100)
    i+=1
    timmy.right(ord(steps[i])-28)
    i+=1
    timmy.forward(ord(steps[i])-74)
    
    steps = caesar(steps, 20)
    
    timmy.penup()
    timmy.color('orange')
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 7, height/2 - ord(steps[i]) -3)
    i+=1
    timmy.setheading(ord(steps[i])+181)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-62)
    i+=1
    timmy.left(ord(steps[i])+12)
    i+=1
    timmy.forward(ord(steps[i])-68)
    i+=1
    timmy.backward(ord(steps[i])-98)
    i+=1
    timmy.left(ord(steps[i])-20)
    i+=1
    timmy.forward(ord(steps[i])-106)
    i+=1
    timmy.backward(ord(steps[i])-83)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) -22, height/2 - ord(steps[i]) -13)
    i+=1
    timmy.setheading(ord(steps[i])-74)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-68)
    i+=1
    timmy.right(ord(steps[i])+16)
    i+=1
    timmy.forward(ord(steps[i])-82)
    i+=1
    timmy.right(ord(steps[i])+38)
    i+=1
    timmy.forward(ord(steps[i])-23)
    i+=1
    timmy.right(ord(steps[i])-10)
    i+=1
    timmy.forward(ord(steps[i])-79)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 86, height/2 - ord(steps[i])+ 26)
    timmy.pendown()
    i+=1
    timmy.dot(ord(steps[i])-94)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 44, height/2 - ord(steps[i]) + 4)
    i+=1
    timmy.setheading(ord(steps[i])+157)
    timmy.pendown()
    i+=1
    timmy.forward(ord(steps[i])-73)
    i+=1
    timmy.left(ord(steps[i])-9)
    i+=1
    timmy.forward(ord(steps[i])-111)
    i+=1
    timmy.left(ord(steps[i])-20)
    i+=1
    timmy.forward(ord(steps[i])-84)
    i+=1
    timmy.left(ord(steps[i])+34)
    i+=1
    timmy.forward(ord(steps[i])-66)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 58, height/2 - ord(steps[i]) + 28)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-89)
    i+=1
    timmy.forward(ord(steps[i])-65)
    i+=1
    timmy.right(ord(steps[i])-4)
    i+=1
    timmy.forward(ord(steps[i])-23)
    i+=1
    timmy.right(ord(steps[i])-4)
    i+=1
    timmy.forward(ord(steps[i])-55)
    i+=1
    timmy.left(ord(steps[i])+9)
    i+=1
    timmy.forward(ord(steps[i])-60)
    i+=1
    timmy.left(ord(steps[i])+18)
    i+=1
    timmy.forward(ord(steps[i])-67)
    
    timmy.penup()
    i+=1
    timmy.goto(timmy.position()[0] + ord(steps[i]) - 69 , height/2 - ord(steps[i]) + 29)
    timmy.pendown()
    i+=1
    timmy.setheading(ord(steps[i])-67)
    i+=1
    timmy.forward(ord(steps[i])-79)
    i+=1
    timmy.right(ord(steps[i])+24)
    i+=1
    timmy.forward(ord(steps[i])-59)
    i+=1
    timmy.right(ord(steps[i])+10)
    i+=1
    timmy.forward(ord(steps[i])-79)
    i+=1
    timmy.left(ord(steps[i])+9)
    i+=1
    timmy.forward(ord(steps[i])-22)
    i+=1
    timmy.left(ord(steps[i])-4)
    i+=1
    timmy.forward(ord(steps[i])-59)
    
    timmy.penup()
    timmy.home()
    for i in range(1, 100):
        timmy.right(10)
        sleep(.1)
    
    return


def clueThemIn():
    clue = "Gur pbagnvare jnf pubfra gb svg va jvgu gur raivebazrag, ohg fubhyq or qvssrerag rabhtu.\nLbh'yy svaq jung lbh frrx va gur bnfvf."
    print caesar(clue, 13)
    

def testCaesar():
    '''
    Tests your caesar function. If your code does not raise errors here, 
    you probably created a valid function. Probably. This really doesn't
    test all cases, as you can easily write a function that outputs the
    expected answers for the known inputs that will appear to succeed,
    but get you no where.
    I'm printing the error and exiting for ease of use with skulpt.
    '''
    if "Bc D2" != caesar("Ab C2", 1):
        print "caesar('Ab C2', 1) failed."
        exit()
    if "Uryyb Jbeyq." != caesar("Hello World.", 13):
        print "caesar('Hello World.', 13) failed."
        exit()
    if "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" != caesar(caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 7), 19):
        print "caesar(caesar('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',7),19) failed."
        exit()
    
    print "All tests passed. You should be good to go."


if __name__ == '__main__':
    main()
    
