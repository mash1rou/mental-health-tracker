from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nim' : '23/516252/PA/22075',
        'name': 'Raditya Maheswara',
        'class': 'CSA'
    }

    return render(request, "main.html", context)

