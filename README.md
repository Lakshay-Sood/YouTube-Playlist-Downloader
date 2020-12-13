# YouTube-Playlist-Downloader
#### A fully functional youtube playlist downloader with no limits.
Now there is no need to waste time on useless websites that usually have limits on either quality, or length, or the number of videos to be downloaded.

#### Not only video but you can also choose to download the videos as mp3 files
So now you can download your favourite music videos or the entire playlist straight away.

## Features
#### 1) All individual video links get copied to the clipboard
'yt_playlist_link_extractor.py' file browses through the URL provided of the youtube playlist and copies all the individual video links in the clipboard in a specified format as required to initialise list data structure in the other file.
#### 2) Chose the file format (mp4, mp3, ...)
Default is mp4 but you can change the 'file_extension' attribute of the streams.filter function.
#### 3) Chose the quality (1080p, 720p, 480p, ...)
Default is set to the highest possible quality on that video but you can change 'res' attribute of the streams.filter function.
#### 4) Chose the download location
Default is the directory where this python script resides but you can change the 'output_path' attribute of the stream.download function.
#### 5) Add numbered prefix to the file names
Default is numbering starting from 1 but you can change or remove it by editing the 'filename_prefix' attribute of the stream.download function.
#### 5) Displays the status of each video and lists if any video(s) gave error while downloading 
The program tries several times to redownload the erroneous videos before printing them out on the console

### Requirements
1) You need to have python 3 installed on your system
2) Download the required packages by running the "  pip install -r requirements.txt  " command in the terminal at the location where you clone/download this repository
3) Download Microsoft Edge webdriver according to your browser version from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    (you can also make minor tweaks in the code to use it with Chrome or Firefox)
4) Voila! You are done.

### Steps
1) Run the 'yt_playlist_link_extractor.py' file in the terminal.
2) Open 'yt_videos_download.py' file in the code editor or IDE and do a 'Ctrl + v' (paste) right after 'urls_to_download = '
3) Input (or paste) the playlist URL when it prompts you to do so.
4) Optional: make changes in the 'yt_videos_download.py' file. (Default: mp4 (video) at best quality)
5) Run the 'yt_videos_download.py' file in the terminal.
6) DONE!

### Future Versions
1) Menu driven program to avoid any code edits by the user to change resolution, file format, etc.
2) Make an executable of the script so that you don't have to install the python modules and won't have to manually run the program from the terminal.
