#
# Copyright © Michal Čihař <michal@weblate.org>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from django.template import Library
from django.utils.formats import number_format
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext

register = Library()


@register.filter
def price_format(value, currency="€"):
    if currency == "EUR":
        currency = "€"
    price = number_format(value, force_grouping=True)
    if len(currency) > 1:
        # Translators: currency is a currency code here, for example CZK
        return pgettext("Price display", "%(currency)s %(price)s") % {
            "currency": currency,
            "price": price,
        }
    # Translators: currency is a currency symbol here, for example €
    return pgettext("Price display", "%(currency)s%(price)s") % {
        "currency": currency,
        "price": price,
    }


@register.filter
def make_strong(value):
    return mark_safe(f"<strong>{value}</strong>")
