from rest_framework import fields

from .. import filters as base_filters


class CharFilter(base_filters.CharFilter):
    field_class = fields.CharField


class BooleanFilter(base_filters.BooleanFilter):
    field_class = fields.BooleanField


class NumberFilter(base_filters.NumberFilter):
    field_class = fields.FloatField


class ListFilter(base_filters.MultipleChoiceFilter):
    field_class = fields.ListField


class ChoiceFilter(base_filters.ChoiceFilter):
    field_class = fields.ChoiceField


class UUIDFilter(base_filters.UUIDFilter):
    field_class = fields.UUIDField


class MultipleChoiceFilter(base_filters.MultipleChoiceFilter):
    field_class = fields.MultipleChoiceField


class DateFilter(base_filters.DateFilter):
    field_class = fields.DateField


class DateTimeFilter(base_filters.DateTimeFilter):
    field_class = fields.DateTimeField


class TimeFilter(base_filters.TimeFilter):
    field_class = fields.TimeField


class DurationFilter(base_filters.DurationFilter):
    field_class = fields.DurationField
