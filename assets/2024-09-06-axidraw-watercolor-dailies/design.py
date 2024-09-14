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
    def __init__(self, x, y, size, fill, dwg):
        '''
        X and Y are the coordinates of the square in the grid

        fill can be "Light_Fill", "Heavy_Fill", "No_Fill" or "None"
        '''
        self.x = x
        self.y = y
        self.size = size

        self.fill = fill
        #self.fill_weights = fill_weights
        #self.fill_categories = ['Light_Fill', 'Heavy_Fill', 'No_Fill', 'None']

        # Assert that fillweights must be same length as fillCategories
        #assert len(self.fill_weights) == len(self.fill_categories)

        self.dwg = dwg

    def chooseFill(self):
        if self.fill: 
            return self.fill
        else: 
            return 'None'

    def drawFilledAt(self,x_pix,y_pix, num_lines): 
        self.dwg.add(
                self.dwg.rect(
                    (x_pix, y_pix), 
                    (self.size, self.size), 
                    fill='none', stroke='black')
                )
        # create lines at regular intervals to fill the shape
       # num_lines = random.choice([2,3,4,5,6])
        orientation = random.choice(['horizontal', 'vertical'])

        if orientation == 'horizontal':
            for i in range(num_lines):
                self.dwg.add(
                    self.dwg.line(
                        (x_pix + i * self.size/num_lines, y_pix),
                        (x_pix + i * self.size/num_lines, y_pix + self.size),
                        stroke='black'
                    )
                )
        else:
            for i in range(num_lines):
                self.dwg.add(
                    self.dwg.line(
                        (x_pix, y_pix + i * self.size/num_lines),
                        (x_pix + self.size, y_pix + i * self.size/num_lines),
                        stroke='black'
                    )
                )

    def drawNoFillAt(self,x_pix,y_pix):
        
        # Sometimes draw a square with no fill; other times draw sides separately and sometimes exclude them

        if random.random() > 0.5:

            self.dwg.add(
                self.dwg.rect(
                    (x_pix, y_pix), 
                    (self.size, self.size), 
                    fill='none', stroke='black')
            )
        
        else:

            # draw each side and render each with some probability 

            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix, y_pix),
                        (x_pix + self.size, y_pix),
                        stroke='black'
                    )
                )
            
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix + self.size, y_pix),
                        (x_pix + self.size, y_pix + self.size),
                        stroke='black'
                    )
                )
            
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix + self.size, y_pix + self.size),
                        (x_pix, y_pix + self.size),
                        stroke='black'
                    )
                )
            
            if random.random() > 0.25:
                self.dwg.add(
                    self.dwg.line(
                        (x_pix, y_pix + self.size),
                        (x_pix, y_pix),
                        stroke='black'
                    )
                )

    def draw(self):
        # Draw at the location defined by the x and y coordinates
        # So it's at location x*size, y*size
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

    X_size_pixels = 300
    Y_size_pixels = 500
    square_size_pixels = 10

    num_x_pixels = X_size_pixels // square_size_pixels
    num_y_pixels = Y_size_pixels // square_size_pixels

    fracture = Fracture(num_x_pixels//2, num_y_pixels)
    fracture_locations = fracture.create()

    focal = Focal(num_x_pixels, num_y_pixels)
    focal_location = focal.create()

    focal2 = Focal(num_x_pixels, num_y_pixels)
    focal2_location = focal2.create()


    dwg = svgwrite.Drawing('output.svg', size=(X_size_pixels, Y_size_pixels))

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
            if random.random() < normalized_distance_from_fracture*.45:
                
                if random.random() < normalized_distance_from_fracture*.5:
                    fill = 'Light_Fill'
                else: 
                    fill = 'Heavy_Fill'

            elif random.random() > normalized_distance_from_fracture*1.1:
                fill = 'No_Fill'

            if distance_from_fracture < 3 and random.random() > 0.1: 
                fill = 'None'

            if random.random() > 3*normalized_distance_from_focal: 
                fill = 'None'

            if random.random() > 3*normalized_distance_from_focal2: 
                fill = 'None'

            # slowly increasing chance of none as you go down the page
            if random.random() > 0.95 * y / num_y_pixels: 
                fill = 'None' 

#            xp, yp = push_from_focal(x, y, focal_x, focal_y, 0.25)
            xp, yp = x, y

            squares.append(Square(xp, yp, square_size_pixels, fill, dwg))

    # Draw all the squares
    for square in squares:
        square.draw()
    
    dwg.save()


if __name__ == '__main__':
    main()


