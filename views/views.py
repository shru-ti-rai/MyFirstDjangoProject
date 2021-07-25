from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def ex1(request):
    sites = ['''<h1>For entertainment</h1> <a href="https://www.facebook.com/">Click</a>''']
    return HttpResponse((sites))

def analyze(request):
    #GET THE TEXT
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    print(removepunc)
    print(djtext)

    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)


    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)

    elif(spaceremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Remove space', 'analyzed_text': analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)

    elif(charcounter=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = djtext.count(djtext)
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)




    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("Remove New Line")
#
# def spaceremove(request):
#     return HttpResponse("<a href='removepunc'><button>Click</button></a>")
#
# def charcount(request):
#     return HttpResponse("Remove Char Count")


