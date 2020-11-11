from __future__ import unicode_literals

from djongo import models

class Posts(models.Model) :
	_id = models.ObjectIdField()
	post_title = models.CharField(max_length=255)
	post_description = models.TextField()

	object = models.DjongoManager()


class Guest_User(models.Model):

	_id = models.ObjectIdField()
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

	object = models.DjongoManager()
