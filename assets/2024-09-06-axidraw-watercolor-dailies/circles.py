import svgwrite
import random
import math

# Function to convert polar to Cartesian coordinates
def polar_to_cartesian(center_x, center_y, radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    x = center_x + radius * math.cos(angle_radians)
    y = center_y - radius * math.sin(angle_radians)  # SVG y-coordinates increase downwards
    return x, y

# Function to generate a path for a circular arc
def describe_arc(x, y, radius, start_angle, end_angle):
    start = polar_to_cartesian(x, y, radius, end_angle)
    end = polar_to_cartesian(x, y, radius, start_angle)
    large_arc_flag = "0" if end_angle - start_angle <= 180 else "1"
    d = f"M {start[0]} {start[1]} A {radius} {radius} 0 {large_arc_flag} 0 {end[0]} {end[1]}"
    return d

# Create an SVG drawing object
dwg = svgwrite.Drawing("concentric_circles_with_calibration.svg", profile="tiny", size=(500, 500))

center_x = 250
center_y = 250
max_radius = 200
num_circles = 10

# Draw concentric circles with random arcs removed
for i in range(num_circles):
    radius = max_radius - (i * (max_radius // num_circles))
    # Randomly select an arc to remove from the circle
    start_angle = random.randint(0, 360)
    arc_length = random.randint(30, 180)  # Length of the arc to be removed
    end_angle = (start_angle + arc_length) % 360

    # Create path for the arc that remains
    arc_path = describe_arc(center_x, center_y, radius, end_angle, start_angle)
    
    # Add the arc path to the SVG
    dwg.add(dwg.path(d=arc_path, stroke="black", fill="none", stroke_width=2))

# Add four points for calibration in the corners
corner_points = [(0, 0), (0, 500), (500, 0), (500, 500)]
for point in corner_points:
    dwg.add(dwg.circle(center=point, r=5, stroke="red", fill="red"))

# Save the SVG file
dwg.save()

print("SVG file with concentric circles and calibration points generated.")
