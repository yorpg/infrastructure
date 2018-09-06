from pynamodb.models import Model
from pynamodb import attributes
from .aws_config_mixin import AwsMeta


class User(Model):
    """
    A DynamoDB User
    """
    Meta = AwsMeta.meta('user')

    id = attributes.UnicodeAttribute(hash_key=True)
    email = attributes.UnicodeAttribute()
    first_name = attributes.UnicodeAttribute(null=True)
    last_name = attributes.UnicodeAttribute(null=True)
