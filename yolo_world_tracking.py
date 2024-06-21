from collections import defaultdict
from ultils.generate_video_from_frames import generate_video_from_frames

import cv2
import numpy as np

from ultralytics import YOLO

class PromptedObjectsTracking:
    def __init__(self, model = "yolov8x-world.pt"):
        # Load the YOLOv8 model
        model = YOLO(model)

    def set_classes(self, classes_name: [str]):
        model.set_classes(classes_name)

    def track(self, video_path, output_video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Store the track history
        track_history = defaultdict(lambda: [])

        tracked_frames = []
        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 tracking on the frame, persisting tracks between frames
                results = model.track(frame, persist=True)

                # Get the boxes and track IDs
                boxes = results[0].boxes.xywh.cpu()
                track_ids = results[0].boxes.id.int().cpu().tolist()

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Plot the tracks
                for box, track_id in zip(boxes, track_ids):
                    x, y, w, h = box
                    track = track_history[track_id]
                    track.append((float(x), float(y)))  # x, y center point
                    if len(track) > 30:  # retain 90 tracks for 90 frames
                        track.pop(0)

                    # Draw the tracking lines
                    points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                    cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)
                tracked_frames.append(annotated_frame)

            else:
                # Break the loop if the end of the video is reached
                break

        # Release the video capture object and close the display window
        cap.release()

        generate_video_from_frames(tracked_framesm output_video_path)
    

if __name__ == "__main__":
    output_video_path = "./tracked_video.mp4"
    video_path = "datasets/horse.mp4"
    promted_objects_track = PromptedObjectsTracking()
    promted_objects_track.set_classes(["horse"])
    promted_objects_track.track(video_path, output_video_path)