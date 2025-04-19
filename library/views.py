from django.shortcuts import render,redirect
from .models import Book,Category
from .forms import BookForm,CategoryForm
from django.contrib import messages


# Create your views here.

def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()

    bf = BookForm()  # default
    cf = CategoryForm()
    form_has_error = False
    
    total_sales = sum(book.price for book in Book.objects.filter(status='Sold') if book.price)
    total_rentals = sum(book.total_rental for book in Book.objects.filter(status='Rental') if book.total_rental)



    if request.method == 'POST':
        # إنشاء الفورمات من البيانات المرسلة
        bf = BookForm(request.POST, request.FILES)
        cf = CategoryForm(request.POST)

        # التحقق من صحة فورم الكتاب
        if bf.is_valid():
            book = bf.save(commit=False)  # عدم حفظ الكتاب فوراً
            book.save()  # حفظ الكتاب في قاعدة البيانات
            messages.success(request, "تم إضافة الكتاب بنجاح!")  # عرض رسالة نجاح
            return redirect('books')  # إعادة التوجيه إلى صفحة النجاح

        else:
            form_has_error = True  # ⬅️ إذا كان هناك خطأ في الفورم

        # التحقق من صحة فورم الفئة
        if cf.is_valid():
            cf.save()  # حفظ الفئة

    else:
        # في حالة أن الطلب ليس من نوع POST، نعيد تهيئة الفورمات
        bf = BookForm()
        cf = CategoryForm()
    context = {
        'books': books,
        'categories': categories,
        'bf': bf,  # ✅ لازم نرجّع نفس الفورم عشان يعرض الأخطاء
        'cf': cf,
        'allbooks': Book.objects.filter(active=True).count(),
        'soldbooks': Book.objects.filter(status='Sold').count(),
        'rentalbooks': Book.objects.filter(status='Rental').count(),
        'availablebooks': Book.objects.filter(status='Available').count(),
        'form_has_error': form_has_error,
        'total_sales': total_sales,
        'total_rentals': total_rentals,
        'total_profit': total_sales + total_rentals,

    }

    return render(request, 'pages/index.html', context)



def books(request):
    title = None
    books = Book.objects.all()
    categories = Category.objects.all()
    search_message = ""

    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            books = books.filter(title__icontains=title)
            if not books.exists():
                search_message = "لا يوجد كتب بهذا العنوان."

    
    
    
    
    if request.method == 'POST':
       
         
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            
    context = {
        'books':books,
        'categories':categories,
        'cf':CategoryForm,
        'search_message': search_message,
        
        }
    
    return render(request,'pages/books.html',context)


def update(request, id):
    book_id = Book.objects.get(id=id)

    if request.method == 'POST':
        bf = BookForm(request.POST, request.FILES, instance=book_id)
        if bf.is_valid():
            book = bf.save(commit=False)  # ⬅️ نحجز الكائن
            book.save()                  # ⬅️ نشغّل save() بتاعة الموديل
            return redirect('index')
    else:
        bf = BookForm(instance=book_id)

    contxt = {
        'bf': bf
    }

    return render(request, 'pages/update.html', context=contxt)


def delete(request,id):
    book_delete = Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('index')
    return render(request,'pages/delete.html')





from django.http import JsonResponse
from .models import Book

def earnings_api(request):
    total_sales = sum(book.price for book in Book.objects.filter(status='Sold') if book.price)
    total_rentals = sum(book.total_rental for book in Book.objects.filter(status='Rental') if book.total_rental)
    return JsonResponse({
        'sales': float(total_sales),
        'rentals': float(total_rentals),
        'total': float(total_sales + total_rentals)
    })
