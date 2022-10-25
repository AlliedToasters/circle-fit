# Circle-Fit
## Simple Circle Fitting Library for Python
Fitting circles is a simple problem. Given a set of points in 2-D space, let's find a "best fit" circle. A simple 
least-squares algorithm is a simple and effective solution. A novel algorithm came out in 2011 called 
["Hyper Fit"](https://www.sciencedirect.com/science/article/pii/S0167947310004809?via%3Dihub) by Kanatani, et al.

This library implements the hyper fit algorithm, as well as a range of other circle fitting algorithms:

```
- hyperLSQ()      : Least squares circle fit with "hyperaccuracy" by Kenichi Kanatani, Prasanna Rangarajan
- standardLSQ()   : Least squares circle fit
- riemannSWFLa()  : Riemann circle fit, SWFL version A
- lm()            : Levenberg-Marquardt in the full (a,b,R) parameter space
- prattSVD()      : Algebraic circle fit by V. Pratt
- taubinSVD()     : Algebraic circle fit by G. Taubin
- hyperSVD()      : Algebraic circle fit with "hyperaccuracy"
- kmh()           : Consistent circle fit by A. Kukush, I. Markovsky, S. Van Huffel
```
## Installation
```
pip install circle-fit
```

## Usage
### Prepare the Data
Your data must have at least two points in 2-D space. Circle-fit expects an 2D List or numpy ndarray of shape 
`(n, 2)`, where n is the number of points in your dataset.<br>
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
xc, yc, r, sigma = hyperLSQ(point_coordinates)
plot_data_circle(point_coordinates, xc, yc, r)
```
