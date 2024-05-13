import django_filters
from django_filters import FilterSet
from .models import Post
from django import forms


class PostFilter(FilterSet):
    date = django_filters.DateTimeFilter(field_name="post_date",
                                          lookup_expr="exact",
                                          label="Дата создания:",
                                         widget = forms.DateInput(attrs={'type':'date'})

                                     )
    class Meta:
        model = Post
        fields = ["post_head", "author"]