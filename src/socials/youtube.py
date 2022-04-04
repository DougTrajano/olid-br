import logging
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.data_models import RawText
from retrying import retry

_logger = logging.getLogger()

class YouTubeCrawler(object):
    def __init__(self, api_key: str):
        self.api = build("youtube", "v3",
                         developerKey=api_key)
        self.call_counter = 0
        self.date_format = "%Y-%m-%dT%H:%M:%SZ"

        self.comments = None
        self.videos = None

    @staticmethod
    def _get_video_id(video_url: str):
        """Get video id from a YouTube video url.

        Args:
        - video_url: YouTube video url (e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ)

        Returns:
        - video_id: YouTube video id
        """
        return video_url.split("watch?v=")[1].split("&")[0]

    def _format_date(self, date: str):
        """Format date to YYYY-MM-DDTHH:MM:SSZ"""
        return datetime.datetime.strptime(date, self.date_format)

    @retry(retry_on_exception=lambda e: isinstance(e, HttpError),
           wait_exponential_multiplier=1000,
           wait_exponential_max=10000,
           stop_max_attempt_number=5)
    def _yt_comments_call(self, video_id: str, max_results: int):
        """
        Call YouTube API to get comments from a video.

        Args:
        - video_id: YouTube video id
        - max_results: maximum number of comments to retrieve

        Returns:
        - comments: list of comments
        """
        response = self.api.commentThreads().list(
            part="snippet,replies",
            maxResults=max_results,
            videoId=video_id).execute()
        self.call_counter += 1
        return response

    def _check_max_results(self, max_results: int = 50):
        if max_results > 50:
            max_results = 50
            _logger.warning(f"Maximum number of comments is 50. Setting max_results to 50.")
        return max_results

    def get_channel_videos(self, channel_id: str, max_results: int = 50):
        """Get videos from a channel

        Args:
        - channel_id: YouTube channel id

        Returns:
        - videos: list of videos
        """
        # empty list for storing videos
        self.videos = []
    
        max_results = self._check_max_results(max_results)

        # retrieve youtube channel results
        channel_response = self.api.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=max_results
        ).execute()
        self.call_counter += 1
    
        # iterate channel response
        while channel_response:
            
            # extracting required info
            # from each result object 
            for item in channel_response["items"]:
                
                try:
                    # Extracting video id
                    video_id = item["id"]["videoId"]
                    
                    # Extracting video title
                    video_title = item["snippet"]["title"]
                    
                    # Store video id and title in list
                    self.videos.append({"id": video_id, "title": video_title})
                except:
                    pass

                print(f"\rCollected {len(self.videos)} videos for channel_id: {channel_id}.", end="")
    
            # Again repeat
            if "nextPageToken" in channel_response:
                channel_response = self.api.search().list(
                    part="snippet",
                    channelId=channel_id,
                    maxResults=max_results,
                    pageToken=channel_response["nextPageToken"]
                ).execute()
                self.call_counter += 1
            else:
                break
    
        # return list of videos
        print(f"\rCollected {len(self.videos)} videos for channel_id: {channel_id}.")
        videos = self.videos.copy()
        self.videos = None
        return videos

    def get_video_comments(self, video_id: str, max_results: int = 50, max_comments: int = None):
        """Get comments and replies from a given video.

        Args:
        - video_id: YouTube video id
        - max_results: maximum number of comments to retrieve (value between 0 and 50).

        Returns:
        - comments: list of comments
        """
        # empty list for storing reply
        self.comments = []

        max_results = self._check_max_results(max_results)
    
        # retrieve youtube video results
        video_response= self._yt_comments_call(video_id, max_results)
    
        # iterate video response
        while video_response:
            # extracting required info
            # from each result object 
            for item in video_response["items"]:
                
                # Extracting comments
                comment = RawText(
                    id=item["id"],
                    text=item["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                    created_at=self._format_date(item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]),
                    source="YouTube")

                self.comments.append(comment)

                # counting number of reply of comment
                replycount = item["snippet"]["totalReplyCount"]
    
                # if reply is there
                if replycount > 0:
                    
                    # iterate through all reply
                    if item.get("replies"):
                        for reply in item["replies"]["comments"]:                        
                            reply = RawText(
                                id=reply["id"],
                                text=reply["snippet"]["textOriginal"],
                                created_at=self._format_date(reply["snippet"]["publishedAt"]),
                                source="YouTube")

                            # Store reply is list
                            self.comments.append(reply)

                print(f"\rCollected {len(self.comments)} comments for video_id: {video_id}", end="")
            
            if isinstance(max_comments, int) and len(self.comments) >= max_comments:
                print(f"\rCollected {len(self.comments)} comments for video_id: {video_id}")
                comments = self.comments.copy()
                self.comments = None
                return comments

            # Again repeat
            if "nextPageToken" in video_response:
                video_response = self._yt_comments_call(video_id, max_results)
            else:
                break
            
        print(f"\rCollected {len(self.comments)} comments for video_id: {video_id}")
        comments = self.comments.copy()
        self.comments = None
        return comments