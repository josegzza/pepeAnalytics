from Helpers.TweetHelper import TweetHelper
from Helpers.ImageHelper import ImageHelper

# TweetApi = TweetHelper()
# TweetApi.tweetIt("Hello")

img = ImageHelper()
img.createImg('templateWhite.png', 'test1.jpg', 'arial.ttf', "Baseball test chart")
img.saveImg()
