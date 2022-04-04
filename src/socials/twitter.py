import tweepy
import logging
from typing import List
from ..data_models import RawText

_logger = logging.getLogger()

class TwitterCrawler(object):
    def __init__(self, consumer_key: str, consumer_secret: str,
                 access_token: str, access_token_secret: str):
        """
        Initialize Twitter API.

        Parameters:
            consumer_key: Twitter API consumer key.
            consumer_secret: Twitter API consumer secret.
            access_token: Twitter API access token.
            access_token_secret: Twitter API access token secret.
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        self.client = tweepy.API(auth,
                                 retry_count=3,
                                 retry_delay=0.5,
                                 wait_on_rate_limit=True)

        _logger.debug("TwitterAPI initialized.")

    def get_tweets(self, username: str, max_count: int = 10) -> List[RawText]:
        """
        Get tweets from a user.

        Args:
            username: Twitter username.
            max_count: Maximum number of tweets to return.

        Returns:
            List of tweets (e.g. [{'id': 123, 'text': 'text', 'created_at': 'date'}])
        """
        _logger.debug(f"Getting tweets from {username} with max_count={max_count}")

        tweets = []

        for tweet in tweepy.Cursor(self.client.user_timeline,
                                   screen_name=username,
                                   count=max_count,
                                   tweet_mode="extended").items(max_count):

            if hasattr(tweet, "full_text"):
                    tweet = RawText(
                        id=tweet.id,
                        text=tweet.full_text,
                        created_at=tweet.created_at,
                        source="Twitter")
                    tweets.append(tweet)

            elif hasattr(tweet, "text"):
                    tweet = RawText(
                        id=tweet.id,
                        text=tweet.text,
                        created_at=tweet.created_at,
                        source="Twitter")
                    tweets.append(tweet)
            else:
                _logger.error(f"Tweet has no text or full_text attribute. {tweet}")
                
        _logger.debug(f"Got {len(tweets)} tweets from {username}")

        return tweets

    def get_replies(self, username: str, tweet_id: int, max_count: int = 10) -> List[RawText]:
        """
        Get replies to a tweet.

        Args:
            username: Twitter username.
            tweet_id: Tweet ID.
            max_count: Maximum number of replies to return.

        Returns:
            List of replies (e.g. [{'id': 123, 'text': 'text', 'created_at': 'date'}])
        """
        _logger.debug(f"Getting replies to {tweet_id} from {username} with max_count={max_count}")

        replies = []

        for tweet in tweepy.Cursor(self.client.search_tweets, q=f"to:{username} filter:replies",
                                result_type="recent",
                                count=max_count,
                                since_id=tweet_id,
                                tweet_mode="extended").items(max_count):

            if hasattr(tweet, "in_reply_to_status_id") and tweet.in_reply_to_status_id == tweet_id:   
                if hasattr(tweet, "full_text"):
                        tweet = RawText(
                            id=tweet.id,
                            text=tweet.full_text,
                            created_at=tweet.created_at,
                            source="Twitter")
                        replies.append(tweet)

                elif hasattr(tweet, "text"):
                        tweet = RawText(
                            id=tweet.id,
                            text=tweet.text,
                            created_at=tweet.created_at,
                            source="Twitter")
                        replies.append(tweet)
                else:
                    _logger.error(f"Tweet has no text or full_text attribute. {tweet}")

        _logger.debug(f"Got {len(replies)} replies from {username}")
        
        return replies

    def get_tweets_by_keyword(self, keyword: str, max_count: int = 10) -> List[RawText]:
        """Get tweets by a keyword.

        Args:
            query: Keyword.
            max_count: Maximum number of tweets to return.

        Returns:
            List of tweets (e.g. [{'id': 123, 'text': 'text', 'created_at': 'date'}])
        """
        _logger.debug(f"Getting tweets by keyword={keyword} with max_count={max_count}")

        tweets = []

        for tweet in tweepy.Cursor(
            self.client.search_tweets,
            q=keyword,
            result_type="recent",
            count=max_count,
            tweet_mode="extended").items(max_count):

            if hasattr(tweet, "full_text"):
                    tweet = RawText(
                        id=tweet.id,
                        text=tweet.full_text,
                        created_at=tweet.created_at,
                        source="Twitter")
                    tweets.append(tweet)

            elif hasattr(tweet, "text"):
                    tweet = RawText(
                        id=tweet.id,
                        text=tweet.text,
                        created_at=tweet.created_at,
                        source="Twitter")
                    tweets.append(tweet)
            else:
                _logger.error(f"Tweet has no text or full_text attribute. {tweet}")
                
        _logger.debug(f"Got {len(tweets)} tweets by {keyword}.")

        return tweets