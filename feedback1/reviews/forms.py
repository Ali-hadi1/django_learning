from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=50, error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'Please enter a shorter name!'
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['username', 'review_text', 'rating'] to show certain fields for end users
        fields = '__all__' # to show all fields for end users
        # exclude = [''] list all fields that are excluded
        labels = {
            'review_text': 'Message'
        }
        error_messages = {
            'username': {
                'required': 'Your usernaem must not be empty',
                'max_length': 'Please enter a shorter name!'
            }
        }