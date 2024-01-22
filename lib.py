import matplotlib.pyplot as plt
import numpy as np

def get_points(f, points=100, length=10):
    x = []
    y = []
    z = []

    ratio = length/points
    for i in range(points):
        value_to_evaluate = i*ratio
        value = f(value_to_evaluate)

        x.append(value_to_evaluate)
        y.append(value.real)
        z.append(value.imag)

    return (np.array([x]), np.array([y]), np.array([z]))

def get_comlpex_points(f, points_length=100, points_width=10, length=10, width=1):
    x = []
    y = []
    z = []

    ratio_length = length/points_length
    ratio_width = width/points_width
    for i in range(points_length):
        value_length = i*ratio_length
        for j in range(points_width):
            value_width = j*ratio_width

            value = complex(value_length, value_width)
            result = f(value)

            # No se como plotear en 4d asi que toca sobreponer todas
            x.append(value_length)
            y.append(result.real)
            z.append(result.imag)

    return (np.array([x]), np.array([y]), np.array([z]))

def plot_4d_to_file(f, points_length=100, points_width=10, length=10, width=1, filename="4d_plot.png"):
    fig = plt.figure()

    ax1 = fig.add_subplot(111, projection='3d')
    x, y, z = get_comlpex_points(f, points_length=points_length, points_width=points_width, length=length, width=width)

    ax1.plot_wireframe(x, y, z)
    ax1.set_xlim([0, length])
    ax1.set_ylim([min(y.flatten()), max(y.flatten())])
    ax1.set_zlim([min(z.flatten()), max(z.flatten())])

    plt.savefig(filename)

def plot_3d_to_file(f, points=100, length=10, filename="3d_plot.png"):
    fig = plt.figure()

    ax1 = fig.add_subplot(111, projection='3d')
    x, y, z = get_points(f, points=points, length=length)

    ax1.plot_wireframe(x, y, z)
    ax1.set_xlim([0, length])
    ax1.set_ylim([min(y.flatten()), max(y.flatten())])
    ax1.set_zlim([min(z.flatten()), max(z.flatten())])

    plt.savefig(filename)
    