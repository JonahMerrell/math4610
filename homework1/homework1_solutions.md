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

### Task 1
For this task, we were asked to email our link to our Github page.

- Link to my github page: [https://jonahmerrell.github.io/math4610/](https://jonahmerrell.github.io/math4610/)

### Task 2
For this task, we were asked to email our instructor to indicate that we have created the math4610 repository on our github account.

- Link to my github Repository: [https://github.com/JonahMerrell/math4610](https://github.com/JonahMerrell/math4610)

### Task 3
For this task, we were asked to email our instructor as to which command line environment we will use in the course.

- For this class, I will be using the Windows command line environment.

### Task 4
For this task, we were asked to write code in the language you intend to use in the course that when executed will inform our instructor as to the language that will be used.

- Code:
  - [printCodeLanguage.py](Task4/printCodeLanguage.py)

### Task 5
For this task, we were asked to create a table of contents for the homework tasks. In my case, my table of contents is
set up to be the homepage for my github pages website.

- Link to my Table of Contents: [https://jonahmerrell.github.io/math4610/](https://jonahmerrell.github.io/math4610/)

### Task 6
For this task, we were asked to approximate a derivative using the central difference quotient to document 
how the error reduces as h decreases until machine precision causes problems. 

- Code:
  - [printCodeLanguage.py](Task6/test_computation_error.py)
- Software Manual entry:
  - [printCodeLanguage](../software_manual/test_computation_error.md)
  
  Using test_computation_error, I learn that as h gets smaller, the approximation for the derivative improves in precision until 
  a certain point. After this point, the approximation for the derivative starts to become worse, since the values involved in 
  the computation with h exceed machine precision. Here are a few examples to demonstrate:
  
|   h    |    e^pi          |      Relative      |
|        |  Approximation   |       Error        |
|   1    | 27.19496960378651| 0.17520119364380132|
|  2^-4  | 23.15576113064367| 0.00065116883506992|
|  2^-8  | 23.14075148264874| 2.5431334490344e-06|
|  2^-12 | 23.14069286266021| 9.9340564228831e-09|
|  2^-16 | 23.14069263357669| 3.4459677102833e-11|
|  2^-20 | 23.14069263264537| 3.4459677102833e-11|
|  2^-24 | 23.14069262146949| 4.8873959191347e-10|
|  2^-28 | 23.14069271087646| 3.3748857792838e-09|
|  2^-32 | 23.14069366455078| 4.4586889738722e-08|
  
### Task 7
For this task, we were asked to implement two separate routines to compute (1) the absolute error between a number
 and an approximation of that number and (2) the relative error between a number and an approximation of that number.

- Code:
  - [abs_error.py](Task7/abs_error.py)
  - [rel_error.py](Task7/rel_error.py)
- Software Manual entry:
  - [abs_error](../software_manual/abs_error.md)
  - [rel_error](../software_manual/rel_error.md)
  
### Task 8
For this task, we were asked to implement a shared library for our code, as well implemement 2 methods that measure 
the machine epsilon for a double and a float.

- Code:
  - [calculate_double_float_precision.py](Task8/calculate_double_float_precision.py)
  - [calculate_single_float_precision.py](Task8/calculate_single_float_precision.py)
- Software Manual entry:
  - [calculate_double_float_precision](../software_manual/calculate_double_float_precision.md)
  - [calculate_single_float_precision](../software_manual/calculate_single_float_precision.md)

### Task 9
For this task, we were asked to write a main program that computes the derivative of the exponential function, e^x, at
 the point x=pi, and then report the absolute and relative error.

- Code:
  - [compute_exp_pi.py](Task9/compute_exp_pi.py)
- Software Manual entry:
  - [compute_exp_pi](../software_manual/compute_exp_pi.md)
