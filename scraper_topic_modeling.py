subreddit="wallstreetbets"
limit=500000

comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
submissions = api.search_submissions(subreddit=subreddit, limit=limit, before=before, after=after)

comments_pd = pd.DataFrame(comments)
submissions_pd = pd.DataFrame(submissions)

comments_pd.to_csv('data/wsb_comments.csv')
submissions_pd.to_csv('data/wsb_posts.csv')