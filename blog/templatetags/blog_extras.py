from django.contrib.auth.models import User
from django.template import Library
from django.utils.html import format_html

from blog.models import *

register = Library()

@register.filter
def author_details(author: User, current_user=None):
  if not isinstance(author, User):
    return ''

  if author == current_user:
    return format_html('<strong>me</strong>')

  name = f"{author.first_name} {author.last_name}" if author.first_name and author.last_name else author.username

  return format_html('<a href="mailto:{}">{}</a>', author.email, name) if author.email else name

@register.simple_tag
def row(extra_classes=''):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return format_html('</div>')

@register.simple_tag
def col(extra_classes=''):
  return format_html('<div class="col {}">', extra_classes)

@register.simple_tag
def endcol():
  return format_html('</div>')

@register.inclusion_tag('blog/post-list.html')
def recent_posts(post: Post):
  return {'title': 'Recent Posts', 'posts': Post.objects.exclude(pk=post.pk)[: 5]}