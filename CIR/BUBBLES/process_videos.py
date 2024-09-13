import cv2
import numpy as np
import os
import sys

def create_directories(video_name):
    """Create a 'bub/frm' directory structure for each video."""
    base_dir = os.path.join(video_name, 'bub')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    frm_dir = os.path.join(base_dir, 'frm')
    if not os.path.exists(frm_dir):
        os.makedirs(frm_dir)
    return frm_dir

def remove_subtitles(frame):
    """Remove hardcoded subtitles from the frame."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    mask = cv2.bitwise_not(binary)
    inpainted_frame = cv2.inpaint(frame, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    return inpainted_frame

def extract_and_process_frames(video_path, output_dir):
    """Extract frames from video, process them to remove subtitles, and save them."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}.")
        return
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_dir = os.path.join(output_dir, f'frame_{frame_count:04d}')
        os.makedirs(frame_dir, exist_ok=True)
        
        original_filename = os.path.join(frame_dir, 'frame.jpg')
        cv2.imwrite(original_filename, frame)
        
        processed_frame = remove_subtitles(frame)
        processed_filename = os.path.join(frame_dir, 'frame_no_subtitles.jpg')
        cv2.imwrite(processed_filename, processed_frame)
        
        frame_count += 1
    
    cap.release()
    print(f"Frames processed and saved for video {os.path.basename(video_path)}: {frame_count}")

def process_videos(input_dir):
    """Process all .avi video files in the input directory."""
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.avi'):
            video_path = os.path.join(input_dir, filename)
            video_name = os.path.splitext(filename)[0]
            print(f"Processing video: {video_path}")
            frm_dir = create_directories(video_name)
            extract_and_process_frames(video_path, frm_dir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        print("Error: The provided path is not a directory.")
        sys.exit(1)
    
    process_videos(input_dir)

