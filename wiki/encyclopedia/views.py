from django.shortcuts import render
from django.http import HttpResponse
from markdown import markdown
from . import util

class Md_to_HTML:

    def __init__(self,mdfile):
        self.mdfile = mdfile
    def md_to_html(self):
        md = open(self.mdfile,'r')
        mdread = md.read()
        html = markdown(mdread)
        md.close()
        return(html)
        
    
         

def index(request):
       return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
       })
    
def CSS(request):
     ht = Md_to_HTML(mdfile = 'entries/CSS.md')
     return HttpResponse(ht.md_to_html())
   
def entries(request,url):
    if  url  not in util.list_entries():
         return render(request,"encyclopedia/error.html")
    else:    
        ht = Md_to_HTML(mdfile = 'entries/'+url+".md")
        return HttpResponse(ht.md_to_html())
    

