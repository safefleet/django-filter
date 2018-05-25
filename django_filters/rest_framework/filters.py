from rest_framework import fields

from .. import filters


class CharFilter(filters.CharFilter):
    field_class = fields.CharField


class BooleanFilter(filters.BooleanFilter):
    field_class = fields.BooleanField


class NumberFilter(filters.NumberFilter):
    field_class = fields.FloatField


class ListFilter(filters.MultipleChoiceFilter):
    field_class = fields.ListField


class ChoiceFilter(filters.ChoiceFilter):
    field_class = fields.ChoiceField


class UUIDFilter(filters.UUIDFilter):
    field_class = fields.UUIDField


class MultipleChoiceFilter(filters.MultipleChoiceFilter):
    field_class = fields.MultipleChoiceField


class DateFilter(filters.DateFilter):
    field_class = fields.DateField


class DateTimeFilter(filters.DateTimeFilter):
    field_class = fields.DateTimeField


class TimeFilter(filters.TimeFilter):
    field_class = fields.TimeField


class DurationFilter(filters.DurationFilter):
    field_class = fields.DurationField
