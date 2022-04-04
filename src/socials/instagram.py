import time
import datetime
import random
from instagram_scraper import InstagramScraper
from pydantic import BaseModel, Field, validator
from typing import Any

class InstaRequest(BaseModel):
    type: str = Field("user", title="Type of request")
    username: str = Field(None, title="Username")
    shortcode: str = Field(None, title="Shortcode of the post")
    response: Any = Field(None, title="Result of the request")
    created_at: datetime.datetime = Field(datetime.datetime.now(), title="Created at")

    @validator("type")
    def type_validator(cls, v):
        if v not in ["user", "post"]:
            raise ValueError(f"Invalid type of request: {v}")
        return v

class InstagramAPI(object):
    def __init__(self, login_user: str = None, login_pass: str = None,
                 wait_time: bool = True, wait_min: float = 1.0, wait_max: float = 3.0):
        """
        InstagramAPI helps you to scrape instagram posts and comments.

        Arguments:
        - login_user: Instagram username
        - login_pass: Instagram password
        - wait_time: Time to wait when you are on a rate limit
        - wait_min: Minimum time to wait when you are on a rate limit
        - wait_max: Maximum time to wait when you are on a rate limit
        """
        self.wait_time = wait_time
        self.wait_max = wait_max
        self.wait_min = wait_min

        if login_user and login_pass:
            args = {"login_user": login_user, "login_pass": login_pass}
            self.insta = InstagramScraper(**args)
            self.insta.authenticate_with_login()
        else:    
            self.insta = InstagramScraper()    
            self.insta.authenticate_as_guest()

    def _wait_time(self):
        if self.wait_time:
            time.sleep(random.uniform(self.wait_min, self.wait_max))

    def get_posts(self, username: str):
        shared_data = self.insta.get_shared_data_userinfo(username=username)
        
        posts = []
        for post in self.insta.query_media_gen(shared_data):
            posts.append(post)
            
        return posts

    def get_post_comments(self, shortcode: str):
        comments = []
        for comment in self.insta.query_comments_gen(shortcode):
            comments.append(comment)
        return comments

    def get_all_comments(self, username: str):
        posts = self.get_posts(username)
        
        comments = []
        for post in posts:
            try:
                post_comments = self.get_post_comments(post["shortcode"])
                comments.append(post_comments)
            except Exception as e:
                while True:
                    self._wait_time()
                    try:
                        post_comments = self.get_post_comments(post["shortcode"])
                        comments.append(post_comments)
                        break
                    except:
                        continue

        return comments