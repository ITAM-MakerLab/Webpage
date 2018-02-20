from django.shortcuts import render, get_object_or_404
from .models import Tutorial, FeaturedTutorial


def tutorialesIndex(request):
    recent_tuts = Tutorial.objects.order_by("tutDateTime").reverse()
    feauted_tuts = FeaturedTutorial.objects.all()
    tut_context = {"tut_list": recent_tuts, "features": feauted_tuts}
    return render(request, "tutoriales/tutorialIndex.html", tut_context)


def tutorialesDetail(request, blogEntry_id):
    selected_entry = get_object_or_404(Tutorial, pk=blogEntry_id)
    tut_centex = {"selected_tutorial": selected_entry}
    return render(request, "tutoriales/tutorialDetails.html", tut_centex)