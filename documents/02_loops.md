## Loops

In coding loops are something that help you repeat your code. In python, we have 2 types of loops- a for loop and a while loop.

## For Loop
```python
for i in range(10):
    print("hello")
```
This is how we use a for loop. This code will print hello 10 times because in range we have 10. 

```python
for i in range(10):
    print(i)

```
If we print the variable i instead of "hello" then it will show us numbers from 0 to 9. Why? Because range gives us numbers from 0-9(because if you write range(10)) and for loop helps you go through the numbers from 0-9.
One might wonder, why are getting numbers from 0 to 9 if write 10 in the range. Let's understand a few things about range function. 

```python
for i in range(1, 10):
    print(i)
```

If we try this code we will get numbers from 1 to 9 because in range we have 1 and 10. why not 10? because the way range function works is that 10 is not included in the range, if you want 10 you have to write range(1, 11).
So, basically we always have to write 1 more than what we need. 
If we write range(10) only 1 number in the range function, it automatically starts the range from 0.

```python
for i in range(1, 10, 2):
    print(i)
```
This code will give us values starting from 1, but next number instead of being 2 will be 3.
why?
Because this time we have written a third number in the range which is 2. This means you want to increment numbers by 2 instead of 1.
So, we will get numbers 1, 3, 5, 7, 9.
```python
for i in range(10, 1, -1):
    print(i)
```

This code will give us numbers from 10 to 2 because of -1 step-interval at the end.


We can also use loops to traverse a list or string.

```python
foods = ["poha", "upma", "ice cream"]

for i in foods:
    print("Gunjan loves",i)
```


Here, writing the name of a list instead of range functions lets the computer know you want to go through the list. Here, the first loop runs i will be "poha", second time "upma" and third time "ice cream".


```python
name = "Gunjan Redu"
for i in name:
    print(i)
```
Here i will go through the name string .



## While Loop


while loop runs as long the condition inside it is true.
```python
while True:
    print("Gunjan is so cool")

```
This is forever loop because the there's no condition here instead just a boolean value True which never happens to be False so the loop never stops, you have to press Ctrl+C to force it to stop

```python
while False:
    print("Gunjan is so cool")

```

This loop never starts running because while already has False in it. 

```python
i =0
while i<5:
    print("Gunjan is so cool")
    i = i + 1

```

This loop will run five times.Here, i starts at 0, and every time the loop runs, it prints the line and then i grows by 1. When i becomes 5, the condition i < 5 is no longer true, so the loop stops. The line i = i + 1 is what saves this loop from being a forever loop.

## Try it yourself

Print the multiplication table of 5 using a for loop.

```python
for i in range(1, 11):
    print(5, "x", i, "=", 5 * i)
```