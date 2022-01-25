from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(villa)
admin.site.register(readMore)
admin.site.register(imageGallery)
admin.site.register(privacyPolicy)
admin.site.register(testimonial)