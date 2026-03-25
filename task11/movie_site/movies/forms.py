from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']  # username генерируется автоматически
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Напишите отзыв...'})
        }