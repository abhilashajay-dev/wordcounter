from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home(request):
	return render(request,"home.html")

def counted(request):
	fulltext = request.GET["fulltext"]
	wordlist=fulltext.split()
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1



	return render(request,"count.html",{"fulltext":fulltext, "count":len(wordlist),"worddictionary":worddictionary.items()})


def about(request):
	template_name="base.html"
	obj= get_template(template_name)
	title ="this is about page"
	context ={"body":title, "title_header":"about page"}
	rendered_obj=obj.render(context)
	return HttpResponse(rendered_obj)

