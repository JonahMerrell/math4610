# Homework4<br>

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
For this task, we were asked to determine if there might be an advantage to using one of the hybrid methods (developed in the previous tasksheet) for root finding.<br>

In order to compare bisection method, newton's method, and the bisection method, I ran each of their multiple-root finding versions on the same equation and with the the same tolerance. I then compared the execution time of each of them. The results are shown below:

|   Root-finding Algorithm           |    Execution Time    |
|   root_solve_bisection_interval    |  0.1910111904144287  |
|   root_solve_newton_intervals      |  0.1160066127777099  |
|   root_solve_secant_intervals      |  0.128007173538208   |

We can see from the results above that Newton's method performed the fastest compared to the other 2 methods. The secant method, although slower, didnt perform that much slower than Newton's method. (Probably because the 2 methods are very similar). Had the worst performance, meaning that the bisection method converges slower than Newton's method or the secant method.


