# Circle-Fit
## Simple Circle Fitting Library for Python
Fitting circles is a simple problem. Given a set of points in 2-D space, let's find a "best fit" circle. A simple least-squares algorithm is a simple and effective solution. A novel algorithm came out in 2011 called ["Hyper Fit"](https://www.sciencedirect.com/science/article/pii/S0167947310004809?via%3Dihub) by Kanatani, et al.

## Installation
```
pip install circle-fit
```

## Usage
### Prepare the Data
Your data must have at least two points in 2-D space. Circle-fit expects an array (or similar structure) of shape `(n, 2)`, where n is the number of points in your dataset.<br>
There are two algorithms available: `hyper_fit` and `least_squares_circle`. Both return four values:
```
- xc : x-coordinate of solution center (float)
- yc : y-coordinate of solution center (float)
- R : Radius of solution (float)
- variance or residual (float)
```