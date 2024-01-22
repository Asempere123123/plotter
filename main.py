from lib import plot_4d_to_file, plot_3d_to_file

def function(x):
    return (-1)**x

plot_4d_to_file(function, points_length=2000, points_width=1000, length=10, width=1)
plot_3d_to_file(function, points=2000, length=10)