import random
import svgwrite
import math

def distance_xy(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def push_from_focal(x, y, focal_x, focal_y, push_factor):
    distance = distance_xy(x, y, focal_x, focal_y)
    angle = math.atan2(y - focal_y, x - focal_x)
    return (x + push_factor * distance * math.cos(angle), y + push_factor * distance * math.sin(angle))

class Square: 
    def __init__(self, x, y, size, fill, dwg, rotate="rotate(0 0 0)"):
        '''
        X and Y are the coordinates of the square in the grid

        fill can be "Light_Fill", "Heavy_Fill", "No_Fill" or "None"
        '''
        self.x = x
        self.y = y
        self.size = size
        self.stroke = self.choose_stroke_color(x, y)
        self.fill = fill
        self.rotate = rotate # transform="rotate(45 100 50)"
        self.dwg = dwg

    def chooseFill(self):
        if self.fill: 
            return self.fill
        else: 
            return 'None'

    def choose_stroke_color(self, x, y):
        # Example of a stochastic function based on location with added randomness
        colors = ['black', 'grey', 'red', 'yellow', 'pink', 'blue', 'green','orange', 'brown']
        base_index = (math.sin(x * 0.1) + math.cos(y * 0.1)) * len(colors) / 2
        random_factor = random.uniform(-1, 1)  # Random factor between -1 and 1
        index = int((base_index + random_factor) % len(colors))
        return colors[index]

    def draw_partial_square(self, x_pix, y_pix, sides):
        """
        Draws a square with only the specified sides.
        sides: a list containing any combination of 'top', 'bottom', 'left', 'right'
        """
        if 'top' in sides:
            self.dwg.add(
                self.dwg.line(
                    (x_pix, y_pix),
                    (x_pix + self.size, y_pix),
                    stroke=self.stroke, transform=self.rotate
                )
            )
        if 'bottom' in sides:
            self.dwg.add(
                self.dwg.line(
                    (x_pix, y_pix + self.size),
                    (x_pix + self.size, y_pix + self.size),
                    stroke=self.stroke, transform=self.rotate
                )
            )
        if 'left' in sides:
            self.dwg.add(
                self.dwg.line(
                    (x_pix, y_pix),
                    (x_pix, y_pix + self.size),
                    stroke=self.stroke, transform=self.rotate
                )
            )
        if 'right' in sides:
            self.dwg.add(
                self.dwg.line(
                    (x_pix + self.size, y_pix),
                    (x_pix + self.size, y_pix + self.size),
                    stroke=self.stroke, transform=self.rotate
                )
            )

    def drawFilledAt(self, x_pix, y_pix, num_lines): 
        
        if random.random() > 0.2:  # 80% chance to add the square boundary
            sides = random.sample(['top', 'bottom', 'left', 'right'], k=random.randint(1, 4))
            self.draw_partial_square(x_pix, y_pix, sides)

        orientation = random.choice(['horizontal', 'vertical', 'concentric'])

        if orientation == 'horizontal':
            for i in range(num_lines):
                if random.random() > 0.1:  # 80% chance to draw the line
                    self.dwg.add(
                        self.dwg.line(
                            (x_pix + i * self.size / num_lines, y_pix),
                            (x_pix + i * self.size / num_lines, y_pix + self.size),
                            stroke=self.stroke, transform=self.rotate
                        )
                    )
        elif orientation == 'vertical':
            for i in range(num_lines):
                if random.random() > 0.1:  # 80% chance to draw the line
                    self.dwg.add(
                        self.dwg.line(
                            (x_pix, y_pix + i * self.size / num_lines),
                            (x_pix + self.size, y_pix + i * self.size / num_lines),
                            stroke=self.stroke, transform=self.rotate
                        )
                    )
        elif orientation == 'concentric':
            for i in range(num_lines):
                inset = i * self.size / (2 * num_lines)
                if random.random() > 0.1:  # 80% chance to draw the square
                    self.dwg.add(
                        self.dwg.rect(
                            (x_pix + inset, y_pix + inset), 
                            (self.size - 2 * inset, self.size - 2 * inset), 
                            fill='none', stroke=self.stroke, transform=self.rotate)
                    )

    def drawNoFillAt(self, x_pix, y_pix):
        if random.random() > 0.5:
            sides = random.sample(['top', 'bottom', 'left', 'right'], k=random.randint(1, 4))
            self.draw_partial_square(x_pix, y_pix, sides)
        else:
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix, y_pix),
                        (x_pix + self.size, y_pix),
                        stroke=self.stroke, transform=self.rotate
                    )
                )
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix + self.size, y_pix),
                        (x_pix + self.size, y_pix + self.size),
                        stroke=self.stroke, transform=self.rotate
                    )
                )
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix + self.size, y_pix + self.size),
                        (x_pix, y_pix + self.size),
                        stroke=self.stroke, transform=self.rotate
                    )
                )
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix, y_pix + self.size),
                        (x_pix, y_pix),
                        stroke=self.stroke, transform=self.rotate
                    )
                )

    def draw(self):
        x_pix = self.x * self.size 
        y_pix = self.y * self.size

        self.fill = self.chooseFill()

        if self.fill == 'Light_Fill':
            self.drawFilledAt(x_pix, y_pix, 3)
        elif self.fill == 'Heavy_Fill':
            self.drawFilledAt(x_pix, y_pix, 6)
        elif self.fill == 'No_Fill':
            self.drawNoFillAt(x_pix, y_pix)

class Fracture: 
    def __init__(self, start_x, num_rows): 
        self.start_x = start_x
        self.num_rows = num_rows
    
    def create(self): 
        curr_row = 0
        curr_x = self.start_x
        locations = []

        while curr_row < self.num_rows:
            locations.append(curr_x)
            direction = random.choice([-1, 1])
            curr_x = curr_x + direction
            curr_row += 1
        
        return locations

class Focal: 
    def __init__(self, max_x, max_y): 
        self.max_x = max_x
        self.max_y = max_y

    def max_distance_from_focal(self, x, y):

        distances = [
            distance_xy(x, y, 0, 0),
            distance_xy(x, y, 0, self.max_y),
            distance_xy(x, y, self.max_x, 0),
            distance_xy(x, y, self.max_x, self.max_y)
        ]

        return max(distances)
    
    def create(self): 
        x = random.randint(0, self.max_x)
        y = random.randint(0, self.max_y)
        return (x, y)

def main(): 
    # smaller size
    # X_size_pixels = 300
    # Y_size_pixels = 500
    # square_size_pixels = 10

    # larger size - 5.5 by 8.5 inch; 0.5 inch margin = -1
    X_size_pixels = 550
    Y_size_pixels = 550
    square_size_pixels = 12

    num_x_pixels = X_size_pixels // square_size_pixels
    num_y_pixels = Y_size_pixels // square_size_pixels

    fracture = Fracture(num_x_pixels//2, num_y_pixels)
    fracture_locations = fracture.create()

    focal = Focal(num_x_pixels, num_y_pixels)
    focal_location = focal.create()

    focal2 = Focal(num_x_pixels, num_y_pixels)
    focal2_location = focal2.create()

    dwg = svgwrite.Drawing('output.svg', size=(X_size_pixels, Y_size_pixels))

    # Define size factors
    min_size_factor = 0.5
    max_size_factor = 2

    # Create a list of squares
    squares = []
    for y in range(num_y_pixels):
        for x in range(num_x_pixels):

            # Fracture distances
            curr_fracture_location = fracture_locations[y]
            distance_from_fracture = abs(curr_fracture_location - x)
            max_distance_from_fracture = max(curr_fracture_location, abs(num_x_pixels - curr_fracture_location))
            normalized_distance_from_fracture = distance_from_fracture / max_distance_from_fracture # 0 to 1

            # Focal distances
            focal_x, focal_y = focal_location
            distance_from_focal = distance_xy(x, y, focal_x, focal_y)
            max_distance_from_focal = focal.max_distance_from_focal(x, y)
            normalized_distance_from_focal = distance_from_focal / max_distance_from_focal

            # Focal distances
            focal2_x, focal2_y = focal2_location
            distance_from_focal2 = distance_xy(x, y, focal2_x, focal2_y)
            max_distance_from_focal2 = focal2.max_distance_from_focal(x, y)
            normalized_distance_from_focal2 = distance_from_focal2 / max_distance_from_focal2

            # Choose render style based on distance from fracture
            # Can be "Fill", "No Fill" or "None" with probability based on distance from fracture

            fill = 'None'
            if random.random() < normalized_distance_from_fracture * 0.3:
                if random.random() < normalized_distance_from_fracture * 0.5:
                    fill = 'Light_Fill'
                else: 
                    fill = 'Heavy_Fill'
            elif random.random() > normalized_distance_from_fracture * 1.1:
                fill = 'No_Fill'

            if distance_from_fracture < 5 and random.random() > 0.1: 
                fill = 'None'

            if random.random() > 2 * normalized_distance_from_focal: 
                fill = 'None'

            if random.random() > 2 * normalized_distance_from_focal2: 
                fill = 'None'

            # slowly increasing chance of none as you go down the page
            if random.random() > 0.98 * y / num_y_pixels: 
                fill = 'None' 

            # Rotate the squares around the focal point; the closer they are are the more they are rotated

            # Calculate rotation angle based on distance from focal point
            max_rotation = 180 * random.uniform(0.9, 1.1)  # Maximum rotation angle in degrees
            rotation_factor = 1 - normalized_distance_from_focal  # Closer squares rotate more
            base_rotation_angle = max_rotation * rotation_factor
            
            # Add some randomness to the rotation angle
            random_factor = random.uniform(0.85, 1.15)  # Random factor between 0.9 and 1.1
            rotation_angle = base_rotation_angle * random_factor

            # Ensure rotation angle stays within reasonable bounds
            rotation_angle = max(min(rotation_angle, max_rotation), -max_rotation)
            # rotation_angle = 0

            # Calculate the center of the square for rotation
            center_x = x * square_size_pixels + square_size_pixels / 2
            center_y = y * square_size_pixels + square_size_pixels / 2

            # Create the rotation transform string
            rotate = f"rotate({rotation_angle} {center_x} {center_y})"

            # Remove size variation
            varied_square_size = square_size_pixels

            # Remove the line that references undefined variables
            # size_factor = min_size_factor + (max_size_factor - min_size_factor) * combined_size_factor

            squares.append(Square(x, y, varied_square_size, fill, dwg, rotate=rotate))

    # Draw all the squares within bounds
    for square in squares:
        x_pix = square.x * square.size
        y_pix = square.y * square.size

        if 0 <= x_pix < X_size_pixels and 0 <= y_pix < Y_size_pixels:
            square.draw()

    # Create dots at the four corners of the drawing
    pts = [
        (0, 0), 
        (X_size_pixels, 0), 
        (0, Y_size_pixels), 
        (X_size_pixels, Y_size_pixels)
    ]

    for pt in pts: 
        dwg.add(
            dwg.circle(
                center=pt,
                r=5,  # radius of the circle
                stroke='purple'
            )
        )

    dwg.save()

if __name__ == '__main__':
    main()


