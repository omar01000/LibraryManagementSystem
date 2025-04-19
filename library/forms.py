from django import forms
from .models import Book,Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['active']

    def clean(self):
        cleaned_data = super().clean()

        rental_price_day = cleaned_data.get('rental_price_day')
        rental_period = cleaned_data.get('rental_period')
        status = cleaned_data.get('status')
        price = cleaned_data.get('price')

        # ✅ الحالة = Rental → لازم السعر والمدة يكونوا موجودين
        if status == 'Rental':
            if not rental_price_day or not rental_period:
                raise forms.ValidationError("عند اختيار الحالة 'Rental'، يجب إدخال سعر الإيجار ومدة الإيجار.")

        # ❌ الحالة مش Rental → مينفعش المستخدم يدخل سعر أو مدة
        else:
            if rental_price_day or rental_period:
                raise forms.ValidationError("لا يمكن إدخال سعر أو مدة إيجار إلا إذا كانت الحالة 'Rental'.")

        if price and rental_price_day:
            raise forms.ValidationError("لا يمكن إدخال السعر وسعر الإيجار معًا. اختر أحدهما فقط.")


        return cleaned_data
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'