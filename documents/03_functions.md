## Functions


In Python, a function is a reusable block of code that executes only when called.
In coding we have a concept called DRY- do not repeat yourself. Repeating your code is considered a bad practice. And functions help us keep our code DRY.
How?


```python
def greeting():
    print("Gunjan is so smart")
    
greeting()

```
This is how we create a function write def, then write the name of the function followed by the round brackets.
But this wouldn't work until we call the function.To call the function we need to put the name of the function followed by set of parenthesis or as kids like to call it round brackets.
You can call the function as many times as you like. S, everytime you need this code you don't need to write it all over again, we can just call the function. This saves you alot of time and also keeps your code DRY.

We can also customize the functions:

```python
def greeting(x):
    print(x, "is so smart")

greeting("Gunjan")
greeting("Taylor")
```
Here, x is called a parameter in the function, we pass its value while calling the function. In the function call we have "Gunjan" and "Taylor" are 2 different values passed to the function in 2 different function calls.


We can also have functions with multiple parameters:
```python
def calculate(a, b):
    print(a+ b)

calculate(4, 10)

```
Here, the calculate function has 2 parameters a and b, when you call the function you must exactly two values, one for each parameter. The first value in the function call 4 is given to the first parameter which is a and second value 10 is given to the second parameter.

## return statement

The variables we create inside a function are called local variables, which means you can't access them outside the function.That's why we use return values from the function using a return statement. 

```python
def calculate():
    a = 8+6             # a is a local variable, accessing outside would give us an error
    return  a


b = calculate()   # value of a is assigned to b as soon as we call the function
print(b)
```

print() displays a value on the screen, while return sends a value back from a function so you can store it in a variable or use it in another calculation. For example, print(5 + 3) displays 8, but return 5 + 3 inside a function lets you reuse the result later. Remember: print shows a result, while return gives a result back to the code that called the function.

## Try It Yourself

Create a function called add_numbers that takes two numbers as arguments and returns their sum.
Call the function with 5 and 3, store the result in a variable, and print it.

```python
def add_numbers(a, b):
    
    # Write your code here

result = add_numbers(5, 3)
print(result)

```





