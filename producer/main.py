import praw

client_id = "_xspuN5O4G3UQpfPHSf0Hg"
client_secret = "9PxgHzL_6e2qJBYH6lGTneJNT8IDFw"
username = "Comfortable-Bell3887"
password = "kafka22agh"
subreddit_name = "data"


def main():
    reddit = praw.Reddit(
        user_agent=username,
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password
    )

    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.top(time_filter="all", limit=None):
        sub = {
            "id": submission.id,
            "spoiler": submission.spoiler,
            "over_18": submission.over_18,
            "title": submission.title,
            "award_count": submission.total_awards_received,
            "awarder_count": len(submission.awarders),
            "created_utc": int(submission.created_utc),
            "thumbnail": submission.thumbnail,
            "thumbnail_height": submission.thumbnail_height,
            "thumbnail_width": submission.thumbnail_width,
            "url": submission.url,
            "score": submission.score,
            "upvote_ratio": submission.upvote_ratio,
            "shortlink": submission.shortlink
        }
        if hasattr(submission, 'post_hint'):
            sub["post_hint"] = submission.post_hint

        print(sub)


if __name__ == "__main__":
    main()
