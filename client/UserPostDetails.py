from InstagramAPI import InstagramAPI
from FileGenerator import FileGenerator
import datetime
import time

class UserPostDetails:

    def postFilterByTime(self, userPost, clientStartedTime, clientEndingTime):
        postCreatedTime = datetime.datetime.fromtimestamp(userPost['taken_at'])
        if (postCreatedTime > clientStartedTime) and (postCreatedTime < clientEndingTime):
            return userPost
        return False

    def instaDetailExtractor(self, post, apiObject, userName, postCount):
        isLikers = apiObject.getMediaLikers(post['id'])
        fileGenerator = FileGenerator()
        postCaption = post['caption']

        try:
            captionText = postCaption['text']
        except TypeError:
            captionText = ''

        likers = apiObject.LastJson.get('users')
        details = [('User name', 'Post created date time', 'Caption', 'Total likes', 'Likers'),
                   (userName, datetime.datetime.fromtimestamp(post['taken_at']), captionText, len(likers), '')]
        for liker in likers:
            details.append(('', '', '', '', liker['username']))
        fileGenerator.createExcelFile(userName, datetime.datetime.fromtimestamp(post['taken_at']), details, '/home/anuradha/insta/', postCount)

    def userPostDetails(self, credentials, clientStartedTime, clientEndingTime):
        for userName, obj in credentials.items():
            myposts = []
            has_more_posts = True
            max_id = ""
            while has_more_posts:
                obj.getSelfUserFeed(maxid=max_id)
                if obj.LastJson['more_available'] is not True:
                    has_more_posts = False  # stop condition

                max_id = obj.LastJson.get('next_max_id', '')
                postCount = 1
                for post in obj.LastJson['items']:
                    selectedPost = self.postFilterByTime(post, clientStartedTime, clientEndingTime)
                    if selectedPost != False:
                        self.instaDetailExtractor(selectedPost, obj, userName, postCount)
                    postCount += 1
                time.sleep(2)  # Slows the script down to avoid flooding the servers
            sorted(myposts, key=lambda k:
            k['like_count'],reverse=True)
            time.sleep(2)
