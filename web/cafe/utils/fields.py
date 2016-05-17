from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder

class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.

    example:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)


        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """

    __metaclass__ = models.SubfieldBase

    def from_db_value(self, value, expression, connection, context):
        if value == "":
            return None

        if isinstance(value, str):
            return json.loads(value)

        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None

        if isinstance(value, dict):
            value = json.dumps(value)

        return super(JSONField, self).get_db_prep_save(value, *args, **kwargs)