from django import template
register = template.Library()


@register.filter(name='empower')
def empower(field, css):
    """
    Add placeholder and required attributes to the field.
    Also add to the field any class specified by the template.
    """
    attrs = {
        "class": css,
        "placeholder": field.label,
    }
    if field.field.required:
        attrs["required"] = 'true'

    return field.as_widget(attrs=attrs)
