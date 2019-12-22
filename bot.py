from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pytube import YouTube
import os
import subprocess
from selenium.webdriver.common.action_chains import ActionChains

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.GoodTwitter = r'C:\Users\Bryan Adams\AppData\Roaming\Mozilla\Firefox\Profiles\w605arb8.default-release-1572544189289\extensions\{09707f3a-3940-48dd-a1f5-6d3747a0c330}.xpi'
        #self.fp = webdriver.FirefoxProfile(r'C:\Users\Bryan Adams\AppData\Roaming\Mozilla\Firefox\Profiles\w605arb8.default-release-1572544189289')
        self.tweetID =''
        self.fp = webdriver.FirefoxProfile()
        self.bot= webdriver.Firefox(self.fp)
        self.bot.install_addon(self.GoodTwitter)
        self.output = ''
        self.tweetLink=""


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
        self.tweetLink = 'https://twitter.com'+ tweetStatusIDUsername
        time.sleep(2)
        bot.get(self.tweetLink)
        time.sleep(3) 
        overlay=bot.find_element_by_id("permalink-overlay-dialog")
        YTUrl=overlay.find_element_by_xpath("//a[@class='twitter-timeline-link u-hidden']").get_attribute("title")
        YouTube(YTUrl).streams.filter(file_extension='mp4').first().download(r'F:\Programming\GitHub\Video-Reply-Twitter-Bot\Videos',self.tweetID )
        time.sleep(5) 




    def edit_video(self):
        video = r'"F:\Programming\GitHub\Video-Reply-Twitter-Bot\Videos\{}.mp4"'.format(self.tweetID)
        audio = r'"F:\Programming\GitHub\Video-Reply-Twitter-Bot\Videos\die.wav"'
        self.output = r'"F:\Programming\GitHub\Video-Reply-Twitter-Bot\Videos\{}.mp4"'.format(self.tweetID+'_edited')
        command = "ffmpeg -i {} -i {} -c:v copy -map 0:v:0 -map 1:a:0 -stream_loop {} -shortest".format(video, audio,self.output)
        subprocess.call(command)
        
    def upload_video(self):
        bot = self.bot        
        time.sleep(3) 
        bot.find_element_by_css_selector('#permalink-overlay-dialog .Icon--reply').click()
        filePath = r'F:\Programming\GitHub\Video-Reply-Twitter-Bot\Videos\{}.mp4'.format(self.tweetID+'_edited')
        element = bot.find_element_by_css_selector('#permalink-overlay-dialog .file-input')
        time.sleep(1)
        element.send_keys(filePath)
        time.sleep(4)
        right_drag_element = bot.find_element_by_class_name('VideoTrim-rightHandle')
        left_drag_element = bot.find_element_by_class_name('VideoTrim-leftHandle')
        middle_drag_element = bot.find_element_by_class_name('VideoTrim-midHandleCursor')
        ActionChains(bot).drag_and_drop_by_offset(middle_drag_element, -500,0).perform()
        time.sleep(1)
        ActionChains(bot).drag_and_drop_by_offset(right_drag_element, 300,0).perform()
        time.sleep(1)
        bot.find_element_by_css_selector('#media-edit-dialog .EdgeButton.EdgeButton--primary.js-done').click()
        time.sleep(1)
        bot.find_element_by_css_selector('#permalink-overlay-dialog .tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn').click()  







ed = TwitterBot('mrslagovich', open("mypassword.txt").read().strip())
ed.login()
ed.scan_mentions()
ed.download_video()
ed.edit_video()
#ed.upload_video()
#ed.download_video()


