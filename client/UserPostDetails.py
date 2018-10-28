from InstagramAPI import InstagramAPI
import time

class UserPostDetails:

    myposts = []
    has_more_posts = True
    max_id = ""

    InstagramAPI = InstagramAPI("geomet.killer", "Geo123456")
    InstagramAPI.login()

    while has_more_posts:
        InstagramAPI.getSelfUserFeed(maxid=max_id)
        if InstagramAPI.LastJson['more_available'] is not True:
            has_more_posts = False  # stop condition
            print("stopped")

        max_id = InstagramAPI.LastJson.get('next_max_id', '')
        myposts.extend(InstagramAPI.LastJson['items'])  # merge lists
        time.sleep(2)  # Slows the script down to avoid flooding the servers

    print(len(myposts))

    myposts_sorted = sorted(myposts, key=lambda k:
    k['like_count'],reverse=True)

    print(myposts_sorted)
