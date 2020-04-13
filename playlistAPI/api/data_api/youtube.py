import os

from youtube import API


class YouTube(object):
	def __init__(self, username=""):
		self.client = API(client_id=os.environ('YOUTUBE_CLIENT_ID'),
		                  client_secret=os.environ('YOUTUBE_SECRET'),
		                  api_key=os.environ('YOUTUBE_API_KEY'))
