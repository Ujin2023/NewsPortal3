from django import forms
from .models import Post

class PostFormCreateNews(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author',
                  'post_head',
                  'post_text',
                  ]



