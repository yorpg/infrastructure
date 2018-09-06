from pynamodb.models import Model
from pynamodb import attributes


class User(Model):
    """
    A DynamoDB User
    """

    class Meta:
        table_name = "Users"
        host = "http://172.17.0.2:8000"

    id = attributes.UnicodeAttribute(hash_key=True)
    email = attributes.UnicodeAttribute()
    first_name = attributes.UnicodeAttribute(null=True)
    last_name = attributes.UnicodeAttribute(null=True)
