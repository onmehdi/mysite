from django.contrib import admin

# Register your models here.
from website.models import Person, Contact, Newsletter


admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Newsletter)