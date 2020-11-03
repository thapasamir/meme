from django.http import HttpResponse
from django.shortcuts import redirect,render


def unauthenticated_user(view_func):
	def wrapper_func(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request,*args,**kwargs)
	return wrapper_func

def allowed_user(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request,*args,**kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			
			if group in allowed_roles:
				return view_func(request,*args,**kwargs)
			else:
				return HttpResponse('<h1 style="text-align: center;vertical-align: middle;font-size: 14rem;">404 Error</h1>')		
		return wrapper_func
	return decorator


	
