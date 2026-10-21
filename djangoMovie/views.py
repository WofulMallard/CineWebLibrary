from django.shortcuts import render, redirect
from .models import Movie
from django.db.models import Q

def movie_list_view(request):
    query = request.GET.get('q', '')
    if query:
        # Search by title, director, or genre
        movies = Movie.objects.filter(
            Q(title__icontains=query) | 
            Q(director__icontains=query) | 
            Q(genre__icontains=query)
        )
    else:
        movies = Movie.objects.all()
    
    return render(request, 'djangoMovie/movie_list.html', {'movies': movies, 'query': query})

def add_movie_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')
        
        if title and director and genre and release_year and rating:
            Movie.objects.create(
                title=title,
                director=director,
                genre=genre,
                release_year=release_year,
                rating=rating
            )
            return redirect('movie_list')
            
    return render(request, 'djangoMovie/add_movie.html')