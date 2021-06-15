from Pipe import get_frames, apply_filter, generate_result
import cv2 as cv

def main():
    original_frames = get_frames()
    filtered_frames = []
    for frame in original_frames:
        filtered_frames.append(apply_filter(frame))
    generate_result(filtered_frames)
    return


if __name__ == '__main__':
    main()