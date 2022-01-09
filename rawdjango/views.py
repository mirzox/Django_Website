from django.shortcuts import render


def index(request):
    context = {
        'title': "Homepage",
        'active_home': 'active'

    }
    return render(request, 'rawdjango/index.html', context=context)


def index_alt2(request):
    context = {
        'title': "Homepage 2",
        'active_home': 'active',
        'active_homepage2': 'active'

    }
    return render(request, 'rawdjango/index-alt2.html', context=context)


def index_alt3(request):
    context = {
        'title': "Homepage 3",
        'active_home': 'active',
        'active_homepage3': 'active'

    }
    return render(request, 'rawdjango/index-alt3.html', context=context)


def index_alt4(request):
    context = {
        'title': "Homepage 4",
        'active_home': 'active',
        'active_homepage4': 'active'

    }
    return render(request, 'rawdjango/index-alt4.html', context=context)


def index_landing(request):
    context = {
        'title': "Homepage Landing",
        'active_home': 'active',
        'active_landing': 'active'

    }
    return render(request, 'rawdjango/index-landingpage.html', context=context)


def about(request):
    context = {
        'title': "About",
        'active_pages': 'active',
        'active_about': 'active'

    }
    return render(request, 'rawdjango/about.html', context=context)