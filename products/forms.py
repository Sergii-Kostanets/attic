from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review
from decimal import Decimal


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['size_category', 'overall_rating']

    rating = forms.DecimalField(
        label='Rating',
        min_value=Decimal('1.00'),
        max_value=Decimal('5.00'),
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        ('1', '★☆☆☆☆'),
        ('2', '★★☆☆☆'),
        ('3', '★★★☆☆'),
        ('4', '★★★★☆'),
        ('5', '★★★★★'),
    ]

    rating = forms.ChoiceField(
        label=False,
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
    )

    content = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Write your review here...',
                   'maxlength': '200'}),
    )

    class Meta:
        model = Review
        fields = ['content', 'rating']
