from django.db import models
from django.utils import timezone 


from users.models import CustomUser



class Poll(models.Model):
	title = models.CharField(max_length = 1024)
	# this field, will allow us to prevent users from voting more than once 
	voters = models.ManyToManyField(CustomUser, default = None, blank = True, related_name = "polls_voted")
	# this field we need in order to order the items, newest first 
	date_created = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title 




class Option(models.Model):
	title = models.CharField(max_length = 512)
	# related name allows us to access the foreignkey objects, directly from the poll object 
	poll = models.ForeignKey(Poll, on_delete = models.CASCADE, default = None, blank = True, null = True, related_name = "options")
	# votes will be incremeneted by 1
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return f"Option for: {self.poll.title}, {self.title}"



class Announcement(models.Model):
	title = models.CharField(max_length = 1024)
	# this field we need in order to order the items, newest first 
	date_created = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title
