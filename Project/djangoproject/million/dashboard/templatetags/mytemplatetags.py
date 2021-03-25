from django import template
register = template.Library()

# @register.simple_tag(takes_context=True)
# def param_replace(context, **kwargs):
#     d = context['request'].GET.copy()
#     for k, v in kwargs.items():
#         d[k] = v
#     for k in [k for k, v in d.items() if not v]:
#         del d[k]
#     return d.urlencode()



@register.simple_tag 
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name,value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_quarystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
        encoded_querystring = '&'.join(filtered_quarystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url