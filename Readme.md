Spline Interpolation
=====================

Implemented methods
1. Linear spline
2. Quadratic spline
3. Natural cubic spline
4. Not-a-knot cubic spline
5. Periodic cubic spline
6. Clamped cubic spine

Running the program
>   python main.py

Input has to given in the input.txt file. Sample input file has been provided below
>   
    -1.000 0.0385
    -0.500 0.1379
    0.000 1.0000
    0.500 0.1379
    1.000 0.0385

    -0.8000
    -0.2000
    0.2000
    0.8000

    -1.0 1.5

Till the first line break data points have to be provided in 'x y' form.

Then the test points have to be given.

The last line is for only the clamped spline interpolation. They are s_0 and s_n respectively. Can be ommitted if using other methods

The output will be saved to outfile