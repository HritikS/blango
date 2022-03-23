from django.contrib.auth.models import User
from django.template import Library
from django.utils.html import format_html

register = Library()

@register.filter
def author_details(author: User, current_user=None):
  if not isinstance(author, User):
    return ''

  if author == current_user:
    return format_html('<strong>me</strong>')

  name = f"{author.first_name} {author.last_name}" if author.first_name and author.last_name else author.username

  return format_html('<a href="mailto:{}">{}</a>', author.email, name) if author.email else name