from django.shortcuts import render, redirect

from online_library.main.forms import CreateProfileForm, CreateBookForm
from online_library.main.models import Profile, Book


def show_home(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create profile')

    books = Book.objects.all()
    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'home-with-profile.html', context)


def add_book_page(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
    }

    return render(request, 'add-book.html', context)


def edit_book_page(request, pk):
    return render(request, 'edit-book.html')


def details_book_page(request, pk):
    return render(request, 'book-details.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def profile_page(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile_page(request):
    return render(request, 'edit-profile.html')


def delete_profile_page(request):
    return render(request, 'delete-profile.html')


