from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def index(request):
    team = "动态规划"
    fp = open("/opt/noob/noobs/sunird/templates/index.html")
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({"team_name" : team}))
    return HttpResponse(html)
