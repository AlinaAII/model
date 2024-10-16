from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from movie_review_service.model import load_model
import os
from django.conf import settings

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.title = form.cleaned_data['title']
            review.content = form.cleaned_data['content']
            
            # Загружаем модель
            model = load_model()
            
            # Используем модель для определения рейтинга и sentiments
            rating = predict_rating(model, review.content)
            sentiment = determine_sentiment(model, review.content)
            
            review.rating = rating
            review.sentiment = sentiment
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

from django.template.loader import render_to_string
def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    
    # Используем абсолютный путь к шаблону
    template_path = os.path.abspath(os.path.join(settings.BASE_DIR, 'templates', 'reviews', 'review_list.html'))
    
    return render(request, template_path, {'reviews': reviews})


def predict_rating(model, text):
    # Реализация предсказания рейтинга
    # Здесь нужно использовать вашу предобученную модель
    pass

def determine_sentiment(model, text):
    # Реализация определения sentiments
    # Здесь нужно использовать вашу предобученную модель
    pass

