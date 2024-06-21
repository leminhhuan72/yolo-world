import cv2
import os

def generate_video_from_folder(frame_folder, output_video_path, fps=24):
    """
    Generates a video from frames stored in a specified folder.
    
    Parameters:
        frame_folder (str): Path to the folder containing frame images.
        output_video_path (str): Path where the output video will be saved.
        fps (int): Frames per second for the output video.
    """
    # Get list of all image files in the folder
    files = [f for f in os.listdir(frame_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    files.sort()  # Ensure the frames are in the correct order

    if not files:
        print("No frames found in the specified folder.")
        return

    # Read the first frame to get the size
    first_frame_path = os.path.join(frame_folder, files[0])
    first_frame = cv2.imread(first_frame_path)
    if first_frame is None:
        print(f"Error reading the first frame: {first_frame_path}")
        return

    height, width, layers = first_frame.shape
    size = (width, height)

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for mp4 output
    out = cv2.VideoWriter(output_video_path, fourcc, fps, size)

    for file_name in files:
        frame_path = os.path.join(frame_folder, file_name)
        frame = cv2.imread(frame_path)
        
        if frame is None:
            print(f"Error reading frame: {frame_path}")
            continue
        
        out.write(frame)

    out.release()
    print(f"Video saved to {output_video_path}")



def generate_video_from_frames(frames, output_video_path, fps=24):
    """
    Generates a video from frames stored in a specified folder.
    
    Parameters:
        frames (list): python list containing frame images.
        output_video_path (str): Path where the output video will be saved.
        fps (int): Frames per second for the output video.
    """
    if not frames:
        print("No frames found in the list.")
        return

 
    first_frame = frames[0]
    if first_frame is None:
        print(f"Error reading the first frame")
        return

    height, width, layers = first_frame.shape
    size = (width, height)

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for mp4 output
    out = cv2.VideoWriter(output_video_path, fourcc, fps, size)

    for file_name in files:
        frame_path = os.path.join(frame_folder, file_name)
        frame = cv2.imread(frame_path)
        
        if frame is None:
            print(f"Error reading frame: {frame_path}")
            continue
        
        out.write(frame)

    out.release()
    print(f"Video saved to {output_video_path}")
