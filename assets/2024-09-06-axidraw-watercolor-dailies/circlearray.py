import svgwrite
import random

# Define SVG parameters
width = 300          # Width of the SVG canvas
height = 300         # Height of the SVG canvas
circle_radius = 20   # Radius of the circles
padding = 10         # Space between the circles
rows, cols = 5, 5    # Number of rows and columns

# Create a list of colors for the strokes
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'black', 'pink']

# Initialize SVG drawing
dwg = svgwrite.Drawing('circles.svg', profile='tiny', size=(width, height))

# Calculate starting position
start_x = circle_radius + padding
start_y = circle_radius + padding

# Generate circles
for row in range(rows):
    for col in range(cols):
        x = start_x + col * (circle_radius * 2 + padding)
        y = start_y + row * (circle_radius * 2 + padding)
        
        # Choose a random color for the stroke
        stroke_color = random.choice(colors)
        
        # Create a circle
        dwg.add(dwg.circle(center=(x, y), r=circle_radius, stroke=stroke_color, fill='none', stroke_width=2))

# Save SVG to file
dwg.save()

print("SVG file 'circles.svg' has been generated!")
