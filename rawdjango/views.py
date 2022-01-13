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


def typography(request):
    context = {
        'title': "Typography",
        'active_features': 'active',
        'active_typography': 'active'

    }
    return render(request, 'rawdjango/typography.html', context=context)


def components(request):
    context = {
        'title': "Components",
        'active_features': 'active',
        'active_components': 'active'

    }
    return render(request, 'rawdjango/components.html', context=context)


def icons(request):
    context = {
        'title': "Icons",
        'active_features': 'active',
        'active_icons': 'active'

    }
    return render(request, 'rawdjango/icons.html', context=context)


def icons2(request):
    context = {
        'title': "Icons",
        'active_features': 'active',
        'active_icons2': 'active'

    }
    return render(request, 'rawdjango/icon-variations.html', context=context)


def about(request):
    context = {
        'title': "About",
        'active_pages': 'active',
        'active_about': 'active'

    }
    return render(request, 'rawdjango/about.html', context=context)


def faq(request):
    context = {
        'title': "FAQ",
        'active_pages': 'active',
        'active_faq': 'active'

    }
    return render(request, 'rawdjango/faq.html', context=context)


def team(request):
    context = {
        'title': "Team",
        'active_pages': 'active',
        'active_team': 'active'

    }
    return render(request, 'rawdjango/team.html', context=context)


def services(request):
    context = {
        'title': "Services",
        'active_pages': 'active',
        'active_services': 'active'

    }
    return render(request, 'rawdjango/services.html', context=context)


def pricingbox(request):
    context = {
        'title': "Pricingbox",
        'active_pages': 'active',
        'active_pricingbox': 'active'

    }
    return render(request, 'rawdjango/pricingbox.html', context=context)


def page404(request):
    context = {
        'title': "404",
        'active_pages': 'active',
        'active_404': 'active'

    }
    return render(request, 'rawdjango/404.html', context=context)
