import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt

# We use pmaw instead of praw to circumvent praw's limit scraping
api = PushshiftAPI()

# Specify subreddit to scrape and number of comments/posts to scrape
subreddit = "wallstreetbets"
limit = 500000

# Specify time-frame of post/comments to scrape 
before = int(dt.datetime(2022,10,1,0,0).timestamp())
after = int(dt.datetime(2022,9,1,0,0).timestamp())

# Scrape it
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
submissions = api.search_submissions(subreddit=subreddit, limit=limit, before=before, after=after)

# Dump it
comments_pd = pd.DataFrame(comments)
submissions_pd = pd.DataFrame(submissions)
comments_pd.to_csv('data/wsb_comments.csv')
submissions_pd.to_csv('data/wsb_posts.csv')
