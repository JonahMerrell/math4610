# Homework2<br>

## [Back](../)

- [x] [Task 1](#task-1)
- [x] [Task 2](#task-2)
- [x] [Task 3](#task-3)
- [x] [Task 4](#task-4)
- [x] [Task 5](#task-5)


### Task 1
For this task, we were asked to implement the newton iteration.

- Code:
  - [root_solve_newton.py](Task1/root_solve_newton.py)
- Software Manual entry:
  - [root_solve_newton](../software_manual/root_solve_newton.md)

### Task 2
For this task, we were asked to implement the secant iteration.

- Code:
  - [root_solve_secant.py](Task2/root_solve_secant.py)
- Software Manual entry:
  - [root_solve_secant](../software_manual/root_solve_secant.md)

### Task 3
For this task, we were asked to compare the 4 methods for root finding (functional iteration, bisection, Newton's method, and the secant method) <br>

I created a program that performs the 4 methods on the same equation: x cosh(x) + x<sup>3</sup> - pi = 0<br>

      The true root to the equation x * cosh(x)+ x^3 - pi is 1.0963278
      Using the fixed point iteration, the solution was N/A, which took N/A iterations.
      Using the bisection iteration, the solution was 1.0963282585144043, which took 22 iterations.
      Using the newton iteration, the solution was 1.0963277882922402, which took 4 iterations.
      Using the secant iteration, the solution was 1.096327788292231, which took 5 iterations.
	  
- Code:
  - [compare_root_methods_test.py](Task3/compare_root_methods_test.py)

  
### Task 4
For this task, we were asked to implement a hybrid method that uses the bisection iteration and newton's iteration.

- Code:
  - [root_solve_newton_hybrid.py](Task4/root_solve_newton_hybrid.py)
- Software Manual entry:
  - [root_solve_newton_hybrid](../software_manual/root_solve_newton_hybrid.md)

  
### Task 5
For this task, we were asked to implement a hybrid method that uses the bisection iteration and the secant iteration.

- Code:
  - [root_solve_secant_hybrid.py](Task5/root_solve_secant_hybrid.py)
- Software Manual entry:
  - [root_solve_secant_hybrid](../software_manual/root_solve_secant_hybrid.md)
 

