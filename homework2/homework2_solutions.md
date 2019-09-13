# Homework1<br>

## [Back](../)

- [x] [Task 1](#task-1)
- [x] [Task 2](#task-2)
- [x] [Task 3](#task-3)
- [x] [Task 4](#task-4)
- [x] [Task 5](#task-5)
- [x] [Task 6](#task-6)
- [x] [Task 7](#task-7)
- [x] [Task 8](#task-8)
- [x] [Task 9](#task-9)
- [x] [Task 10](#task-10)

### Task 1
For this task, we were asked to set up a root finding problem for the equation: x cosh(x) + x<sup>3</sup> = pi

__Solution__:

Given x cosh(x) + x<sup>3</sup> = pi <br>
	  x cosh(x) + x<sup>3</sup> - pi = 0 <br>
		Let f(x) = xcosh(x) + x<sup>3</sup> - pi<br>
		
Thus, the root finding problem is to find x such that f(x) = 0

### Task 2
For this task, we were asked to set up at least two associated fixed point iteration for the equation: x cosh(x) + x<sup>3</sup> = pi

__Fixed-point Iteration__
x = x + f(x)
x<sub>1</sub> = x<sub>0</sub> + f(x), given an intital guess x<sub>0</sub> <br>
Let g(x<sub>k</sub>) = x<sub>k</sub> + f(x<sub>k</sub>) <br>
x<sub>k + 1</sub> = g(x<sub>k</sub>) <br>

