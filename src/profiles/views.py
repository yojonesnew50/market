from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, RequestContext, Http404, HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import slugify
from django.forms.models import modelformset_factory

from .models import UserPurchase


@login_required
def library(request):
    try:
        products = request.user.userpurchase.products.all()
    except:
        products = None
    return render(request, "profiles/library.html", {"products": products })
