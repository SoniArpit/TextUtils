# I have created this file - Arpit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('''Home <a href="/removepunc">remove punc</a>
    #                             <a href="/capitalizefirst">capitalizefirst</a>
    #                             <a href="/newlineremove">newlineremove</a>
    #                             <a href="/spaceremove">spaceremove</a>
    #                             <a href="/charcounter">charcounter</a>''')

    params = {'name':'harry', 'place':'Mars'}
    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations  = '''[]!"#$%&'()*+,./:;<=>?@\^`|{}~-'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose':'remove punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if charactercounter == "on":
        analyzed=""
        params = {'purpose': 'Character Counter', 'analyzed_text': f"{djtext} \n"
        f"\nLength:{len(djtext)}"}

    if removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and newlineremover!="on"and fullcaps!="on" and charactercounter!="on":
        return HttpResponse("Error!!")
    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')


# def capfirst(request):
#     return HttpResponse("capitalize first"+'''<br><a href="/">Back to Home</a>''')
#
# def newlineremove(request):
#     return HttpResponse("new line remove"+'''<br><a href="/">Back to Home</a>''')
#
# def spaceremove(request):
#     return HttpResponse("space remove"+'''<br><a href="/">Back to Home</a>''')
#
# def charcounter(request):
#     return HttpResponse("character counter"+'''<br><a href="/">Back to Home</a>''')


# def file(request):
#     with open('index.html') as f:
#         file=f.read()
#     return HttpResponse(file)

# def index(request):
#     return HttpResponse(''' <a href="https://www.codesnail.com" target="_blank">CodeSnail</a>
#                             <a href="https://codewithharry.com" target="_blank"> CodeWithHarry</a>
#                             <a href="https://instagram.com/code_snail" target="_blank"> code_snail</a>
#                             <a href="https://amazon.com" target="_blank"> Amazon</a>
#                             <a href="https://example.com" target="_blank"> Example.com</a>''')
