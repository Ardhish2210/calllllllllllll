import yt_dlp

# Define options for yt-dlp to extract audio and convert it to mp3
ydl_opts = {
    'format': 'bestaudio/best',  # Download the best quality audio
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract the audio
        'preferredcodec': 'mp3',  # Convert audio to mp3
        'preferredquality': '192',  # Set quality to 192 kbps
    }],
    'ffmpeg-location': './',  # Specify location of FFmpeg (ensure ffmpeg is installed)
    'outtmpl': "./%(id)s.%(ext)s",  # Save the file with its video ID and extension
}

# Function to download and save audio from a YouTube link
def save_audio(link):
    link = link.strip()  # Clean up the link in case there are extra spaces
    
    # Inner function to handle yt-dlp extraction
    def get_vid(link):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # Use yt-dlp to handle download
            return ydl.extract_info(link)  # Extract video info and download
    
    # Call the yt-dlp function to get and download the audio
    meta = get_vid(link)
    save_location = meta['id'] + ".mp3"  # Construct the saved file name as the video ID with .mp3
    
    print('Saved mp3 to', save_location)  # Print confirmation of the saved file
    
    return save_location  # Return the location of the saved audio file

# Example usage
# video_url = "https://www.youtube.com/watch?v=VIDEO_ID"
# save_audio(video_url)
