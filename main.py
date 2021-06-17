import instaloader
bot = instaloader.Instaloader()
username = "INSERT INSTAGRAM ACCOUNT USERNAME HERE"
print(bot.download_profile(username,profile_pic_only=True))
