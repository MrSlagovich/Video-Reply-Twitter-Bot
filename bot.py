from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pytube import YouTube
import os
import subprocess

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.GoodTwitter = r'C:\Users\Bryan Adams\AppData\Roaming\Mozilla\Firefox\Profiles\w605arb8.default-release-1572544189289\extensions\{09707f3a-3940-48dd-a1f5-6d3747a0c330}.xpi'
        self.fp = webdriver.FirefoxProfile(r'C:\Users\Bryan Adams\AppData\Roaming\Mozilla\Firefox\Profiles\w605arb8.default-release-1572544189289')
        self.tweetID =''
        self.fp = webdriver.FirefoxProfile()
        self.bot= webdriver.Firefox(self.fp)
        self.bot.install_addon(self.GoodTwitter)
        self.output = ''



    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')      
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def scan_mentions(self):
        bot = self.bot
        bot.get('https://twitter.com/mentions')
        time.sleep(3)
        

        
    def download_video(self):
        bot = self.bot
        time.sleep(2)
        tweetStatusIDUsername = bot.find_element_by_class_name('tweet').get_attribute('data-permalink-path')
        self.tweetID = tweetStatusIDUsername.split("/")[3]
        tweetLink = 'https://twitter.com'+ tweetStatusIDUsername
        time.sleep(2)
        bot.get(tweetLink)
        time.sleep(3) 
        overlay=bot.find_element_by_id("permalink-overlay-dialog")
        YTUrl=overlay.find_element_by_xpath("//a[@class='twitter-timeline-link u-hidden']").get_attribute("title")
        videoName = r'F:\Programming\Python\Tweet Bot\Videos\{}.mp4'.format(self.tweetID)
        output_file = YouTube(YTUrl).streams.filter(file_extension='mp4').first().download(r'F:\Programming\Python\Tweet Bot\Videos')
        os.rename(output_file, videoName)
        time.sleep(10)
   



    def edit_video(self):
        video = r'"F:\Programming\Python\Tweet Bot\Videos\{}.mp4"'.format(self.tweetID)
        audio = r'"F:\Programming\Python\Tweet Bot\Videos\die.wav"'
        self.output = r'"F:\Programming\Python\Tweet Bot\Videos\{}.mp4"'.format(self.tweetID+'_edited')

        command = "ffmpeg -i {} -i {} -c:v copy -map 0:v:0 -map 1:a:0 {}".format(video, audio,self.output)
        subprocess.call(command)
        time.sleep(3) 


    def upload_video(self):
        bot = self.bot
        bot.find_element_by_class_name('Icon--reply').click()
        time.sleep(6) 
        filePath = r'F:\Programming\Python\Tweet Bot\Videos\broom.jpg'
        #element = bot.find_element_by_css_selector('input.file-input')
        element = bot.find_element_by_xpath("//input[@type='file']")
        bot.execute_script("arguments[0].style.display = 'block';", element)
        time.sleep(1)
        element.send_keys(filePath)



ed = TwitterBot('diehardgaragetheme@yandex.com', open("mypassword.txt").read().strip())
ed.login()
ed.scan_mentions()
# ed.download_video()
# ed.edit_video()
ed.upload_video()


# ed.download_video()


