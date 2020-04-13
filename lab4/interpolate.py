import numpy as np
import matplotlib.pyplot as plt


def jacobi(A, b, x0, tol, n_iterations=300):
    n = A.shape[0]
    x = x0.copy()
    x_prev = x0.copy()
    counter = 0
    x_diff = tol+1
    
    while (x_diff > tol) and (counter < n_iterations):
        for i in range(0, n):
            s = 0
            for j in range(0,n):
                if i != j:
                    s += A[i,j] * x_prev[j] 
            
            x[i] = (b[i] - s) / A[i,i]

        counter += 1
        x_diff = (np.sum((x-x_prev)**2))**0.5 
        x_prev = x.copy()

    return x

def cubic_spline(x, y, tol = 1e-100):
    x = np.array(x)
    y = np.array(y)

    if np.any(np.diff(x) < 0):
        idx = np.argsort(x)
        x = x[idx]
        y = y[idx]

    size = len(x)
    delta_x = np.diff(x)
    delta_y = np.diff(y)
    
    A = np.zeros(shape = (size,size))
    b = np.zeros(shape=(size,1))
    A[0,0] = 1
    A[-1,-1] = 1
    
    for i in range(1,size-1):
        A[i, i-1] = delta_x[i-1]
        A[i, i+1] = delta_x[i]
        A[i,i] = 2*(delta_x[i-1]+delta_x[i])
        b[i,0] = 3*(delta_y[i]/delta_x[i] - delta_y[i-1]/delta_x[i-1])

    c = jacobi(A, b, np.zeros(len(A)), tol = tol, n_iterations=1000)
    
    d = np.zeros(shape = (size-1,1))
    b = np.zeros(shape = (size-1,1))
    for i in range(0,len(d)):
        d[i] = (c[i+1] - c[i]) / (3*delta_x[i])
        b[i] = (delta_y[i]/delta_x[i]) - (delta_x[i]/3)*(2*c[i] + c[i+1])    
    
    return y, b.squeeze(), c.squeeze(), d.squeeze()


if __name__ == "__main__":
    points = np.array([[1.5, 80],
                    [1.9, 136],
                    [2.3, 70],
                    [2.7, 165],
                    [3.1, 102]])
    x_points = points[:,0]
    y_points = points[:,1]
    coeffs = cubic_spline(x_points, y_points)

    x_interp = []
    y_interp = []
    for index, xi in enumerate(x_points[:-1]):
        for x in np.arange(x_points[index], x_points[index + 1], 0.01):
            y = coeffs[0][index] + coeffs[1][index]*(x-xi) + coeffs[2][index]*((x-xi)**2) + coeffs[3][index]*((x-xi)**3) 
            x_interp.append(x)
            y_interp.append(y)
    x_interp.append(x_points[-1])
    y_interp.append(y_points[-1])
    
    print("Коефіцієнти сплайна:\na = {}\nb = {}\nc = {}\nd = {}".format(
        coeffs[0], coeffs[1], coeffs[2], coeffs[3]))

    plt.xlim([min(x_points) - 0.3, max(x_points) + 0.3])
    plt.ylim([min(y_points) - 10, max(y_interp) + 10])
    plt.plot(x_points, y_points, '-o', color='orange')
    plt.plot(x_interp, y_interp, color='blue')
    plt.title('Cubic Spline')

    plt.show()
