class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Translate the point by dx and dy."""
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

 ### [2] Driver Program
import matplotlib.pyplot as plt


def read_points_from_file(file_path):
    """Read points from a text file and return a list of Point objects."""
    points = []
    with open(file_path, 'r') as file:
        next(file)  # Skip header
        for line in file:
            x, y = map(float, line.strip().split(','))
            points.append(Point(x, y))
    return points


def plot_points(points, color='blue', label='Original'):
    """Plot points on a scatter plot."""
    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]
    plt.scatter(x_coords, y_coords, color=color, label=label)


def main(file_path):
    # Read points from file
    points = read_points_from_file(file_path)

    # Plot original points
    plot_points(points, color='blue', label='Original Points')

    # Move points
    for point in points:
        point.move(1, 1)  # Translate each point by (1, 1)

    # Plot moved points
    plot_points(points, color='red', label='Moved Points')

    # Set plot details
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Scatter Plot of Points')
    plt.legend()
    plt.grid(True)
    plt.show()


# Specify your file path here
main('C:/Users/USER/Desktop/SEAN/x_y_coordinates.txt')





