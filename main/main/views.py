from django.http import HttpResponse

from main.constants import WELCOME, COPYRIGHT

content = f'''
{WELCOME}
........................................

Available API requests:

/ (root)

........................................
{COPYRIGHT}
'''


def root(req):
    return HttpResponse(content, content_type="text/plain")
