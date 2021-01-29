from django.shortcuts import render

# Create your views here.
def atlmktdash_view(request):
    return render(request, 'atlmkt_dash/atlmktdash.html')
