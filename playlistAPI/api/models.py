from django.db import models
from django_mysql.models import ListTextField


class Song(models.Model):
	# id field created by default
	id = models.UUIDField(primary_key=True)
	duration = models.IntegerField(default=0)
	title = models.CharField('Title', max_length=100)
	artists = ListTextField(base_field=models.CharField(max_length=100))
	album = models.CharField('Album name', max_length=100, blank=True)
	track_number = models.SmallIntegerField('Track number', blank=True, null=True)
	release_date = models.DateTimeField(null=True)
	cover_image_url = models.TextField('Cover image', default='playlistAPI/static/assets/default_song_img.jpg')
	date_row_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'songs'

	def __unicode__(self):
		return "%s" % self.title


class songsByPlatform(models.Model):
	added_date = models.DateTimeField(auto_now_add=True)
	songID = models.UUIDField(primary_key=True)
	spotifyID = models.TextField(blank=True)
	appleID = models.TextField(blank=True)
	youtubeID = models.TextField(blank=True)

	class Meta:
		db_table = 'songs_by_platform'
