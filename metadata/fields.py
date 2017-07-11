"""
Module for creating slug fields.

"""

import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class KeySlugField(models.SlugField):
    """ The slug field used by :class:'MetaDataAttributes' """

    def validate(self, value, instance):
        """
        Slugs are used to convert the Python attribute label to a database
        lookup and vice versa. We need it to be a valid Python identifier.
        We don't want it to start with a '_', underscore will be used
        for variables we don't want to be saved in db.
        """
        super(KeySlugField, self).validate(value, instance)
        slug_regex = r'[a-z][a-z0-9_]*'
        if not re.match(slug_regex, value):
            raise ValidationError(_(u'Must be all lower case, '
                                    u'start with a letter, and contain '
                                    u'only letters, numbers, or underscores.'))

    @staticmethod
    def create_slug_from_name(name):
        """
        Creates a slug based on the name
        """
        name = name.strip().lower()

        # Change spaces to underscores
        name = '_'.join(name.split())

        # Remove non alphanumeric characters
        return re.sub('[^\w]', '', name)
