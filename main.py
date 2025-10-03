from utils import read_video, save_video

def main():
    #read video
    video_frames = read_video("videos/match.mp4")

    #save video
    save_video(video_frames, 'output_videos/output_video.avi')

if __name__ == "__main__":
    main()