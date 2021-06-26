from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from miapp.models import Article
from django.db.models import Q

def index(request):
    lenguajes=['javascript','pyhton','php','c++']
    hasta=range(2021,2050)
    
    diccionario={'title':'Index','mi_variable':'dato','lenguajes':lenguajes}
    return render(request,"index.html",diccionario)

def hola_mundo(request):
    fecha=datetime.now()
    hasta=range(2021,2050)
    return render(request,"hola_mundo.html",{"fechas":fecha,"years":hasta})

def redireccionar(request):
    return redirect(index)

def pordefecto(request,parametro):
    nombre=parametro
    return render(request,'pordefecto.html',{"nombres":nombre})

def creararticulo(request,title,content,published):
    articulo=Article(
        title=title,
        content=content,
        published=published
    )
    articulo.save()
    return HttpResponse(f"<h1>El articulo {articulo.title} se ha creado</h1>")

def sacararticulo(request):
    try:
        articulo=Article.objects.get(id=9, published=False)
    except:
        articulo=Article.objects.get(title="primer articulo",id=1)
    return HttpResponse(f"{articulo.title}")

def editararticulo(request,id):
    articulo=Article.objects.get(pk=id) #pk primary key
    articulo.title='batman'
    articulo.content='contenido'
    articulo.published=False
    articulo.save()
    return HttpResponse(f"{articulo.title} fue editado")

"""def articulos(request):
    articulos=Article.objects.order_by('-id')[2:7]
    return render(request,'articulos.html',{'articulos':articulos})

def articulos(request):
    articulos=Article.objects.filter(title='tercer articulo',id=7)
    return render(request,'articulos.html',{'articulos':articulos})

def articulos(request):
    articulos=Article.objects.filter(title__contains='articulo',id__gte=12).exclude(published=True) #like de sql, __iexact no discrimina mayusculas con minusculas (lockups)
    #grater than id__gt gte=>  lte <= lt<
    return render(request,'articulos.html',{'articulos':articulos})"""

def articulos(request):
    #articulos=Article.objects.raw('SELECT* FROM miapp_article WHERE title="cuarto" ')   #consulta cruda de sql
    #consultas or, se importa la Q de Django.db.models
    ''' articulos=Article.objects.filter(
        Q(title__contains="articulo")|Q(published=True)
    )
    '''
    articulos=Article.objects.all()
    return render(request,'articulos.html',{'articulos':articulos})

def borrararticulo(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect (articulos)


def formulario(request):

    return render(request,"formulario.html")

def makearticulo(request):
    
    if request.method=="GET":
        title=request.GET['title']
        content=request.GET['content']
        published=request.GET['published']
        articulo=Article(
        title=title,
        content=content,
        published=published
        )
        articulo.save()
        return HttpResponse(f"<h1>El articulo {articulo.title} se ha creado</h1>")
    elif request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        published=request.POST['published']
        articulo=Article(
        title=title,
        content=content,
        published=published
        )
        articulo.save()
        return HttpResponse(f"<h1>El articulo {articulo.title} se ha creado</h1>")    