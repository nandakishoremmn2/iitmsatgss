from django.shortcuts import render

def home(request, *args, **kwargs):
    # if not content_creator_check(request.user):
    #     print "redirecting"
    #     return redirect(reverse('keam_home'))

    return render(request, 'gss/login.html', locals())