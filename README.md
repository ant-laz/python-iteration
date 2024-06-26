# python iteration
A tutorial on understanding the main ways to do iteration with python

## Setting up your environment

### Python 3.10+

This is a hands on workshop, please come ready with Python 3.10+ installed: 
 * use the Python official [downloads](https://www.python.org/downloads/)
 * use pyenv
 * follow the instructions for Google [Cloud](https://cloud.google.com/python/docs/setup)
 * ...or whatever you prefer ! 

### Development Environment

This is a hands on workshop, please come ready with a development environment:
 * VSCode
 * PyCharm
 * GCP cloud shell 
 * GCP cloud shell editor
 * GCP workstation
 * ...or whatever you prefer ! 


### Python Virtual Env

With *python* pointing at python 3.10 run the following.

Create a virtual environment
```
python -m venv venv
```
Activate the virtual environment.
```
source venv/bin/activate
```

While activated, your `python` and `pip` commands will point to the virtual environment,
so any changes or install dependencies are self-contained.

### Initialize code

Execute form the root of this repo to initialze the pipeline code.

First, update pip before installing dependencies, it's always a good idea to do this.
```sh
pip install -U pip
```

Install the project as a local package, this installs all the dependencies as well.
```
pip install -e .
```

check everything is working
```
python main.py
```

You should see
```py
we're up and running
```



## pattern 1

It is common to see iteration like so

```py
for x in y:
    do_something_with(x)
```
### pattern 1 - theory

How does this work & for what kind of types can ```y``` be ? 

Recall that Python has [built-in types](https://docs.python.org/3/library/stdtypes.html#)

 * numeric types: int, float, complex
 * boolean type: bool
 * sequence types: list, tuple, range
 * text sequence types: str
 * binary sequence types: bytes, bytearray, memoryview
 * set types: set, frozenset
 * mapping types: dict


And Python has specialized [container data types](https://docs.python.org/3/library/collections.html) that include : 

 * namedtuple
 * deque (short for double ended queue)
 * OrderedDict

Can all types be used as ```y``` in the pattern above ? No.

Consider the following

```py
my_int = 123
for digit in my_int:
    print(digit)
```
we get the following error

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

How do we make sense of the error above ? Luciano Ramalho, in the book Fluent Python, suggests an approach called
"The Python Data Model" which describes how the "python interpreter invokes special 
methods to perform basic object operations, often triggered by special syntax. The special methods names are always written with leading & trailing double underscores".

 * For example one "special" methods is ```__len__()``` which is called by the Python interpreter when evaluating code like ```len(my_object)```.

 * Another example of a "special" methosd is ```__getitem__(key)``` which is called by the Python interpreter when evaluating code ```obj[key]```.

 * Another example of a "special" methosd is ```__repr__()``` which is called by the Python interpreter when evaluating code ```str(obj)```.

Ok, so back to our error then. As per the offical Python glossary an [iterable](https://docs.python.org/3/glossary.html#term-iterable) is a "an object capable of returning its members one at a time". 

So the built-in numeric type ```int``` does not have this property, it is not capable of
return its members one at a time. Hoever the the built-in sequence type ```list``` does 
have this property as per the example below, which executes without error.

```py
my_int_list = [1,2,3]
for digit in my_int_list:
    print(digit)
```

Ok, so which [built-in types](https://docs.python.org/3/library/stdtypes.html#) & [container data types](https://docs.python.org/3/library/collections.html) are [iterable](https://docs.python.org/3/glossary.html#term-iterable) ? Many of them, including:

 * sequence types: list, tuple, range
 * text sequence types: str
 * set types: set, frozenset
 * mapping types: dict

How can I make my own classes iterable ?  As per the offical Python [glossary](https://docs.python.org/3/glossary.html#term-iterable), "objects of any classes you define with an ```__iter__()```
method" are iterable. 

How do you implement an ```__iter__()``` method ? As per the offical [docs](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__), this method returns an [iterator](https://docs.python.org/3/glossary.html#term-iterator) object.


Huh?!

What's is an iterator then? 

An iterator is an object that is used to traverse through some sequence of items. 
This process of traversal is called iteration.  An interator is an ojbect that 
implements the [iterator protocol](https://docs.python.org/3/library/stdtypes.html#typeiter). 

This protocol is comprised of dunder methods : ```__iter__()``` and ```__next__()```.

 * ```__iter__()``` - return the iterator object itself, for details see [docs](https://docs.python.org/3/library/stdtypes.html#typeiter). Note that iterators needs to return an iterator so that iterators are iterable & usable in for loops. Confused ? See the worked example below.

 * ```__next__()``` - return next item or an exception if none remain, for details see [docs](https://docs.python.org/3/library/stdtypes.html#typeiter)

Let's use this new knowledge to understand our list example:

```py
my_int_list = [1,2,3]
for digit in my_int_list:
    print(digit)
```

Can be rewritten using our new knowledge of iterable & iterators.
```py
my_int_list = [1,2,3]

numbers_iterator = my_int_list.__iter__()

while True:
  try:
    print(numbers_iterator.__next__())
  except StopIteration: 
    break
```

Which one would you like to be writing everyday? 

Thank goodness we have the for statement, right ? 


Let's get some practice with these new ideas with the following exercises.

### pattern 1 - exercise A

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern1.TestStarBuzzCoffeeOrders.test_ordering_a_coffee
```

You will get an error like: 
```shell
ERROR: test_ordering_a_coffee (test.test_pattern1.TestStarBuzzCafeOrders)
Your new start-up StarBuzz Cafe needs to take orders!
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../test/test_pattern1.py", line 31, in test_ordering_a_coffee
    actual_num_orders: int = len(cafe_orders)
TypeError: 'NoneType' object cannot be interpreted as an integer

----------------------------------------------------------------------
Ran 1 test in 0.001s
```

Using the theory above, modify pattern1.py to make the test pass.

### pattern 1 - exercise B

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern1.TestStarBuzzCoffeeOrders.test_looping_through_all_orders
```
You will get an error like: 
```shell
ERROR: test_looping_through_all_orders (test.test_pattern1.TestStarBuzzCafeOrders)
You need to loop through all orders.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../test/test_pattern1.py", line 49, in test_looping_through_all_orders
    for order in cafe_orders:
TypeError: iter() returned non-iterator of type 'NoneType'

----------------------------------------------------------------------
Ran 1 test in 0.000s
```

Using the theory above, modify pattern1.py to make the test pass.

### pattern 1 - exercise B

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern1.TestStarBuzzCoffeeOrders.test_checking_order_queue_at_idx
```

You will get an error like: 
```shell
FAIL: test_checking_order_queue_at_idx (test.test_pattern1.TestStarBuzzCafeOrders)
Your baristra needs to checks orders at random.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../test/test_pattern1.py", line 68, in test_checking_order_queue_at_idx
    self.assertEqual(expected_order_retreived, actual_order_retreived)
AssertionError: 'latte' != None

----------------------------------------------------------------------
Ran 1 test in 0.000s
```

Using the theory above, modify pattern1.py to make the test pass.

## pattern 2

It is common to see iteration like so

```py
for i, x in enumerate(y):
    do_something_with(i, x)
```

### pattern 2 - theory

So, what's going on here ? 

As per the docs, Python has a number of [built-in functions](https://docs.python.org/3/library/functions.html)

And one of those functions is [enumerate](https://docs.python.org/3/library/functions.html#enumerate)

As per the docs, enumerate takes as input an "iterable (which) must be a sequence, 
an iterator, or some other object which supports iteration."

From pattern 1 & its exercises, we know what an iterable is & what an iterator is too.

Go through the exercises below to get some experience with ```enumerate```.


### pattern 2 - exercise A

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern2.TestStarBuzzCoffeeDisplay.test_display_all_orders
```

You will get an error like: 
```shell
======================================================================
ERROR: test_display_all_orders (test.test_pattern2.TestStarBuzzCoffeeDisplay)
Customers need to know their place in the queue at StarBuzz Coffee !
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern2.py", line 34, in test_display_all_orders
    actual_display_info = str(cafe_display)
TypeError: __str__ returned non-string (type NoneType)

----------------------------------------------------------------------
```

Using the theory above, modify pattern2.py to make the test pass.

### pattern 2 - exercise B

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern2.TestStarBuzzCoffeeDisplay.test_hiding_initial_test_orders
```

You will get an error like: 
```shell
======================================================================
ERROR: test_hiding_initial_test_orders (test.test_pattern2.TestStarBuzzCoffeeDisplay)
Hide the 2 coffees the baristas have before opening time !
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern2.py", line 54, in test_hiding_initial_test_orders
    actual_display_info = str(cafe_display)
TypeError: __str__ returned non-string (type NoneType)

----------------------------------------------------------------------
```

Using the theory above, modify pattern2.py to make the test pass.

## pattern 3

It is common to see iteration like so

```py
for key, value in d.items():
    do_something_with(key, value)
```

### pattern 3 - theory

So what's going on here then ? 

Can ```d``` by any type ? What about a ```list``` ? 

```shell
l = [1,2,3]
for key, value in l.items():
  print(key)
  print(value)
```

No! We get an error

```shell
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'items'
```

It turns out that ```d``` can only be a ```dict```. ```dict.items()``` is called a 
"dictionary view". 

As per the docs for [dict.items()](https://docs.python.org/3/library/stdtypes.html#dict.items)
this method returns a [view object](https://docs.python.org/3/library/stdtypes.html#dict-views)
which gives the items in the dict as ```(key,value)``` pairs.

So how can view objects be used in the ```for x in y``` pattern ? As per the docs, 
"Dictionary views can be iterated over to yield their respective data". Furthermore, 
these dictionary views have an ```iter(dictview)``` method which return an ```iterator.```
From the previous section, we learnt that this is what is required to be an ```iterable```
and to be used in the ```for x in y``` pattern. This is how dictionary view objects, 
like ```dict.items```, ```dict.keys``` and ```dict.values``` are all ```iterable```
and can be used in the ```for x in y``` pattern of iteration. 

Let's get some practice with ```dict.items()``` with the following exercises.

### pattern 3 - exercise A

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern3.TestStarBuzzInventory.test_full_inventory_report
```

You will get an error like: 
```shell
======================================================================
ERROR: test_full_inventory_report (test.test_pattern3.TestStarBuzzInventory)
The manager needs to know everything in the inventory !
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern3.py", line 33, in test_full_inventory_report
    actual_inventory_report = str(cafe_inventory)
TypeError: __str__ returned non-string (type NoneType)

----------------------------------------------------------------------
```

Using the theory above, modify pattern3.py to make the test pass.

### pattern 3 - exercise B

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern3.TestStarBuzzInventory.test_out_of_stock_inventory_report
```

You will get an error like: 
```shell
======================================================================
FAIL: test_out_of_stock_inventory_report (test.test_pattern3.TestStarBuzzInventory)
The manager needs to know what out of stock items to re-order !
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern3.py", line 51, in test_out_of_stock_inventory_report
    self.assertEqual(expected_inventory_report, actual_inventory_report)
AssertionError: 'cream' != None

----------------------------------------------------------------------
```

Using the theory above, modify pattern3.py to make the test pass.

## pattern 4

It is common to see iteration like so

```py
for x in range(y):
    do_something_with(x)
```

### pattern 4 - theory

Ok, so what's going on here then ? 

```range``` is on the Python [built-in methods](https://docs.python.org/3/library/functions.html). 

As per the more detailed documentation on [ranges](https://docs.python.org/3/library/stdtypes.html#typesseq-range) we understand that ```range``` generates an "immutable sequence 
of numbers.

Amazing, right ? 

But, how does this ```range``` method work with the ```for x in y``` pattern ? 

Recall that all ```sequence``` types are [iterable](https://docs.python.org/3/glossary.html#term-iterable)
and so all ```sequence``` types, like those returned by ```range``` work with the 
```for x in y``` pattern.

Let's get some practices with iteration using ```range``` in the exercises below.

### pattern 4 - exercise A

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern4.TestStarBuzzCoffeeBilling.test_total_revenue_report
```

You will get an error like: 
```shell
======================================================================
FAIL: test_total_revenue_report (test.test_pattern4.TestStarBuzzCoffeeBilling)
Your new start-up StarBuzz Coffee needs to report on all transactions!
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern4.py", line 34, in test_total_revenue_report
    self.assertEqual(expected_total_revenue, actual_total_revenue)
AssertionError: 3 != None

----------------------------------------------------------------------
```

Using the theory above, modify pattern4.py to make the test pass.

### pattern 4 - exercise B

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern4.TestStarBuzzCoffeeBilling.test_vip_program_promotion
```

You will get an error like: 
```shell
======================================================================
FAIL: test_vip_program_promotion (test.test_pattern4.TestStarBuzzCoffeeBilling)
A new promotion invites all odd numbered customers to a new VIP program!
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern4.py", line 57, in test_vip_program_promotion
    self.assertEqual(expected_vip_invitee_list, actual_vip_invitee_list)
AssertionError: '(555)(988)' != None

----------------------------------------------------------------------
```

Using the theory above, modify pattern4.py to make the test pass.

## pattern 5

It is common to see iteration like so

```py
for x, y in zip(a, b):
    do_something_with(x, y)
```

### pattern 5 - theory

So what's going on here? 

As per the docs, ```zip``` is a Python [built-in function](https://docs.python.org/3/library/functions.html)

As per the [zip docs](https://docs.python.org/3/library/functions.html#zip) : 

 * "```zip``` Iterates over several iterables in parallel, producing tuples with an item from each one."
 * "```zip``` returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables." 

 Having completed the above exercises we should understand some of the terms mentioned 
 here. We can pass as input to ```zip``` iterables such as ```list``` and ```str```.

 Because ```zip``` returns an iterator we can use it in the ```for x in y``` pattern.

 Let's get some practice with ```zip``` through the exercises below.


### pattern 5 - exercise A

Run the unit-test for this exercise.

```shell
python -m unittest test.test_pattern5.TestStarBuzzDisplayCoffeeAndFood.test_display_all_orders
```

You will get an error like: 
```shell
======================================================================
ERROR: test_display_all_orders (test.test_pattern5.TestStarBuzzDisplayCoffeeAndFood)
Customers need to see both their food & coffee orders on the big screen!
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../python-iteration/test/test_pattern5.py", line 33, in test_display_all_orders
    actual_display_info = str(cafe_display)
  File "../python-iteration/src/pattern5.py", line 37, in __repr__
    return str(self.order_system)
TypeError: __str__ returned non-string (type NoneType)

----------------------------------------------------------------------
```

Using the theory above, modify pattern5.py to make the test pass.



