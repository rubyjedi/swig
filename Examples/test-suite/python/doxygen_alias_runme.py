#!/usr/bin/python

import doxygen_alias
import inspect
import commentVerifier

commentVerifier.check(inspect.getdoc(doxygen_alias.make_something),
    """\
A function returning something.

:rtype: :py:class:`Something`
:return: A new object which may be None.""")
