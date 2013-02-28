# Copyright 2012 VPAC
#
# This file is part of django-tldap.
#
# django-tldap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-tldap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-tldap  If not, see <http://www.gnu.org/licenses/>.

from tldap.query_utils import Q
import tldap.utils
from tldap.utils import DEFAULT_LDAP_ALIAS

import django.conf

connections = None
connection = None

# For backwards compatibility - Port any old database settings over to
# the new values.
if not hasattr(django.conf.settings, 'LDAP'):
    django.conf.settings.LDAP = {}

# ok to use django settings
if not django.conf.settings.LDAP:
    django.conf.settings.LDAP[DEFAULT_LDAP_ALIAS] = {
        'ENGINE': 'tldap.backend.transaction',
        'URI': django.conf.settings.LDAP_URL,
        'USER': django.conf.settings.LDAP_ADMIN_USER,
        'PASSWORD': django.conf.settings.LDAP_ADMIN_PASSWORD,
        'USE_TLS': False,
        'TLS_CA': None,
        'LDAP_ACCOUNT_BASE': django.conf.settings.LDAP_USER_BASE,
        'LDAP_GROUP_BASE': django.conf.settings.LDAP_GROUP_BASE,
    }
    if hasattr(django.conf.settings, 'LDAP_USE_TLS'):
        django.conf.settings.LDAP[DEFAULT_LDAP_ALIAS]["USE_TLS"] = (
            django.conf.settings.LDAP_USE_TLS)
    if django.conf.settings.LDAP[DEFAULT_LDAP_ALIAS]["USE_TLS"]:
        django.conf.settings.LDAP[DEFAULT_LDAP_ALIAS]["TLS_CA"] = (
            django.conf.settings.LDAP_TLS_CA)

if DEFAULT_LDAP_ALIAS not in django.conf.settings.LDAP:
    raise RuntimeError(
        "You must define a '%s' ldap database" % DEFAULT_LDAP_ALIAS)

connections = tldap.utils.ConnectionHandler(django.conf.settings.LDAP)


class DefaultConnectionProxy(object):
    """
    Proxy for accessing the default DatabaseWrapper object's attributes. If you
    need to access the DatabaseWrapper object itself, use
    connections[DEFAULT_LDAP_ALIAS] instead.
  """
    def __getattr__(self, item):
        return getattr(connections[DEFAULT_LDAP_ALIAS], item)

    def __setattr__(self, name, value):
        return setattr(connections[DEFAULT_LDAP_ALIAS], name, value)

connection = DefaultConnectionProxy()
