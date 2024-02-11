from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'category', 'trailer_link', 'averageRating', 'image']

        labels = {
            'title': 'Title',
            'description': 'Description',
            'release_date': 'Release Date',
            'category': 'Category',
            'trailer_link': 'Trailer Link',
            'averageRating': 'Average Rating',
            'image': 'Image',
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

        labels = {
            'comment': 'Comment',
            'rating': 'Rating',
        }

        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 0.5}),
        }
