# pip install instaloader
import os
import instaloader

def profile(uname):
    instance = instaloader.Instaloader()

    os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))

    return ( instance.download_profile(uname,profile_pic_only=True))


profile('narendramodi')
