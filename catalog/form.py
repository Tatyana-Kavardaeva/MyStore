from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Ошибка, связанная с именем продукта')
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('В описание продукта добавлены недопустимые слова')
            return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'description', 'is_published')


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
