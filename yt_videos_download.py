# Importing YouTube Module from pytube library
from pytube import YouTube
# to print start and end time
import time

# use the 'yt_playlist_link_extractor.py' file to extract videos links from a playlist and just Ctrl+V here
urls_to_download = [
    'https://youtu.be/DQfeB_FKKkc?list=PL-J2q3Ga50oMQa1JdSJxYoZELwOJAXExP']

print("\n\n1) UNCOMMENT 'stream.download()' IN THE FOR LOOP \n2) AND CHECK DOWNLOAD LOCATION \n3) CHECK IF YOU NEED FILENAME PREFIX \n\n")
# print("ALSO check the video quality\n\n")
print("\nStarting Downloads...\n")
current_time = time.strftime("%H:%M:%S", time.localtime())
print('Start Time: {}\n'.format(current_time))


error_links = []  # url list of not downloaded videos
total = len(urls_to_download)  # total videos in playlist
downloaded = 0  # succesfully downloaded videos
tries = 0  # loops of trying to download errorsome links

# end loop after trying 5 times MAX to download videos
while(len(urls_to_download) != 0 and tries < 5):
    for link in urls_to_download:
        try:
            yt = YouTube(link)

            # Downloaded video will be the best quality video
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first()

            ### ⏬ UNCOMMENT ⏬ ###
            stream.download(filename_prefix="{} - ".format(link.split('index=')
                                                           [-1]), output_path=r"D:\Downloads HDD\Courses\Web D 0\Clever Programmer")

            # printing the links downloaded
            print('Downloaded: ', link)
            downloaded += 1
        except:
            print('💥💥ERROR:  ', link)
            error_links.append(link)

    tries += 1
    print("\n{} / {} errors in try {}.\n".format(len(error_links),
                                                 len(urls_to_download), tries))

    if (len(urls_to_download) == len(error_links)):
        print("\nRepeating Errors. Exiting program.\n")
        break

    urls_to_download = error_links
    error_links = []


print("\n{} / {} videos downloaded successfully.\n".format(downloaded, total))

if len(urls_to_download) != 0:
    print("\nError links of {} videos:".format(len(urls_to_download)))
    print(' \n'.join(urls_to_download.__str__().split(' ')))

current_time = time.strftime("%H:%M:%S", time.localtime())
print('\nEnd Time: {}\n'.format(current_time))

######################### MY TRIAL CODE ##############################

# def my_yt_downloader(url):
#     # Creating YouTube object with the link
#     myVideo = YouTube(url)
#     # print("myVideo: ", myVideo, "\n\n")

#     # Creating StreamQuery Object
#     webmStreams = myVideo.streams.filter(res="480p").first()
#     # print("webmStreams: ", webmStreams, "\n\n")

#     # to download file in this directory only
#     # webmStreams.download()
#     print("Video downloaded: ", myVideo.title)


# for youtube_url in url_list:
#     my_yt_downloader(youtube_url)

######### Filtering only audio streams ####################
# audioStream = myVideoStream.filter(type="audio")

# # Accessing first stream in the audio streams and Download it
# audioStream = audioStream.first()
# audioStream.download('D:/')
############## ONLY audio ENDS ############################

######################### MY TRIAL CODE ENDS ##############################
