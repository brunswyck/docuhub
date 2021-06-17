# general basics review
## some code to warm up
```python
except: # except w no arg specified catches all errors
	
for i in range(10):
    try:
        if 10 / i == 2.0:
            break  # skips for loop 1 round on i = 0
    except ZeroDivisionError:  # handles i = 0 & prints 1
        print(1)
    else:
        print(2)   # prints 2 until i == 5, so 4 times 2
# 1 2 2 2 2
			
dict.get(4, "key 4 is not present")
dict.get(4, 99) # if no key 4, return 99

range(1, 9) # 9 not included

# Tuples can be created without the parentheses, by just separating the values with commas
my_tuple = "one", "two", "three"
tpl = () # empty tuple

sqs[4:7] # from 4 (5th) up to (not including) 7 (8th element) in list
list[0:2] # first two elements

# 3rd arg = STEP value
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
squares[2:8:3] # index 2, 5 grabbed [4, 25]

# reverse a list, neg value = backwards
[::-1] 
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1]) # [49, 36]

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
# [0, 4, 16, 36, 64]

# Create a list of multiples of 3 from 0 to 20.
a = [i for i in range(20) if i%3 ==0] # [0, 3, 6, 9, 12, 15, 18]

even = [2*i for i in range(10**100)] # MemoryError -> resolve w generator (yield)

print("{0}{1}{0}".format("abra", "cad")) # abracadabra
print("Hello ME".replace("ME", "world")) # "Hello World"
print("This is a sentence.".replace("This")) # True
# join -> string, split -> list

nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
	
if any([i % 2 == 0 for i in nums]):
    print("at least one is even")
	
for index, value in enumerate(nums):  # go over index & values
    print(index,"-",value) # 0-55 1-44 2-33 3-22 4-11
# percentage -> 100 * X / total

def find_longest_word(text):
    words = text.split(' ')
    biggest_word = ''
    for index, word in enumerate(words):
        if len(word) > len(biggest_word):
            biggest_word = words[index]
    return biggest_word


if __name__ == '__main__':
    txt = input()
    print(find_longest_word(txt))

```
# functional programming
## Higher-order, pure & anon functions

- Higher-order functions take other functions as arguments, or return them as results
- Pure functions have no side effects, and return a value that depends only on their arguments

```python
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# pure
def func(x):
    y = x**2
    z = x + y
    return z

# impure
some_list = []
def impure(arg):
    some_list.append(arg)

```
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel. 
- complicate the otherwise simple task of I/O, more difficult to write

## lambda
```python
""" lambda land

assign functions to variable = anonymous

pass function as an argument to another function
They can only do things that require a single expression
"""
def some_func(f, arg)
    return f(arg)

some_func(lambda x: 2*x*x, 5)

a = (lambda x: x*x), (8) # 64

# Lambda functions can be assigned to variables, and used like normal functions
double = lambda x: x*2
print(double(7))
# however, usually better to define function with def instead ...

triple = lambda x: x * 3
add = lambda x, y: x + y  # using 2 params

print(add(triple(3), 4)) # 13
```
## map

- The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument

```python

def add_five(x):
	return x+5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums)) # map(function, iterable)
# [16, 27, 38, 49, 60]

# using lambda:
result = list(map(lambda x: x+5, nums)) # [16, 27, 38, 49, 60]
```
## filter
- filters an iterable by removing items that don't match a predicate
(a function that returns a Boolean)

```python

nums = [11, 22, 33, 44, 55]
result = list(filter(lambda x: x%2==0, nums)) # [22, 44]
```
>***
>**note**
>Like map, the result has to be explicitly converted to a list to print it
>***

## Generator
- yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables

```python

def countdown():
	i=5
	while i > 0:
		yield i  # return value i & continue
		i -= 1


for i in countdown():
    print(i)  # 5 4 3 2 1

	
# they can be infinite!
def infinite_sevens():
    while True:
        yield 7


for i in infinite_sevens():
	print(i)
	
# Finite generators can be converted into lists by passing them as arguments to the list function

def numbers(x):
	for i in range(x):
		if i%2 == 0:
			yield i


print(list(numbers(11))) # [0, 2, 4, 6, 8, 10]
```

>***
>**note**
>Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage.
>Furthermore, we do not need to wait until all the elements have been generated before we start to use them. 
>***

## Decorators
Decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you don't want to modify

```python

def decor(func):
	def wrap():
		print("===============")
		func()
		print("===============")
	return wrap  # return inner function 'wrap'


def print_text():
	print("Becode was Here")


decorated = decor(print_text)  # some_var = decorator_func(some_function)
decorated()  # some_var()

@decor
def print_text():
	print("Becode was Here")


print_text()
# ===============
# Becode was Here
# ===============
```
>***
>**note**
>if we wrote a useful decorator we might want to replace print_text with the decorated version
>altogether so we always got our "plus something" version of print_text
>***



```
## sets
- Are unordered, so can't be indexed
- Cannot contain duplicate elements
- Faster membership checking than lists
- ~~append~~ use set.add()
- set.remove(x) # specific element
- set.pop(x) # remove arbirary element

|set operation| operator| description|
|:---:|:---:|---|
|union       |   \|  | combine 2 sets to form new one |
|intersection|   &   | get items present in both |
|difference  |   -   | get items in 1st set but not in 2nd|
|symmetric difference|^|get items in either but not both|
```python
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) # {4, 5, 6}
print(first - second) # {1, 2, 3}
print(first ^ second) # {1, 2, 3, 7, 8, 9}


```
## itertools
### count accumulate cycle repeat takewhile chain

One type of function it produces is **infinite iterators**
| function | description |
|---|:---|
| Count | **counts up** infinitely from a value|
| Cycle | *infinitely iterates through an iterable* (for instance a list or string)|
| Repeat| **repeats an object**, either infinitely or a specific number of times|
| Takewhile| takes items from iterable while predicate function remains True |
| Chain | **combines** iterables |
| Accumulate |returns a **running total** of values in an iterable|

```python
from itertools import count

for i in count(3): # counts up starting from 3
	print(i)
	if i>= 11:
		break

""" 3  4  5  6  7  8  9  10  11 """


from itertools import accumulate, takewhile


nums = list(accumulate(range(8)))
print(nums)  # [0,  1,   3,   6,  10,   15,   21, 28]
             # [0, 0+1, 1+2, 3+3, 6+4, 10+5, 15+6, 21+7]


print(list(takewhile(lambda x: x<=6, nums)))  # [0, 1, 3, 6]

# takewhile stops as soon as predicate == FALSE!
nums = [2, 4, 6, 7, 9, 8]  # will stop returning at hitting value 7
print(list(takewhile(lambda x: x%2==0, nums)))  # [2, 4, 6]



```

### itertools combinatoric functions (get all combo's)

```python

from itertools import product, permutations

letters = ("A", "B")

print(list(product(letters, range(2)))) # [('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters))) # [('A', 'B'), ('B', 'A')]


letters = ("A", "B", "C")
print(list(permutations(letters)))
#[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

a={1, 2}
print(len(list(product(range(3), a)))) # 6
print(list(product(range(3), a)))  # [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]

```


# OOP
## Classes
### Superclass

```python

# Superclass
class Animal:
	def __init__(self, name, color):
		self.name = name
		self.color = color

# Subclass
# If a class inherits from another with the same attributes or methods, it overrides them
class Cat(Animal):
	def purr(self):
		print("Purrr")
		
tiger = Cat("tiger", "black")
print(tiger.color)
tiger.purr
```
### indirect inheritance
```python
class A:
	def method(self):
		print("A method")
		
class B:
	def another_method(self):
		print("B method")
		
class C:
	def third_method(self):
		print("C method")
		
c = C()
c.method()
c.another_method()
c.third_method()
```

### super function
```python
class A: # superclass
	def spam(self):
		print(1)

class B(A)
    def spam(self):
	    print(2)
	    super().spam() # calls spam method of superclass
		
B().spam()
```
### magic methods
[special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
[nice summary on github](https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.markdown)

* f __ne__ is not implemented, it returns the opposite of __eq__
There are no other relationships between the other operators

|magic method| operator |
|------------|:--------:|
|\_\_sub__| - |
|\_\_mul__| * |
|\_\_truediv__| / |
|\_\_floordiv__| // |
|\_\_mod__| % |
|\_\_pow__| ** |
|\_\_and__| & |
|\_\_xor__| ^ |
|\_\_or__| \| |


* if x hasn't implemented \_\_add__, and x and y are of different types, then y.\_\_radd__(x) is called. There are equivalent r methods for all magic methods in table
* If \_\_ne__ is not implemented, it returns the opposite of \_\_eq__

### object lifecycle
- Destruction of an object occurs when its reference count reaches zero
Reference count is the number of variables and other elements that refer to an object
- two (or more) objects can be referred to by each other only, and therefore can be deleted as well
- The del statement reduces the reference count of an object by one, and this often leads to its deletion
- In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary)

### data hiding
* Weakly private methods and attributes have a *single underscore* at the beginning
* it is mostly only a convention, and does not stop external code from accessing them
* Its only actual effect is that from module_name import * won't import variables that start with a single underscore
* Strongly private methods and attributes have a **double underscore** at the beginning of their names. This causes their names to be mangled, which means that they can't be accessed from outside the class
* Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod
```python
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg() # 7
print(s._Spam__egg) # 7  _Class__private_attr
print(s.__egg)  # AttributeError: 'Spam' object has no attribute '__egg'
print(_Spam__egg)

```
- How would the attribute __a of the class b be accessed from outside the class?
``_b__a``


### class methods

* are called by a class, which is passed to the cls parameter of the method
* A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor
* @classmethod
```python
class Rectangle:
    def __init__(self, width, height):
		self.width = width
		self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_lenght, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area()) # 25



class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        combined_cap = self.capacity + other.capacity
        combined_name = self.name + '&' + other.name
        return Juice(combined_name, combined_cap)

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)

```
### static methods
- don't receive additional arguments
- @staticmethod
```python

```
### properties
- customizing access to instance attributes
- @property
- method will be called instead of attribute with same name
- common use is to make it read-only

```python
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pinapple_allowed)
pizza.pineapple_allowed = True
```
#### setter/getter
- to define a setter you use decorator of the same name as property dot setter
- @skin_color.setter

```python
class Pizza:
    def __init__(self, toppings):
		self.toppings = toppings
		self._pineapple_allowed = False

	@property
	def pineapple_allowed(self):
		return self._pineapple_allowed
	
	@pineapple_allowed.setter
	def pineapple_allowed(self, value):
		if value:
			password = input("Enter the password: ")
			if password == "Sw0rdf1sh!":
				self._pineapple_allowed = value
			else:
				raise ValueError("Alert! Intruder!")
				
				
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


# simple game
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = " A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >=3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else: 
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg ="There is no {} here.".format(noun) 
    return msg

```
# regex

## regex functions
|function|desciption|
|--|:--:|
|re.match| determine whether it matches at the **beginning** of a string|
|re.search|finds a match of a pattern **anywhere** in the string|
|re.findall|returns a **list** of all substrings that match a pattern|
|re.iter| same as re.findall but returns an **iterator**
|re.sub| replace all (or count) occurences of pattern in string
|re.split(delim, string)| split string into list using delimiter|
```python

import re

pattern = r"pam"
match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())  # pam -> returns string matched = pam
    print(match.start())  # 4   -> returns start of first match
    print(match.end())    # 7   -> returns end of first match
    print(match.span())   # (4, 7) -> returns start & end of first match as tuple
	print(match.string)   # eggspamsausage -> returns string passed into function
	
	
# re.sub
str = "My name is David. Hi David."
pattern = r"David"
new_str = re.sub(pattern, "Patrick", str, count=1)
print(new_str)  # My name is Patrick. Hi David.
		

```
## metacharacters
|char|description|example|
|:--:|-----------|-------|
[]	|A set of characters	|"[a-m]"	|
|\	|Signals a special sequence (can also be used to escape special characters)	|"\d"	
|.	|Any character (except newline character)|	"he..o"	|
|^	|Starts with	|"^hello"	|
|$	|Ends with	|"world$"|	
|*	|Zero or more occurrences|	"aix*"	|
|+	|One or more occurrences	|"aix+"	|
|{}	|Exactly the specified number of occurrences|	"al{2}"	|
|\|	|Either or	|"falls|stays"	|
|()	|Capture and group|

## special sequences aka character classes
|Character|	Description|Example|
|---------|------------|-------|
\A	|Returns a match if the specified characters are at the beginning of the string|	"\AThe"	
\b	|Returns a match where the specified characters are at the beginning or at the end of a word	|r"\bain"
|||r"ain\b"	
\B	|Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word|	r"\Bain"
|||r"ain\B"	
\d	|Returns a match where the string contains digits (numbers from 0-9)|	"\d"	
\D	|Returns a match where the string DOES NOT contain digits|	"\D"	
\s	|Returns a match where the string contains a white space character|	"\s"	
\S	|Returns a match where the string DOES NOT contain a white space character|	"\S"	
\w	|Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	|"\w"	
\W	|Returns a match where the string DOES NOT contain any word characters|	"\W"	
\Z	|Returns a match if the specified characters are at the end of the string	|"Spain\Z"

## sets
| set| description|
|--|---|
[ ] | Contains a set of characters to match
[amk] | Matches either a, m, or k. It does not match amk
[a-z] | Matches any alphabet from a to z
[a\\-z] | Matches a, -, or z. It matches - because \ escapes it
[a-] | Matches a or -, because - is not being used to indicate a series of characters
[-a] | As above, matches a or -
[a-z0-9] | Matches characters from a to z and also from 0 to 9
[(+*)] | Special characters become literal inside a set, so this matches (, +, *, and )
[^ab5] | Adding ^ excludes any character in the set. Here, it matches characters that are not a, b, or 5

## groups
|group|description|
|-----|-----------|
( ) | Matches the expression inside the parentheses and groups it
(? ) | Inside parentheses like this, ? acts as an extension notation. Its meaning depends on the character immediately to its right
(?PAB) | Matches the expression AB, and it can be accessed with the group name
(?aiLmsux) | Here, a, i, L, m, s, u, and x are flags:
||a — Matches ASCII only
||i — Ignore case
||L — Locale dependent
||m — Multi-line
||s — Matches all
||u — Matches unicode
||x — Verbose
(?:A) | Matches the expression as represented by A, but unlike (?PAB), it cannot be retrieved afterwards
(?#...) | A comment. Contents are for us to read, not for matching
A(?=B) | Lookahead assertion. This matches the expression A only if it is followed by B
A(?!B) | Negative lookahead assertion. This matches the expression A only if it is not followed by B
(?<=B)A | Positive lookbehind assertion. This matches the expression A only if B is immediately to its left. This can only matched fixed length expressions
(?<!B)A | Negative lookbehind assertion. This matches the expression A only if B is not immediately to its left. This can only matched fixed length expressions
(?P=name) | Matches the expression matched by an earlier group named “name”
(...)\\1 | The number 1 corresponds to the first group to be matched. If we want to match more instances, use 1 up to 99 (1 = repeat the same thing)
```python

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"
# named group matching 'abc' followed by non-capturing group 'def' followed by 'ghi'
match = re.match(pattern, "abcdefghi")

if match:
    print(match.group("first"))  # abc
    print(match.groups())  # ('abc', 'ghi')


"""
\A and \Z match the beginning and end of a string
\b matches the empty string between \w and \W characters, or \w characters and -- the beginning or end of the string. Informally, it represents the boundary between words
\B matches the empty string anywhere else
\b(cat)\b" basically matches the word "cat" surrounded by word boundaries
"""

str = "Please contact info@sololearn.com for assistance"
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

```
# good to know
## tuple unpacking
- Tuple unpacking allows you to assign each item in an **iterable** (often a tuple) to a variable
- can be also used to swap variables by doing a, b = b, a
since b, a on the right hand side forms the tuple (b, a) which is then unpacked
- A variable that is prefaced with an asterisk (\*) takes all values from the iterable that are left over from the other variables
```python
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5, 6, 7, 8]
print(d)  # 9

```
## Ternary operator

```python
a = 7
b = 1 if a >= 5 else 42
print(b) # b = 1 cuz 7>=5

status = 1
msg = "logout" if status = 1 else "login"

b = 1 if 2+2 == 5 else 2
```
## more on else
* With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop)
```python
for i in range(10):
	if i == 999:
		break
else:
	print("this is executed bc i goes from 0 up to 9, not 999")
	

for i in range(10):
    if i == 5:
        break  # -> breaks loop, else block not run
else:
    print("this is NOT executed, i = 5 breaks the loop")
	
	
for i in range(10):
     if i > 5:
        print(i)
          break  # will print 6 & break
else:
     print("7")

```
* executed if NO ERROR occurs in TRY statement
```python
try:
    print(5 * 4/0)
except ZeroDivisionError:
    print("idiot")  # will print idiot :D
else:
    print("yay else ran") # did not run bc error ocurred
```
## `__main__`
- to make a file that can be both imported as a module and run as a script

* if python is running module (source file) as main program it sets \_\_name__ = "\_\_main__"
* if file imported as module \_\_name__ = "that_modules_name"
    * code in if `__name__ == "__main__":` block won't run

# Packaging
- involves use of the modules setuptools and distutils
- should contain a file called `__init__.py`
- parent dir has to have: `README.txt LICENSE.txt setup.py`

```python
# example
SoloLearn/
   LICENSE.txt
   README.txt
   setup.py
   sololearn/
      __init__.py
      sololearn.py
      sololearn2.py
```
## setup.py
- contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip
- After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer)
- To build a **source distribution**, use the command line to navigate to the directory containing setup.py, and run the command `python setup.py sdist`
- Run `python setup.py bdist` or, for Windows, python setup.py bdist_wininst to build a **binary distribution**
- Use `python setup.py register`, followed by `python setup.py sdist upload` to upload a package
- Finally, install a package with `python setup.py install`
```python
# example setup.py
from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)

```
>***
>**NOTE**
>For Windows, many tools are available for converting scripts to executables. For example, >py2exe, can be used to package a Python script, along with the libraries it requires, into a >single executable. PyInstaller and cx_Freeze serve the same purpose
>
>For Macs, use py2app, PyInstaller or cx_Freeze.

>***
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
>***
>**NOTE**
>
>***



id: 8059aa2f8e0f47fa88692039f800f7dc
parent_id: 9dc5f510516c48d4be44e2662f771a28
created_time: 2021-03-15T15:48:39.602Z
updated_time: 2021-03-20T11:02:26.270Z
is_conflict: 0
latitude: 0.00000000
longitude: 0.00000000
altitude: 0.0000
author: 
source_url: 
is_todo: 0
todo_due: 0
todo_completed: 0
source: joplin-desktop
source_application: net.cozic.joplin-desktop
application_data: 
order: 0
user_created_time: 2021-03-15T15:48:39.602Z
user_updated_time: 2021-03-20T11:02:26.270Z
encryption_cipher_text: 
encryption_applied: 0
markup_language: 1
is_shared: 0
type_: 1
