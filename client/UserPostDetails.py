from InstagramAPI import InstagramAPI
import datetime
import time

class UserPostDetails:

    def postFilterByTime(self, userPost, timeToCheck):
        #post_dict = json.loads(userPost)
        postCreatedTime = datetime.datetime.fromtimestamp(userPost['taken_at'])
        givenTime = datetime.datetime.now() - datetime.timedelta(minutes=timeToCheck)
        if postCreatedTime<givenTime:
            return userPost

    def instaDetailExtractor(self, post, apiObject):
        isLikers = apiObject.getMediaLikers(post['id'])
        if isLikers:
            likers = apiObject.LastJson.get('users')
            for liker in likers:
                print(str(datetime.datetime.fromtimestamp(post['taken_at']))+liker['username'])
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
                #print(obj.LastJson)
                for post in obj.LastJson['items']:
                    #p = self.postFilterByTime(post, 10)
                    self.instaDetailExtractor(post, obj)
                            #self.postDetailExtractor(p)
                            #if not p:
                            #   break

                myposts.extend(obj.LastJson['items'])  # merge lists
                time.sleep(2)  # Slows the script down to avoid flooding the servers

            #print(len(myposts))
#created_at_utc
            myposts_sorted = sorted(myposts, key=lambda k:
            k['like_count'],reverse=True)
            #print(userName)
            #print(myposts_sorted)
            time.sleep(2)

InstagramAPI2 = InstagramAPI('geomet.killer', 'Geo123456')
InstagramAPI2.login()
time.sleep(2)
credentials = {'geomet.killer':InstagramAPI2}
upd = UserPostDetails()
upd.userPostDetails(credentials)

        #resp_dict['value']['queryInfo']['creationTime']  # 1349724919000
