from django.contrib import admin
from justtranslate.models import *

class ArticleAdmin(admin.ModelAdmin):
    pass
    
class SentenceAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Sentence, SentenceAdmin)