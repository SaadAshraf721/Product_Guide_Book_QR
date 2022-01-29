from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import Group
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import *
from django.contrib.auth import authenticate ,login as abc,logout as deff
from qr.settings import base_url
from django.contrib.auth.decorators import login_required
def register(request):
    if request.user.is_authenticated:
        return redirect('/dash/')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()

            # user_group = Group.objects.get(name='Genral user')
            # user.groups.add(user_group)

            form.save()
            res="sucessfully Register"
            return render(request, "register.html", {"form": form,'res':res})
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

# class reg(CreateView):
#     model = CustomUser
#     form_class = RegisterForm()
#     template_name =" register.html"
#     fields = ["email", "password1", "password2", "CompanyName", "Address", "BillingDetails", "Plan", "PhoneNumber",
#               "wesite_url"]

@login_required(login_url='/login/')
def dash(request):
    usr=request.user
    pr=Product.objects.filter(usr=usr)
    # pr = Product.objects.all()

    return render(request,'main.html',{'pr':pr})

@login_required(login_url='/login/')
def langv(request):
    usr = request.user
    pr=lang.objects.filter(usr=usr)
    # pr = lang.objects.all()

    return render(request, 'lang.html', {'pr': pr})


@login_required(login_url='/login/')
def logout(request):
    deff(request)
    return redirect('/login/')
def login(request):
    if request.user.is_authenticated:
        return redirect('/dash/')

    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['password']
        user = authenticate(email=email, password=passw)
        if user is not None:
            abc(request, user)
            return redirect('/dash/')
        else:
            fr = 'User not valid'
            return render(request, 'login.html', {'fr': fr})


    return render(request, 'login.html')

from django.http import HttpResponseRedirect
import random
from cryptohash import sha1
import qrcode
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
class productcreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = productform
    model = Product
    template_name = 'add.html'



    def form_valid(self, form):
        obj = form.save(commit=False)
        unumber = random.randint(100000, 1000000)
        obj.usr = self.request.user
        cod = str(unumber) + self.request.user.email + obj.name
        cod2 = str(sha1(cod))
        obj.Qr_code.name = cod2 + ".png"
        img = qrcode.make(base_url + 'search/?q='+cod2+'.png')
        img.save("media/" + cod2 + ".png")
        obj.save()
        return HttpResponseRedirect('/dash/')


class deleteprod(LoginRequiredMixin,DeleteView):
    # specify the model you want to use
    login_url = '/login/'
    model = Product
    template_name = 'confrm.html'

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/dash/"
    def dispatch(self, request, *args, **kwargs):
        if not Product.objects.filter(pk=kwargs['pk'],usr=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
class editproduct(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    form_class = productform
    model = Product
    template_name = 'editprod.html'
    success_url = "/dash/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pr"] = language.objects.filter(product_id=self.kwargs['pk'],product__usr=self.request.user)
        context['idd']=Product.objects.get(pk=self.kwargs['pk']).id
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     self.pkk=kwargs['pk']
    #     if not Product.objects.filter(pk=kwargs['pk'],usr=request.user).exists():
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)


class langadd(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = lang_form
    model = lang
    template_name = 'add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usr = self.request.user
        obj.save()
        return HttpResponseRedirect('/lang/')


class editlang(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    form_class = lang_form
    model = lang
    template_name = 'edit.html'
    success_url = "/lang/"

    def dispatch(self, request, *args, **kwargs):
        if not lang.objects.filter(pk=kwargs['pk'],usr=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class editlangass(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    form_class = langpro_form
    model = language
    template_name = 'edit.html'
    success_url = "/dash/"
    def dispatch(self, request, *args, **kwargs):
        if not language.objects.filter(product__usr=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class deletelngass(LoginRequiredMixin,DeleteView):
    # specify the model you want to use
    login_url = '/login/'
    model = language
    template_name = 'confrm.html'

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/dash/"
    def dispatch(self, request, *args, **kwargs):
        if not language.objects.filter(pk=kwargs['pk'],product__usr=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class deletelang(LoginRequiredMixin,DeleteView):
    # specify the model you want to use
    login_url = '/login/'
    model = lang
    template_name = 'confrm.html'

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/lang/"
    def dispatch(self, request, *args, **kwargs):
        if not lang.objects.filter(pk=kwargs['pk'],usr=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




# class lang_ass(LoginRequiredMixin,CreateView):
#     login_url = '/login/'
#     form_class = langpro_form
#     model = language
#     template_name = 'addlng.html'

    # def dispatch(self, request, *args, **kwargs):
    #     self.uss=request.user
    #     if not Product.objects.filter(pk=request.GET['pr'],usr=request.user).exists():
    #         return self.handle_no_permission()
    #     pr=Product.objects.get(pk=request.GET['pr'])
    #     self.prr=request.GET['pr']
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if Product.objects.filter(id=self.prr,usr=self.uss).exists():
    #         context["Name"] = Product.objects.get(pk=self.prr).name
    #         context["idd"]=Product.objects.get(pk=self.prr).id
    #     else:
    #         return self.handle_no_permission()
    #     return context

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.usr = self.request.user
    #     obj.product_id=self.prr
    #     obj.save()
    #     return HttpResponseRedirect('/lnag/')

@login_required(login_url='/login/')
def lang_ass(request):
    if request.method == 'POST':
        lange=request.POST.get('language','')
        title = request.POST.get('title', '')
        subtitle = request.POST.get('subtitle', '')
        txt = request.POST.get('txt', '')
        image = request.FILES['image']
        video = request.POST.get('video', '')
        prd=request.POST.get('product', '')
        language.objects.create(product_id=prd,language_id=lange,title=title,subtitle=subtitle,image=image,video=video)
        return redirect("/"+prd+"/edit/")
    prd=request.GET.get("pr")
    usr = request.user
    lng=lang.objects.filter(usr=usr).exclude(id__in=language.objects.filter(product_id=prd).values_list('language', flat=True))
    return  render(request,'addlng.html',{'lng':lng,'prd':prd})

def search(request):
    cod=request.GET['q']
    prd=Product.objects.get(Qr_code=cod)
    lng=language.objects.filter(product=prd)
    return render(request,'search.html',{'lng':lng,'pr':prd.id})

def detail(request):
    rec=""
    if request.method == 'POST':
        prd=request.POST['prd']
        lng=request.POST['lng']
        rec=language.objects.filter(product=prd,language=lng).first()
    return render(request,'detail.html',{'rec':rec})