from django.shortcuts import render
from django.http import HttpResponse
from markdown import markdown
from random import choice
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from . import util

        
entries_ = util.list_entries()
         
#this function renders home page of encyclopedia
def index(request):
      
       return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
       })
    
#this function return html page on clicking the CSS entry of encyclopedia on homepage
def css(request):
     content = markdown(util.get_entry('CSS')) 
     return render(request,'encyclopedia/show_entry.html',{
         "content":content,
         "which_page":'CSS'
         })

#this function return html page on clicking the entries of encyclopedia on homepage
def entries(request,url):
    #if the given url doesn't exist return error message
    if  url  not in util.list_entries():
         return render(request,"encyclopedia/error.html")
    else:    
        content = markdown(util.get_entry(url))
        return render(request,'encyclopedia/show_entry.html',{
         "content":content,
         "which_page":url
         })

#onclicking the create new page link this function will take user to create_new_page.html         
def newpage(request):
    return render(request,"encyclopedia/create_new_page.html")

#this is a function to add new encyclopedia entry
def newentry(request):
    title = request.GET.get('TitleOfPage','default')
    content = request.GET.get('Markdown_content','default')
    new_entry_saved = util.save_entry(title,content)
    #if the entry already exist return error message
    if new_entry_saved == "error":
        return render(request,"encyclopedia/error.html",{
            "error_message":"Sorry, requested entry already exist you can now only edit the entry",
            "entry_exist_error":True
        })
    else:
        entries_.append(title)
        content = markdown(util.get_entry(title))
        return render(request,'encyclopedia/show_entry.html',{
         "content":content
         })

#on cliking the link 'random page' on layout.html this function will take user to any random page in encyclopedia
def random_page(request):
    random_page = choice(util.list_entries())
    content = markdown(util.get_entry(random_page))
    return render(request,"encyclopedia/show_entry.html",{
        "content":content
    })

#on clicking edit page on any entry page this function will render a page where user can edit page
def edit_page(request,which_page_toedit):
    return render(request,"encyclopedia/edit_page.html",{
    "default":util.get_entry(which_page_toedit),
    "which_page_to_edit":which_page_toedit,
    "entries":util.list_entries()
    }) 

#on submitting form on edit page this will show user edited entry page
def page_edited(request):
    filename = f"entries/{request.GET.get('pagename')}.md"
    content = request.GET.get('edit','default')
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    content = markdown(util.get_entry(request.GET.get('pagename')))
    return render(request,"encyclopedia/show_entry.html",{
        "content":content,
        "which_page":request.GET.get('pagename')
    })
  

    
