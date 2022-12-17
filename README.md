![LICENCE](https://img.shields.io/github/license/AlliedToasters/circle-fit)
[![Flake8](https://github.com/AlliedToasters/circle-fit/actions/workflows/flake8.yml/badge.svg)](https://github.com/AlliedToasters/circle-fit/actions/workflows/flake8.yml)
[![PyTest](https://github.com/AlliedToasters/circle-fit/actions/workflows/PyTest.yml/badge.svg)](https://github.com/AlliedToasters/circle-fit/actions/workflows/PyTest.yml)
![Version](https://img.shields.io/pypi/v/circle-fit)
![Python](https://img.shields.io/pypi/pyversions/circle-fit)
# Circle-Fit
## A Circle Fitting Library for Python
Given a collection of points in 2D space, a common problem is finding the parameters of a circle that best approximate 
these points. This library implements a collection of different circle fitting algorithms:

```
- hyperLSQ()      : Least squares circle fit with "hyperaccuracy" by Kenichi Kanatani, Prasanna Rangarajan
- standardLSQ()   : Least squares circle fit, standard version.
- riemannSWFLa()  : Riemann circle fit, SWFL version A
- lm()            : Levenberg-Marquardt in the full (a,b,R) parameter space
- prattSVD()      : Algebraic circle fit by V. Pratt
- taubinSVD()     : Algebraic circle fit by G. Taubin
- hyperSVD()      : Algebraic circle fit with "hyperaccuracy"
- kmh()           : Consistent circle fit by A. Kukush, I. Markovsky, S. Van Huffel
```

Most of these algorithms are based on the original MATLAB implementations by Nikolai Chernov: 
https://people.cas.uab.edu/~mosya/cl/MATLABcircle.html

Each algorithm may work better in specific cases. If you are in doubt about which to use, `taubinSVD()`
is a good starting point.

## Installation
`circle-fit` is available from PyPi. Run the following in a command line terminal:
`pip install circle-fit`

## Example
Fit a circle to four `(x,y)` points.
```
from circle_fit import taubinSVD
point_coordinates = [[1, 0], [-1, 0], [0, 1], [0, -1]]
xc, yc, r, sigma = taubinSVD(point_coordinates)
```

## Data format
Your data must have at least two points in 2-D space. The algorithms in `circle-fit` expects either 
a 2D List or numpy ndarray of shape `(n, 2)`, where n is the number of points in your dataset.

All the algorithms available in this library return four values:
```
- xc    : x-coordinate of solution center (float)
- yc    : y-coordinate of solution center (float)
- r     : Radius of solution (float)
- sigma : Residual error of solution (float)
```

### View the fit
The function `plot_data_circle(coords, xc, yc, r)` can be used to open a plot window which shows you data points with
a circle fit overlaid on top. Example use:
```
xc, yc, r, sigma = taubinSVD(point_coordinates)
plot_data_circle(point_coordinates, xc, yc, r)
```

### Contributors and Maintainers
This library is a community collaboration, all work is voluntary.

#### To Contribute
Please open a pull request with the changes you would like to contribute ([example](https://github.com/AlliedToasters/circle-fit/pull/10))

#### Contact
As we are volunteers, please be patient when requesting support. You can either open an issue if you think you've found a bug with the code, or contact one of us directly if you have a user issue:

 - michael.r.klear@gmail.com
 - mag.lauritzen@gmail.com

