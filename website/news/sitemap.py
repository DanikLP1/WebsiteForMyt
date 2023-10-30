from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse

from . import models

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return models.Post.objects.all()
    
    def lastmod(self, obj):
        return obj.created_on
    
class DocumentSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return models.Documents.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at
    
class ActivitiesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return models.Activities.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at
    
class Anti_corruptionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return models.Anti_corrupsion.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at

class StaticSitemap(Sitemap):
    def items(self):
        return ['about', 'all_posts', 'feedback_form', 'documents', 'main_documents', 'docs_reg', 'news', 'tasks', 'managment', 'information',
                'ifs', 'structure', 'synopsis', 'procuroment', 'stuffing', 'anti-corruption', 'expertise', 'materials', 'activities', 
                'reports', 'control', 'analytical', 'college', 'info', 'statements', 'events', 'solutions', 'plans',
                'publications', 'audit', 'communication',]
    
    def location(self, item):
        return reverse(item)