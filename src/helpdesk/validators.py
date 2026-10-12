# validators.py
#
# validators for file uploads, etc.

from django.utils.translation import gettext as _

from helpdesk import settings as helpdesk_settings

# TODO: can we use the builtin Django validator instead?
# see:
# https://docs.djangoproject.com/en/4.0/ref/validators/#fileextensionvalidator


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError

    if not helpdesk_settings.HELPDESK_VALIDATE_ATTACHMENT_TYPES:
        return

    name = value.name
    if name.count(".") > 1:
        raise ValidationError(_("Filename must not contain more than one '.'"))

    ext = os.path.splitext(name)[1].lower()
    if ext not in helpdesk_settings.HELPDESK_VALID_EXTENSIONS and ext not in ("", "."):
        raise ValidationError(_("Unsupported file extension: ") + ext)