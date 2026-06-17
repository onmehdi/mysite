from django import template
from blog.models import Post,Category
from django.db.models import Count


register = template.Library()

@register.simple_tag(name='totalposts')
def func1():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name='posts')
def func1():
    posts = Post.objects.filter(status = 1)
    return posts

@register.filter
def snippet(value,args=100):
    return value[:args] + '. . .'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status = 1).order_by('-published_date')[:2]
    return {'posts':posts}

@register.inclusion_tag('blog/latest-post.html')
def latest_post(args = 4):
    Posts = Post.objects.filter(status = 1).order_by('published_date')[:args]
    return {'posts':Posts}


@register.inclusion_tag('blog/latest-post-categories.html')
def latest_post_categories():
    cat_dict = dict(
    Post.objects.filter(category__isnull=False,status=1)
    .values_list('category__name')
    .annotate(post_count=Count('id'))
    )
    # Posts = Post.objects.filter(status = 1)
    # Cats = Category.objects.all()
    # cat_dict = {}
    # for name in Cats:
    #     cat_dict[name] = Posts.filter(category=name).count
    return {'categories':cat_dict}
    

@register.inclusion_tag('blog/categories.html')
def categories():
    cat_dict = dict(
        Category.objects.values_list('id','name')
    )
    return {'categories':cat_dict}
