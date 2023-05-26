from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

from .models import PublishStateOption

def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishStateOption.PUBLISH
    is_draft = instance.state == PublishStateOption.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif is_draft:
        instance.publish_timestamp = None

def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)

