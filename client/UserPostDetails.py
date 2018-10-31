from InstagramAPI import InstagramAPI
import time

class UserPostDetails:

    def userPostDetails(credentials):
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
                print(obj.LastJson['items'])
                myposts.extend(obj.LastJson['items'])  # merge lists
                time.sleep(2)  # Slows the script down to avoid flooding the servers

            print(len(myposts))

            myposts_sorted = sorted(myposts, key=lambda k:
            k['like_count'],reverse=True)
            #print(userName)
            #print(myposts_sorted)
            time.sleep(2)
