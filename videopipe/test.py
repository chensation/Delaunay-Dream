from Pipe import get_frames, apply_filter, generate_gray
import cv2 as cv

def main():
    original_frames = get_frames()
    filtered_frames = []
    for frame in original_frames:
        filtered_frames.append(apply_filter(frame))
    generate_gray(filtered_frames)
    capture = cv.VideoCapture('sampleout.avi')
    while True:
        success, frame = capture.read()
        if not success:
            break
        cv.imshow("Result", frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()
    return


if __name__ == '__main__':
    main()