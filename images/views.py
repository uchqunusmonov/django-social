from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actions.utils import create_action


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            create_action(request.user, 'bookmarked image', image)
            messages.success(request, 'Image uploaded successfully')
            return redirect(image.get_absolute_url())
        else:
            messages.error(request, 'Image upload failed. Please try again.')
    else:
        form = ImageCreateForm()
    return render(request, 'images/image/create.html', {'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {"section": "images", "image": image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                print("adding one like")
                image.user_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                print("removed like")
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get("page")
    images_only = request.GET.get("images_only")
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse("")
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request, 'images/image/list_images.html', {"section": "images", "images": images})
    return render(request, 'images/image/list.html', {"section": "images", "images": images})