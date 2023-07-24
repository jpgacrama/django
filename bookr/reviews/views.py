from django.shortcuts import render

def index(request):
    return render(request, "base.html")

def search(request):
    search_query = request.GET.get('search', '')  # Get the search string from the URL parameters
    context = {
        'search_query': search_query,
    }
    return render(request, "search.html", context)
