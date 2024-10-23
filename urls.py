from django.urls import path

from . import views 


urlpatterns = [
	path("", views.Index, name = "index"),
	# path to detail view  of a poll (here options will be shown and user can vote)
	path("poll/detail/<int:pk>/", views.DetailPoll, name = 'detail-poll'),
	# path to create a new option
	path("create/option/<int:pk>/", views.CreateOption, name = 'create-option'),
	# path to create a new poll
	path("create/poll", views.CreatePoll, name = "create-poll"),
	# path to create a new annnouncement
	path("create/announcement", views.CreateAnnouncement, name = "create-announcement"),
	# path to vote 
	path("vote/poll/<int:pk>/", views.VotePoll, name = 'vote-poll'),
]
