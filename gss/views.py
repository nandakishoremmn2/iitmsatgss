from django.shortcuts import render

def telecommands(request, *args, **kwargs):
    # if not content_creator_check(request.user):
    #     print "redirecting"
    #     return redirect(reverse('keam_home'))

    telecommands_page = True
    return render(request, 'gss/edit.html', locals())