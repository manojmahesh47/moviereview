from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .models import Movie, Category

def home(request):
    query = request.GET.get("title")
    category_id = request.GET.get("category")

    allMovies = Movie.objects.all()

    if query:
        allMovies = allMovies.filter(title__icontains=query)

    if category_id:
        allMovies = allMovies.filter(category_id=category_id)

    categories = Category.objects.all()

    context = {
        "movies": allMovies,
        "categories": categories,
    }

    return render(request, 'main/index.html', context)

def detail(request,id):
    movie = Movie.objects.get(id=id)
    reviews= Review.objects.filter(movie=id).order_by("-comment")

    context ={
       "movie": movie,
        "reviews": reviews,
    }
    return render(request,'main/detail.html',context)

from django.shortcuts import render, redirect
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

def add_movies(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user  # Associate the movie with the logged-in user
            movie.save()
            return redirect("main:home")
    else:
        form = MovieForm()

    return render(request, 'main/add_movies.html', {"form": form, "controller": "Add Movies"})

def edit_movies(request, id):
    movie = None

    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()  # Save the changes to the existing movie object
            return redirect("main:details", id=id)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'main/add_movies.html', {"form": form, "controller": "Edit Movies"})

def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = form.cleaned_data['comment']
                data.rating = form.cleaned_data['rating']
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:details", id=id)
        else:
            form = ReviewForm()

        return render(request, 'main/detail.html', {"form": form})
    else:
        return redirect("accounts:login")


from .forms import ReviewForm  # Make sure to import your ReviewForm


def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        # Retrieve the movie and review objects
        movie = get_object_or_404(Movie, id=movie_id)
        review = get_object_or_404(Review, movie=movie, id=review_id)

        # Check if the logged-in user is the author of the review
        if request.user == review.user:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    form.save()
                    return redirect("main:details", id=movie_id)
            else:
                form = ReviewForm(instance=review)

            return render(request, "main/editreview.html", {"form": form, "movie": movie, "review": review})
        else:
            return redirect("accounts:login")
    else:
        return redirect("accounts:login")

def delete_movies(request, id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=id, user=request.user)
        movie.delete()
    return redirect("main:home")


from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


@login_required
def edit_movies(request, id):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the movie linked with the id
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        # Form check
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            # Check if form is valid
            if form.is_valid():
                edited_movie = form.save()  # Save the edited movie
                  # Delete the old movie
                return redirect("main:detail", id=edited_movie.id)
        else:
            form = MovieForm(instance=movie)

        return render(request, 'main/add_movies.html', {"form": form, "controller": "Edit Movies"})

    # If the user is not logged in, redirect to login page
    return redirect("accounts:login")
