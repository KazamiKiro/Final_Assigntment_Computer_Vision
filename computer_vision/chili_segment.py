import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

def segment_chili(frame, model_path='models/chili_segmen.pt'):
    """
    Detect chilies in a given frame using a YOLOv8n model.

    Args:
        frame (numpy array): Input frame to detect chilies in.
        model_path (str, optional): Path to the YOLOv8n model. Defaults to 'models/chili_segment.pt'.

    Returns:
        tuple: A tuple containing the segmented frame and the number of detections.
    """
    # Load the YOLOv8n model
    model = YOLO(model_path)

    # Initialize variables
    detection_amount = 0  # Initialize detection count
    combination_masking = np.zeros_like(frame, dtype=np.uint8)  # Initialize combined mask

    # Run batched inference on the input frame
    results = model(frame)

    for result in results:
        if hasattr(result, 'masks') and result.masks is not None:
            masker = result.masks.data.cpu().numpy()  # Convert mask to numpy array

            for mask in masker:
                print(mask)
                detection_amount += 1  # Increment detection count
                mask = mask.squeeze()  # Remove single-dimensional entries if any
                mask = (mask * 255).astype(np.uint8)  # Convert mask to binary image (0 and 255)

                # Check if mask dimensions match the frame
                if mask.shape != frame.shape[:2]:
                    mask = cv2.resize(mask, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

                # Create a colored mask for overlay
                colored_masking_red = np.zeros_like(frame, dtype=np.uint8)
                colored_masking_red[mask > 0] = (0, 0, 255)  # Set mask color (green in this example)

                # Combine the colored mask with the combined mask
                combination_masking = cv2.addWeighted(combination_masking, 1, colored_masking_red, 0.5, 0)

    # Combine the original frame with the combined mask
    frame_segmentasi = cv2.addWeighted(frame, 1, combination_masking, 0.5, 0)

    return frame_segmentasi, detection_amount
