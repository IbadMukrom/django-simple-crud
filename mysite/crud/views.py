from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Mahasiswa
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
class Home(View):
    template_name ='home.html'
    def get(self, request):
        return render(request, self.template_name) 

class Register(View):
    template_name = 'register.html'

    def get (self, request):
        return render (request, self.template_name)

class Tambah(View):
    
    def post(self, request):
        mahasiswa = Mahasiswa()
        mahasiswa.nama = request.POST['nama']
        mahasiswa.alamat = request.POST['alamat']
        mahasiswa.nim = request.POST['nim']
        mahasiswa.save()
        return redirect('/mahasiswa/')

class Lihat(View):
    template_name = 'mahasiswa.html'

    def get(self, request):
        data = {
            'semua_mahasiswa': Mahasiswa.objects.all()
        }
        return render (request, self.template_name, data)

class Edit(View):
    template_name = 'edit-mahasiswa.html'

    def get(self, request,id):
        data={
            'mahasiswa': Mahasiswa.objects.get(id=id)
        }
        return render (request, self.template_name , data)

    def post(self,request,id):
        mahasiswa = Mahasiswa.objects.get(id=id)
        mahasiswa.nama = request.POST['nama']
        mahasiswa.alamat = request.POST['alamat']
        mahasiswa.nim = request.POST['nim']
        mahasiswa.save()
        return redirect ('/mahasiswa/')

class Hapus(View):
        template_name = 'hapus-mahasiswa.html'

        def get(self, request, id):
            return render (request, self.template_name)

        def post(self, request, id):
            mahasiswa = Mahasiswa.objects.get(id=id)
            mahasiswa.delete()
            return redirect('/mahasiswa/')