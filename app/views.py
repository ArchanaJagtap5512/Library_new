from django.shortcuts import render , HttpResponse , redirect
from.models import Book 
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import BookForm

# Create your views here.

from .models import Book            # . complete file access 

@login_required
def home(request):
    print(request.method)          # GET
    if request.method == "POST":

        data = request.POST
        bid = data.get("Book_id")
        name = data.get("Book_name")
        qty = data .get("Book_qty")
        price = data.get("Book_price")
        author = data.get("Book_author")
        is_pub = data.get("Book_is_pub")


        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False


        if not bid:
            Book.objects.create(name=name, qty=qty, price=price, author=author)
        else:
            book_obj = Book.objects.get(id=bid)  
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_pub
            book_obj.save()
        # print(Book)
        return render(request, "home.html")
    # return HttpResponse("Success")
    return render(request, "home.html")

@login_required
def show_book(request):
    return render(request, "show_book.html", {"books": Book.objects.filter(is_active=True)})



def update_book(request, pk):   # pk or id 
    book_obj = Book.objects.get(id=pk)
    print(book_obj)
    return render(request, "home.html", {"single_book": book_obj})


def delete_book(request, pk):
    book_obj = Book.objects.get(id=pk).delete()
    return render(request, "home.html", context={"single_book": book_obj})


def soft_delete_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = False
    book_obj.save()
    return redirect("all_inactive_books")


def show_inactive_books(request):  # sare books pass karene hai to koi parameter pass nahi karaana
    return render(request, "show_book.html", {"books": Book.objects.filter(is_active=False), "inactive" : True}) 


def restore_book(request, pk):     
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = True
    book_obj.save()
    return redirect("show_book")


def book_form(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("book_login")
    form = BookForm()
    return render (request=request , template_name="book_form.html", context={"register_form": form})


def book_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect("home_page")
            else:
                return redirect("book_login")
        else:
            return redirect("book_login")
    form = AuthenticationForm()
    return render(request=request , template_name="book_login.html", context={"login_form": form})


def book_logout(request):
    logout(request)
    return redirect("book_login")



#----------------------------------------------------------------------------------------------

# # Username (leave blank to use 'dell'): Archana
# # Email address: a@gmail.com
# # Password: 
# # Password (again): python@123
# # Superuser created successfully.

