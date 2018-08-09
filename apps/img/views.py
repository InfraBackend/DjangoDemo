from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import IMG


# 上传图片
@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'uploading.html')

#展示
@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'showimg.html', content)