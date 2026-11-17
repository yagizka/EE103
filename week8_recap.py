def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)
def take_square(x):
    return x ** 2
print("Derivative with normal function: ", estimate_derivative(take_square, 3))

square_lambda = lambda x: x ** 2
print("Derivative with lambda function: ", estimate_derivative(square_lambda, 3))