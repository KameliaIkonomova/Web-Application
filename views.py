from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages  

from .forms import PollForm, AnnouncementForm
from .models import Poll, Announcement, Option 


# this decorator prevents user from accessing this url if not logged in
@login_required 
def Index(request):
	"""
		here in the template will be passed:
			list of polls,
			list of announcements
	"""
	context = {
		"polls" : Poll.objects.order_by('-date_created'),
		"announcements" : Announcement.objects.order_by('-date_created'),
	}
	return render(request, "main/index.html", context)


@login_required 
def DetailPoll(request, pk):
	# return to template the poll, corresponding to the provided primary key
	context = {
		"poll" : get_object_or_404(Poll, id = pk)
	}
	return render(request, "main/detail-poll.html", context)



@login_required
def CreateOption(request, pk):
	"""
	this view handles only post requests
	"""
	if request.method == 'POST':
		Option.objects.create(poll = get_object_or_404(Poll, id = pk),
							  title = request.POST.get("title"))
		# after creating object, redirect to detail view of the poll
		return redirect("detail-poll", pk = pk)



@login_required
def VotePoll(request, pk):
	"""
	this view handles only post requests
	"""
	if request.method == "POST":
		# get  the poll object 
		option = get_object_or_404(Option, id = pk)
		# store in a variable the poll id for later,  because  after save we cannot access it anymore 
		poll_id = option.poll.id

		# incremenet the votes by 1 
		option.votes += 1 
		# add user who voted to the voters field, this way they cannot vote more than once 
		option.poll.voters.add(request.user)
		# save/commit both changes 
		option.poll.save()
		option.save()
		# redirect to the detail view of the poll 
		return redirect("detail-poll", pk = poll_id)




@login_required 
def CreatePoll(request):
	if request.method == "POST":
		# the following sequence is how a form should be processed in django 
		form = PollForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Poll created!')
			# redirect to the main page 
			return redirect('index')  

	# passing the form into the template so:
	context = {
		"form" : PollForm,
	}
	return render(request, "main/create_view.html", context)


@login_required 
def CreateAnnouncement(request):
	# this is same with createpoll view, but here we use the announcementform 
	if request.method == "POST":
		form = AnnouncementForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Announcement created!')
			# redirect to the main page here too
			return redirect('index')
	context = {
		"form" :  AnnouncementForm 
	}
	# using the  same html file 
	return render(request, "main/create_view.html", context)