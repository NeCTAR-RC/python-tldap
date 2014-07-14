# Copyright 2012-2014 Brian May
#
# This file is part of python-tldap.
#
# python-tldap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-tldap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-tldap  If not, see <http://www.gnu.org/licenses/>.

from tldap.ldap_passwd import check_password
from tldap.ldap_passwd import encode_password
from tldap.ldap_passwd import UserPassword

import warnings
warnings.warn(
    "tldap.methods.ldap_passwd class depreciated; do not use",
    DeprecationWarning)

check_password
encode_password
UserPassword
