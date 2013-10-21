#coding=utf-8

from justtranslate.forms import *
from justtranslate.models import *

from django.shortcuts import render

import re

def add_article(request, template_name='add_article.html'):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data['article']
            article_name = form.cleaned_data['article_name']
            slist = decompose_article(article)
            a = Article.objects.get(article_name=article_name)
            if not a:
                a = Ariticle(article_name=article_name)
                a.save()
            for s in slist:
                s1 = Sentence(article=a,num=s['num'],pnum=s['pnum'],sentence=s['sentence'])
                s1.save()
    else:
        form = AddArticleForm()
    return render(request, template_name, {'form': form})

def decompose_article(article):
    """
    Decompose an article into sentences

    Return sentences:
    A list of sentence
    slist: {
    int num,
    int pnum,
    int sentence}
    """
    
    paragraph = article.split("\r\n")
    pnum = 1
    num = 1
    slist = []
    for p in paragraph:
        if p:
            sentence = re.split(r"(\.|\!|\?|。|！|？)", p)
            for s in sentence:
                if len(s) > 1:
                    slist.append({'num':num,'pnum':pnum,'sentence':s})
                    num = num + 1
                else:
                    slist[-1]['sentence'] = slist[-1]['sentence'] + s
            pnum = pnum + 1
    return slist
