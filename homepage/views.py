from django.shortcuts import render

def homepage(request):
    return render(request,'homepage/home.html',{'title': 'ROMBICK', 'active': 'homepage'})
def contacts(request):
    return render(request,'homepage/contacts.html',{'title': 'Contacts', 'active': 'contacts'})
