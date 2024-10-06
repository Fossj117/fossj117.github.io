import cv2
import math
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def process_frame(frame, frame_count, top_percentage, save_frames, saved_frame_count):
    # Determine the height of the top portion
    height = frame.shape[0]
    top_height = int(height * top_percentage)

    # Slice the frame to only include the top portion
    top_frame = frame[:top_height, :, :]

    # Optionally save the truncated frame for inspection
    if save_frames and saved_frame_count < 5:  # Save only the first 5 frames
        cv2.imwrite(f'top_frame_{frame_count}.png', top_frame)
        saved_frame_count += 1

    # Compute the average color of the top portion of the frame
    avg_color = np.mean(top_frame, axis=(0, 1))
    print(f"Average color of frame {frame_count}: {avg_color}")
    return avg_color

def extract_average_colors(video_path, output_file, per_frame=100, top_percentage=0.33, save_frames=False):
    # Open the video file
    print("Opening video file...")
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    else:
        print("Video opened successfully.")

    # Initialize variables
    frame_count = 0
    average_colors = []
    saved_frame_count = 0

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        futures = []

        # Get the total number of frames
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print("Total frames in video:", total_frames)

        # Loop through the video frames
        print("Starting frame processing...")
        while frame_count < total_frames:
            # Set the position of the next frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
            ret, frame = cap.read()
            if not ret:
                print(f"Cannot fetch frame {frame_count}.")
                break  # Exit the loop if no frame is returned

            # Process the frame
            print(f"Submitting frame {frame_count} for processing...")
            futures.append(executor.submit(process_frame, frame, frame_count, top_percentage, save_frames, saved_frame_count))

            # Increment the frame counter by per_frame
            frame_count += per_frame

        # Collect results as they complete
        for future in futures:
            average_colors.append(future.result())

    # Release the video capture object
    cap.release()
    print("Video processing completed.")

    return average_colors

def create_svg(average_colors, max_width, box_size=50, output_file='average_colors.svg'):
    num_colors = len(average_colors)
    boxes_per_row = min(max_width, num_colors)
    num_rows = math.ceil(num_colors / boxes_per_row)

    # Calculate the dimensions of the SVG image
    svg_width = boxes_per_row * box_size
    svg_height = num_rows * box_size

    # Start building the SVG content
    svg_content = []
    svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">'
    svg_content.append(svg_header)

    # Define a background (optional)
    # svg_content.append(f'<rect width="100%" height="100%" fill="white" />')

    # Loop through each color and create a rectangle
    for idx, color in enumerate(average_colors):
        row = idx // boxes_per_row
        col = idx % boxes_per_row
        x = col * box_size
        y = row * box_size

        # Convert the average color to RGB integer values
        r, g, b = map(int, color)
        fill_color = f'rgb({r},{g},{b})'

        # Create the rectangle element
        rect = f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{fill_color}" />'
        svg_content.append(rect)

        # Add the index number as text
        text_x = x + box_size / 2
        text_y = y + box_size / 2 + 5  # +5 to adjust vertical alignment
        text = f'''
        <text x="{text_x}" y="{text_y}" font-size="12" text-anchor="middle" fill="white">
            {idx}
        </text>
        '''
        svg_content.append(text)

    # Close the SVG tag
    svg_content.append('</svg>')

    # Write the SVG content to a file
    with open(output_file, 'w') as f:
        f.write('\n'.join(svg_content))

    print(f"SVG file '{output_file}' has been created.")

def extract_rgb_values_every_100_frames(video_path, output_file='rgb_values_every_100_frames.csv'):
    # Open the video file
    print("Opening video file...")
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    else:
        print("Video opened successfully.")

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total frames in video:", total_frames)

    # Open the output file
    with open(output_file, 'w') as f:
        # Write the header
        f.write("frame_number,r,g,b\n")

        # Loop through each frame, but only process every 100th frame
        frame_count = 0
        while frame_count < total_frames:
            # Set the position of the next frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
            ret, frame = cap.read()
            if not ret:
                print(f"Cannot fetch frame {frame_count}.")
                break  # Exit the loop if no frame is returned

            # Compute the average color of the frame
            avg_color = np.mean(frame, axis=(0, 1))
            r, g, b = map(int, avg_color)

            # Write the RGB values to the file
            f.write(f"{frame_count},{r},{g},{b}\n")

            print(f"Processed frame {frame_count}: RGB({r}, {g}, {b})")

            # Increment the frame counter by 100
            frame_count += 100

    # Release the video capture object
    cap.release()
    print(f"RGB values for every 100th frame have been written to '{output_file}'.")

# Example usage:
if __name__ == '__main__':

    average_colors_top_third = extract_average_colors('charles_ride.MP4', 'average_colors_top_third.svg', per_frame=100, top_percentage=0.33, save_frames=False)

    # Save the average colors to a CSV file
    with open('average_colors_top_third.csv', 'w') as f:
        for color in average_colors_top:
            f.write(f"{color[0]},{color[1]},{color[2]}\n")

    create_svg(average_colors_top_third, 20, output_file='average_colors_top_third.svg')