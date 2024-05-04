from django import forms
from medical_services.models import Service, Category


class CategoryForm(forms.ModelForm):
    """ Формы для взаимодействия с моделями категорий """
    class Meta:
        model = Category
        fields = ("category_title", "category_description", "category_image",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ServicesForm(forms.ModelForm):
    """ Формы для взаимодействия с моделями услуг """
    class Meta:
        model = Service
        fields = ("services_title", "services_description", "category", "price", "deadline",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
