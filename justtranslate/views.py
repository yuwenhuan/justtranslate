#coding=utf-8

from justtranslate.forms import *

from django.shortcuts import render

import re

def add_article(request, template_name='add_article.html'):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data['article']
            decompose_article(article)
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
    for s in slist:
        print s['sentence'] + "***" + "\n"
