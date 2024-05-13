from django import template


register = template.Library()

cecsor = ['Брань', 'брань', 'QWERTY']
# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor_filter(value):
   for i in value.split():
       if i in cecsor:
           return  " ".join("***")
       else:
           return value

