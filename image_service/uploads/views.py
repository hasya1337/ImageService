from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Image
from .forms import ImageForm


def image_upload_form(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        image = form.save()
        return redirect('image_view', pk=image.pk)
    return render(request, 'uploads/upload_form.html', {'form': form})


def image_view(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'uploads/image_view.html', {'image': image})


def api_image_upload(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = Image.objects.create(image=request.FILES['image'])
        return JsonResponse({'image_url': request.build_absolute_uri(image.image.url)})
    return JsonResponse({'error': 'Invalid request'}, status=400)
