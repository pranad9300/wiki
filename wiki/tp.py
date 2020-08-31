from markdown import markdown
class Md_to_HTML:

    def __init__(self,mdfile):
        self.mdfile = mdfile
    def md_to_html(self):
        md = open(self.mdfile,'r')
        mdread = md.read()
        html = markdown(mdread)
        md.close()
        return(html)
u = ["CSS","Git"]
ht = Md_to_HTML(mdfile='entries/'+u[1]+'.md')
print(ht.md_to_html())