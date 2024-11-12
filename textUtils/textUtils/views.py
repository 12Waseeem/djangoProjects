from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    charcount = request.GET.get('charcount', 'off')



    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)


    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    

    elif (charcount == "on"):
        char_count = 0

# Loop through each character in the string
        for char in djtext:
    # Check if the character is a letter
          if char.isalpha():
        # If it's a letter, increase the count by 1
               char_count += 1

        params = {'purpose1': 'count Characters:', 'analyzed_text1': char_count}
        # Analyze the text
        return render(request, 'counter.html', params)

    else:
        return HttpResponse('Error')


def capfirst(request):
    return HttpResponse("Captalize First")


# def removepunc(request):
#     # get data 
#     djtext = request.GET.get('text', 'bydefault')
#     print(djtext)
#     return HttpResponse(" Remove punctations")



def newlineremove(request):
    return HttpResponse("Remove New Line")



def spaceremove(request):
    return HttpResponse("Remove Extra space")



def charcount(request):
    return HttpResponse("count characters")


