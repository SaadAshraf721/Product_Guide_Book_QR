from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
#
#
# class CustomUserAdmin(UserAdmin):
#     def get_queryset(self, request):
#         qs = self.model._default_manager.get_queryset()
#         if request.user.is_superuser:
#             return qs
#         else:
#             return qs.filter(pk=request.user.id)
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password','CompanyName','Address','BillingDetails','PhoneNumber','wesite_url')}),
#         ('Permissions', {'fields': ()}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','CompanyName')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# from django import forms
# from cryptohash import sha1
# from django.utils.html import format_html
# class CustomBarModelForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name','sr_number')
# class langform(forms.ModelForm):
#     class Meta:
#         model = language
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(langform, self).__init__(*args, **kwargs)
#         if self.request.user.is_superuser:
#             self.fields['product'].queryset = Product.objects.all()
#         else:
#             self.fields['product'].queryset = Product.objects.filter(usr=self.request.user)
#
# import random
#
#
# class Aproduct(admin.ModelAdmin):
#
#
#     form = CustomBarModelForm
#
#
#     def get_queryset(self, request):
#         qs = self.model._default_manager.get_queryset()
#         if request.user.is_superuser:
#             return qs
#         else:
#             return qs.filter(usr=request.user)
#
#     def save_model(self, request, instance, form, change):
#             unumber=random.randint(100000,1000000)
#             instance.usr=request.user
#             cod=str(unumber)+request.user.email+instance.name
#             cod2=str(sha1(cod))
#             instance.Qr_code.name=cod2+".png"
#             img = qrcode.make(request.user.wesite_url+cod2)
#             img.save("media/"+cod2+".png")
#
#             super(Aproduct, self).save_model(request, instance, form, change)
#     list_display = ['name', 'sr_number', 'usr', 'Qr_code']
#     change_list_template = 'cl.html'
#
#
# class Alanguage(admin.ModelAdmin):
#     form = langform
#
#     def get_form(self, request, obj=None, **kwargs):
#         form = super(Alanguage, self).get_form(request, obj=obj, **kwargs)
#         form.request = request
#         return form
#
#     def get_queryset(self, request):
#         qs = self.model._default_manager.get_queryset()
#         if request.user.is_superuser:
#             return qs
#         else:
#             return qs.filter(product__usr=request.user)
#     list_display = ['product', 'language_name', 'title', 'subtitle','txt','image','video']
#
# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Product,Aproduct)
# admin.site.register(language,Alanguage)
admin.site.register(Plan)
