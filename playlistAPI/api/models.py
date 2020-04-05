from django.db import models


class Song(models.Model):
	# id field created by default
	duration = models.IntegerField('Song duration (ms)', editable=False, default=0)
	title = models.CharField('Title', max_length=100)
	artists = models.TextField('Artist', blank=True)
	album = models.CharField('Album name', max_length=100, blank=True)
	track_number = models.SmallIntegerField('Track number', blank=True, null=True)
	genre = models.CharField('Genre', max_length=50, blank=True)
	release_date = models.DateTimeField(blank=True)
	cover_image_url = models.ImageField('Cover image', upload_to='playlistAPI/static/assets',
	                                    default='playlistAPI/static/assets/default_song_img.jpg')
	date_row_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'songs'

	def __unicode__(self):
		return "%s" % self.title


class songsByPlatform(models.Model):
	added_date = models.DateTimeField(auto_now_add=True)
	songID = models.IntegerField(primary_key=True)
	spotifyID = models.TextField(blank=True)
	appleID = models.TextField(blank=True)
	youtubeID = models.TextField(blank=True)

	class Meta:
		db_table = 'songs_by_platform'
