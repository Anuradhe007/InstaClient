from InstagramAPI import InstagramAPI
from FileGenerator import FileGenerator
import datetime
import time

class UserPostDetails:

    def postFilterByTime(self, userPost, timeToCheck):
        #post_dict = json.loads(userPost)
        postCreatedTime = datetime.datetime.fromtimestamp(userPost['taken_at'])
        givenTime = datetime.datetime.now() - datetime.timedelta(minutes=timeToCheck)
        if postCreatedTime<givenTime:
            return userPost

    def instaDetailExtractor(self, post, apiObject, userName, postCount):
        isLikers = apiObject.getMediaLikers(post['id'])
        fileGenerator = FileGenerator()
        postCaption = post['caption']

        try:
            captionText = postCaption['text']
        except TypeError:
            captionText = ''


        likers = apiObject.LastJson.get('users')
        details = [('Post_id', 'User name', 'Post created date time', 'Caption', 'Timestamp', 'Total likes', 'Likers'),
                   (post['id'], userName, datetime.datetime.fromtimestamp(post['taken_at']), captionText, '', len(likers), '')]
        for liker in likers:
            details.append(('', '', '', '', '', '', liker['username']))
            print(str(datetime.datetime.fromtimestamp(post['taken_at']))+liker['username'])
        fileGenerator.createExcelFile(userName, post['id'],  details, 2, postCount)
            #print(post['likers'])
        # for liker in post['likers']:
        #     if not liker:
        #         print(liker['username'])

    def userPostDetails(self, credentials):
        # InstagramAPI2 = InstagramAPI('geomet.killer', 'Geo123456')
        # InstagramAPI2.login()
        # time.sleep(2)
        # credentials = {'anu_radha_007':InstagramAPI1, 'geomet.killer':InstagramAPI2}

        for userName, obj in credentials.items():
            myposts = []
            has_more_posts = True
            max_id = ""
            while has_more_posts:
                obj.getSelfUserFeed(maxid=max_id)
                if obj.LastJson['more_available'] is not True:
                    has_more_posts = False  # stop condition
                    print("stopped")


                max_id = obj.LastJson.get('next_max_id', '')
                postCount = 0
                for post in obj.LastJson['items']:
                    self.instaDetailExtractor(post, obj, userName, postCount)
                    postCount += 1

                #myposts.extend(obj.LastJson['items'])  # merge lists
                time.sleep(2)  # Slows the script down to avoid flooding the servers

            #print(len(myposts))
#created_at_utc
            myposts_sorted = sorted(myposts, key=lambda k:
            k['like_count'],reverse=True)
            time.sleep(2)

InstagramAPI2 = InstagramAPI('geomet.killer', 'Geo123456')
InstagramAPI2.login()
time.sleep(2)
credentials = {'geomet.killer':InstagramAPI2}
upd = UserPostDetails()
upd.userPostDetails(credentials)

        #resp_dict['value']['queryInfo']['creationTime']  # 1349724919000
