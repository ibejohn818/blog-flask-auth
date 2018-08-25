from flask import abort, session
from functools import wraps

class authorize(object):
    """Authorize decorator for flask routes.

    Args:
        group (list[str]): List of groups to authorize
    """
    def __init__(self, groups=[]):
        self.groups = groups

    def check_groups(self):
        """Check the flask session to
        ensure user dict has a group list
        and that it contains a matching
        group

        Returns:
            void on success and abort 403 on fail
        """
        if len(self.groups) <=0:
            return
        # check if admin
        try:
            user_groups = session.get('user').get('groups')
        except Exception as e:
            abort(403)
        authed = False
        for g in self.groups:
            if g in user_groups:
                authed = True
        if not authed:
            abort(403)
        return

    def check_login(self):
        """Check the flask session for
        the presence of 'user' dict
        indicating user is logged in

        Returns:
            void on success and abort 401 on failure
        """
        if not session.get('user'):
            abort(401)
        return

    def __call__(self, f):
        @wraps(f)
        def dec(*args, **kwargs):
            self.check_login()
            self.check_groups()
            return f(*args, **kwargs)
        return dec
