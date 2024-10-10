import svgwrite
import random
import math
import csv

def create_square_group(dwg, num_lines_per_square, cmy, x, y, square_size):
    # Unpack the CMY tuple
    cyan, magenta, yellow = cmy

    print(num_lines_per_square, cyan, magenta, yellow, x, y, square_size)

    # Create a group for the square
    square_group = dwg.g()

    # Define color and proportion pairs
    color_proportions = [('cyan', cyan), ('magenta', magenta), ('yellow', yellow)]

    # Add random vertical lines for each color
    for color, proportion in color_proportions:
        for _ in range(int(num_lines_per_square * proportion)):
            line_x = x + random.randint(0, square_size)
            line = dwg.line(start=(line_x, y), end=(line_x, y + square_size), stroke=color)
            square_group.add(line)

    return square_group

def rgb_to_cmy(rgb):
    # Convert RGB to CMY
    r, g, b = rgb
    c = 1 - (r / 255)
    m = 1 - (g / 255)
    y = 1 - (b / 255)
    return (c, m, y)

def cmy_to_rgb(cmy):
    # Convert CMY values (0-1 range) to RGB (0-255 range)
    c, m, y = cmy
    r = int((1 - c) * 255)
    g = int((1 - m) * 255)
    b = int((1 - y) * 255)
    return r, g, b

def create_svg_with_squares_from_csv(csv_file, filename, num_lines_per_square=10, square_size=80, spacing=20, max_width=20, row_nums=None, col_nums=None):
    # Read RGB colors from CSV
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rgb_colors = [tuple(map(int, row)) for row in reader]

    # Convert RGB to CMY and normalize
    cmy_colors = [rgb_to_cmy(rgb) for rgb in rgb_colors]

    # Calculate the number of squares per row and the number of rows
    num_colors = len(cmy_colors)
    boxes_per_row = min(max_width, num_colors)
    num_rows = math.ceil(num_colors / boxes_per_row)

    # Calculate the dimensions of the SVG image
    svg_width = boxes_per_row * (square_size + spacing)
    svg_height = num_rows * (square_size + spacing)

    # Create the SVG drawing
    dwg = svgwrite.Drawing(filename, size=(svg_width, svg_height))

    for row in range(num_rows):
        for col in range(boxes_per_row):
            if row_nums and row not in row_nums:
                continue
            if col_nums and col not in col_nums:
                continue

            color_index = row * boxes_per_row + col
            if color_index >= num_colors:
                break

            # Calculate the top-left corner of each square
            x = col * (square_size + spacing)
            y = row * (square_size + spacing)

            # Get the CMY color for the current square
            cmy = cmy_colors[color_index]

            # Create the square group using the new function
            square_group = create_square_group(dwg, num_lines_per_square, cmy, x, y, square_size)

            # Add the group to the drawing
            dwg.add(square_group)
    
    # Add tiny dots at the four corners
    circle_radius = 5
    corner_positions = [(0,0), (svg_width, 0), (0, svg_height), (svg_width, svg_height)]
    for pos in corner_positions:
        circle = dwg.circle(center=pos, r=circle_radius, stroke='purple')
        dwg.add(circle)


    # Save the SVG file
    dwg.save()

def create_svg_with_wedges_from_csv(csv_file, filename, num_wedges, num_lines_per_wedge=10, inner_radius=50, outer_radius=100):
    import math

    # Read RGB colors from CSV
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rgb_colors = [tuple(map(int, row)) for row in reader]

    # Convert RGB to CMY and normalize
    cmy_colors = [rgb_to_cmy(rgb) for rgb in rgb_colors]

    # Calculate the angle for each wedge
    angle_per_wedge = 2 * math.pi / num_wedges

    # Create the SVG drawing
    svg_size = 2 * outer_radius
    dwg = svgwrite.Drawing(filename, size=(svg_size, svg_size))

    # Center of the circle
    center_x, center_y = outer_radius, outer_radius

    for wedge_index in range(num_wedges):
        if wedge_index >= len(cmy_colors):
            break

        # Get the CMY color for the current wedge
        cmy = cmy_colors[wedge_index]

        # Unpack the CMY tuple
        cyan, magenta, yellow = cmy

        # Define color and proportion pairs
        color_proportions = [('cyan', cyan), ('magenta', magenta), ('yellow', yellow)]

        # Calculate the start and end angles for the wedge
        start_angle = wedge_index * angle_per_wedge
        end_angle = start_angle + angle_per_wedge

        # Add random lines for each color within the wedge
        for color, proportion in color_proportions:
            for _ in range(int(num_lines_per_wedge * proportion)):
                # Randomly choose an angle within the wedge
                angle = random.uniform(start_angle, end_angle)

                # Convert polar coordinates to Cartesian coordinates for the start and end of the line
                start_x = center_x + inner_radius * math.cos(angle)
                start_y = center_y + inner_radius * math.sin(angle)
                end_x = center_x + outer_radius * math.cos(angle)
                end_y = center_y + outer_radius * math.sin(angle)

                # Create a line from the inner radius to the outer radius
                line = dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke=color)
                dwg.add(line)

    # Save the SVG file
    dwg.save()

def create_svg_with_filled_squares_from_csv(csv_file, filename, square_size=80, spacing=20, max_width=20, row_nums=None, col_nums=None):
    # Read RGB colors from CSV
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rgb_colors = [tuple(map(int, row)) for row in reader]

    # Convert RGB to CMY and normalize
    cmy_colors = [rgb_to_cmy(rgb) for rgb in rgb_colors]

    # Calculate the number of squares per row and the number of rows
    num_colors = len(cmy_colors)
    boxes_per_row = min(max_width, num_colors)
    num_rows = math.ceil(num_colors / boxes_per_row)

    # Calculate the dimensions of the SVG image
    svg_width = boxes_per_row * (square_size + spacing)
    svg_height = num_rows * (square_size + spacing)

    # Create the SVG drawing
    dwg = svgwrite.Drawing(filename, size=(svg_width, svg_height))

    for row in range(num_rows):
        for col in range(boxes_per_row):
            if row_nums and row not in row_nums:
                continue
            if col_nums and col not in col_nums:
                continue

            color_index = row * boxes_per_row + col
            if color_index >= num_colors:
                break

            # Calculate the top-left corner of each square
            x = col * (square_size + spacing)
            y = row * (square_size + spacing)

            # Get the CMY color for the current square
            cmy = cmy_colors[color_index]

            # Convert CMY to RGB for SVG fill
            r, g, b = cmy_to_rgb(cmy)
            fill_color = f'rgb({r},{g},{b})'

            # Create the filled square
            rect = dwg.rect(insert=(x, y), size=(square_size, square_size), fill=fill_color)
            dwg.add(rect)
    
    # Add tiny dots at the four corners
    circle_radius = 5
    corner_positions = [(0,0), (svg_width, 0), (0, svg_height), (svg_width, svg_height)]
    for pos in corner_positions:
        circle = dwg.circle(center=pos, r=circle_radius, stroke='purple')
        dwg.add(circle)

    # Save the SVG file
    dwg.save()

def create_svg_with_partial_squares_from_csv(csv_file, filename, percentage, num_lines_per_square=10, square_size=80, spacing=20):
    # Read RGB colors from CSV
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rgb_colors = [tuple(map(int, row)) for row in reader]

    # Convert RGB to CMY and normalize
    cmy_colors = [rgb_to_cmy(rgb) for rgb in rgb_colors]

    # Calculate the number of squares to include
    num_colors = len(cmy_colors)
    num_squares_to_include = int(num_colors * percentage)

    # Calculate the number of squares per row and column for a square aspect ratio
    squares_per_side = math.ceil(math.sqrt(num_squares_to_include))

    # Calculate the dimensions of the SVG image
    svg_size = squares_per_side * (square_size + spacing)

    # Create the SVG drawing
    dwg = svgwrite.Drawing(filename, size=(svg_size, svg_size))

    for row in range(squares_per_side):
        for col in range(squares_per_side):
            color_index = row * squares_per_side + col
            if color_index >= num_squares_to_include:
                break

            # Calculate the top-left corner of each square
            x = col * (square_size + spacing)
            y = row * (square_size + spacing)

            # Get the CMY color for the current square
            cmy = cmy_colors[color_index]

            # Create the square group using the new function
            square_group = create_square_group(dwg, num_lines_per_square, cmy, x, y, square_size)

            # Add the group to the drawing
            dwg.add(square_group)

    # Add tiny dots at the four corners
    circle_radius = 5
    corner_positions = [(5, 5), (svg_size-5, 5), (5, svg_size-5), (svg_size-5, svg_size-5)]
    for pos in corner_positions:
        circle = dwg.circle(center=pos, r=circle_radius, stroke='purple')
        dwg.add(circle)

    # Save the SVG file
    dwg.save()

# Example usage:
#create_svg_with_partial_squares_from_csv('random_colors_top_third.csv', 'partial_squares_from_csv_square.svg', percentage=0.05, num_lines_per_square=80, spacing=10)

# Example usage:
# Example usage
create_svg_with_wedges_from_csv(
    csv_file='random_colors_top_third_v2.csv',  # Path to your CSV file
    filename='output_wedges.svg',        # Desired output SVG filename
    num_wedges=12,                       # Number of wedges to create
    num_lines_per_wedge=20,              # Number of lines per wedge (optional)
    inner_radius=50,                     # Inner radius of the wedges (optional)
    outer_radius=100                     # Outer radius of the wedges (optional)
)

# create_svg_with_squares_from_csv('random_colors_top_third_v2.csv', 'squares_from_csv_12_16_60lines_sq.svg', num_lines_per_square=40, spacing=10, max_width=20, row_nums=[12,13,14,15,16], col_nums=[8,9,10,11,12])
# create_svg_with_filled_squares_from_csv('random_colors_top_third_v2.csv', 'filled_squares_from_csv_12_16_60lines_sq.svg', spacing=10, max_width=20, row_nums=[12,13,14,15,16], col_nums=[8,9,10,11,12])
#create_svg_with_partial_squares_from_csv('random_colors_top_third.csv', 'squares_from_csv_10percent.svg', 0.1, num_lines_per_square=80, spacing=10)
#create_svg_with_partial_squares_from_csv('random_colors_top_third.csv', 'partial_squares_from_csv_square.svg', percentage=0.1, num_lines_per_square=80, spacing=10)