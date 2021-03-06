# Copyright 2012-2014 VPAC
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

""" Methods specific for Directory Server 389. """


class passwordObjectMixin(object):
    @classmethod
    def is_locked(cls, self):
        return self.accountUnlockTime is not None

    @classmethod
    def lock(cls, self):
        self.accountUnlockTime = '19700101000000Z'

    @classmethod
    def unlock(cls, self):
        self.accountUnlockTime = None
