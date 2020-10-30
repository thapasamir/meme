from .forms import Create_CateogryForm,Create_PostForm,UserCreationform
from django.shortcuts import render,redirect
from .models import Create_Post,Create_Cateogry
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .filter import PostFilters
#Views section of of homepage
def home(request):
	post = Create_Post.objects.all()
	search = PostFilters(request.GET,queryset=post)
	post = search.qs
	return render(request,'html/home.html',{'post':post,'search':PostFilters})

#Views section of cateogry  page
def cateogry(request):
	Cateogry = Create_Cateogry.objects.all()
	return render(request,'html/cateogry.html',{'Cateogry':Cateogry})

#Views section of explore  page
@login_required(login_url='log_in')
def explore(request,id):
	reasult = Create_Post.objects.filter(cateogry=id)
	return render(request,'html/explore.html',{'reasult':reasult})


#Views section of login page
def log_in(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,"Your username or password is incorrect")

	return render(request,'admin/login.html')

#Views section of login page
def log_out(request):
	logout(request)
	return redirect('log_in')

#Views section of sign up page
def signup(request):
	if request.user.is_authenticated:
		messages.info(request,"Already logined")
		return redirect('home')
	else:
		form = UserCreationform()
		if request.method == "POST":
			form = UserCreationform(request.POST)
			if form.is_valid():
				form.save()
				name = form.cleaned_data.get('username')
				messages.success(request,"Yor account was created " + name)
				return redirect('log_in')


		return render(request,'admin/signup.html',{"form":form})


#Views section of about page
def about(request):
	return render(request,'html/about.html')



#Views section of article page
def article(request):
	return render(request,'html/article.html')

#Views section of createpost
def createpost(request):
	form = Create_PostForm()
	if request.method == "POST":
		print("I am worling very finely")
		form = Create_PostForm(request.POST, request.FILES)
		if form.is_valid():
			Title = form.cleaned_data.get("Title")
			photo = form.cleaned_data.get("photo")
			post_cateogry = form.cleaned_data.get("cateogry")
			#emails = form.cleaned_data.get("share_email_with")
			users = Create_Post.objects.filter(cateogry=post_cateogry)
			#users = User.objects.filter(email__in=emails)
			obj = Create_Post.objects.create( Title = Title,photo = photo)
			obj.save()
			#instance = Setupuser.objects.create(organization=org)
			obj.cateogry.add(users)





	return render(request,'admin/createpost.html',{'form':form})


#Views section of creategroup
def createcateogry(request):
	form = Create_CateogryForm()
	if request.method == "POST":
		print("I am worling very finely")
		form = Create_CateogryForm(request.POST,request.FILES)
		if form.is_valid():
			Title = form.cleaned_data.get("Title")
			Description = form.cleaned_data.get("Description")
			photo = form.cleaned_data.get("photo")
			obj = Create_Cateogry.objects.create( 
                                 Title = Title,  
                                 photo = photo,
                                 Description = Description,
                                 ) 
			obj2 = Create_Cateogry.objects.filter(Description=Description)
			obj2.save()
			obj.save()
	else:
		form = Create_CateogryForm()
	return render(request,'admin/createcateogry.html',{'form':form})