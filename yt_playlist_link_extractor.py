from selenium import webdriver
import pyperclip as pc
import time
###################################################################################################

browser = webdriver.Edge('D:\\Downloads HDD\\#Setups\\msedgedriver')
playlist_url = input("Enter the url of the youtube playlist: ")
browser.get(playlist_url)

videos = browser.find_elements_by_css_selector(
    'a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer')

# for playlist with more than 100 videos (cuz youtube does lazy loading and only loads links of first 100 videos)
max_len = 100
if (len(videos) >= max_len):
    browser.execute_script('arguments[0].scrollIntoView(true);', videos[-1])
    time.sleep(2)  # INCREASE sleep duration on slow network
    videos = browser.find_elements_by_css_selector(
        'a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer')
    max_len += 100

url_list = []

for v in videos:
    url_list.append(v.get_attribute('href'))

browser.close()

print("COMPLETED: {} videos.".format(len(url_list)))
# print(url_list)
# copies the list (in string form) to the clipboard
pc.copy(" \n".join(url_list.__str__().split(' ')))
print('All links copied as Array of Strings(links) into clipboard. Just Ctrl + V now.')
