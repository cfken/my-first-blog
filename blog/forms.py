# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 08:22:52 2016

@author: albrightke
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)