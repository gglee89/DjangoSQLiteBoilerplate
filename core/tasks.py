import instaloader
from celery import shared_task

@shared_task
def run_script(USER, PASSWORD, SHORTCODE):
  print('Running run_script @hashtag_kpi.py')

  # INSTALOADER SETUP
  L = instaloader.Instaloader()
  PROFILE = USER  
  L.login(USER, PASSWORD) # (Login)
  # Load session previously saved with `instaloader -l USERNAME`:
  # L.load_session_from_file(USER)
  profile = instaloader.Profile.from_username(L.context, PROFILE)

  likes = set()
  print("Fetching likes of all posts of profile {}.".format(profile.username))
  for post in profile.get_posts():
      print(post)
      likes = likes | set(post.get_likes())

  print("Fetching followers of profile {}.".format(profile.username))
  followers = set(profile.get_followers())