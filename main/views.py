from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from main.models import Cereal, Manufacturer
from main.forms import ContactForm, CerealEditForm, ManufacturerEditForm
from django.core.mail import send_mail
from django.conf import settings


def cereal_list(request):
    context = {}

    cereals = Cereal.objects.all()

    manufacturers = Manufacturer.objects.all()

    context['manufacturers'] = manufacturers

    context['cereals'] = cereals

    return render_to_response('base.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):
    context = {}

    cereal = Cereal.objects.get(pk=pk)

    cereals = Cereal.objects.all()

    manufacturers = Manufacturer.objects.all()

    context['manufacturers'] = manufacturers

    context['cereals'] = cereals

    context['cereal'] = cereal

    return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))


def cereal_create(request):
    context = {}

    context['request'] = request.method

    context['cereal'] = Cereal.objects.all()

    if request.method == 'POST':
        name = request.Get.get('name', None)
        manufacturer = request.Get.get('manufacturer', None)
        hc = request.Get.get('Type', None)
        calories = request.Get.get('calories', None)
        protein = request.Get.get('protein', None)
        fat = request.Get.get('fat', None)
        sodium = request.Get.get('sodium', None)
        dietary_fiber = request.Get.get('dietary_fiber', None)
        carbs = request.Get.get('carbs', None)
        sugars = request.Get.get('sugars', None)
        potassium = request.Get.get('potassium', None)
        vits = request.Get.get('vitamins_and_minerals', None)
        weight = request.Get.get('serving_size', None)
        cups = request.Get.get('cups_per_serving', None)

        if cereal_id != None: 
            cereals = Cereal.objects.all(pk=cereal_id)
        else:
            cereal = Cereal.objects.all(name='Frosted Flakes')

        the_cereal, created = Cereal.objects.get_or_create(name=name)

        the_cereal.manufacturer = manufacturer
        the_cereal.hc = hc
        the_cereal.calories = calories
        the_cereal.protein = protein
        the_cereal.fat = fat
        the_cereal.sodium = sodium
        the_cereal.dietary_fiber = dietary_fiber
        the_cereal.carbs = carbs
        the_cereal.sugars = sugars
        the_cereal.potassium = potassium
        the_cereal.vits = vits
        the_cereal.weight = weight
        the_cereal.cups = cups

        the_cereal.save()

        context['created'] = created

    elif request.method == 'GET':
        print "it was a GET request"

    return render_to_response('cereal_create.html', context, context_instance=RequestContext(request))


def cereal_edit(request, pk):
    context = {}

    cereal = Cereal.objects.get(pk=pk)

    form = CerealEditForm(request.POST or None, instance=cereal)

    context['cereal'] = cereal
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/cereal_list/')

    return render_to_response('cereal_edit.html', context, context_instance=RequestContext(request))


def manufacturer_create(request):
    context = {}

    context['request'] = request.method

    context['manufacturers'] = Manufacturer.objects.all()

    if request.method == 'POST':
        name = request.Get.get('name', None)

        if manufacturer_id != None:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        else:
            manufacturer = Manufacturer.objects.get(name='Nabisco')

        the_manufacturer, created = Manufacturer.objects.get_or_create(name=name)

        the_manufacturer.name = name

        the_manufacturer.save()

        context['created'] = created

    elif request.method == "GET":
            print "it was a GET request"

    return render_to_response('manufacturer_create.html', context, context_instance=RequestContext(request))


def manufacturer_edit(request, pk):

    context = {}

    manufacturer = Manufacturer.objects.get(pk=pk)

    form = ManufacturerEditForm(request.POST or None, instance=manufacturer)

    context['manufacturer'] = manufacturer
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/manufacturer_list/')

    return render_to_response('manufacturer_edit.html', context, context_instance=RequestContext(request))


def contact_view(request):

    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('MANUFACTURERS SIT MESSAGE FROM %s' % name,
                        message,
                        email,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False
                        )
            context['message'] = "email sent"
        else:
            context['message'] = form.errors 

    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))


def manufacturer_detail(request, pk):
    context = {}

    manufacturer = Manufacturer.objects.get(pk=pk)
    # print manufacturer
    # print manufacturer.cereal_set
    # for cereal in manufacturer.cereal_set.all():
    #     print cereal
    # cereals = Cereal.objects.all()

    # manufacturers = Manufacturer.objects.all()

    context['manufacturer'] = manufacturer

    # context['cereals'] = cereals

    # context['cereal'] = cereal

    return render_to_response('manufacturer_detail.html', context, context_instance=RequestContext(request))













    # #context = {}

    # manufacturers = Manufacturer.objects.all()
    
    # for manufacturer in manufacturers:
    #     cereals = Manufacturer.cereal_set.filter(name__startswith="D")
    #     for cereal in cereals:
    #         text_string += "Manufacturer:  %s, Cereal: %s <br>" (manufacturer, cereal.name)

    # return HttpResponse(cereal_list)#, context, context_instance=RequestContext(request))


    # # context = ['cereals'] = cereals

    # return HttpResponse(text_string)#('cereal_list.html', context, context_instance=RequestContext(request))