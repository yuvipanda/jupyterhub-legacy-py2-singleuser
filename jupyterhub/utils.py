"""Miscellaneous utilities"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
def url_path_join(*pieces):
    """Join components of url into a relative url

    Use to prevent double slash when joining subpath. This will leave the
    initial and final / in place

    Copied from notebook.utils.url_path_join
    """
    initial = pieces[0].startswith('/')
    final = pieces[-1].endswith('/')
    stripped = [ s.strip('/') for s in pieces ]
    result = '/'.join(s for s in stripped if s)

    if initial:
        result = '/' + result
    if final:
        result = result + '/'
    if result == '//':
        result = '/'

    return result

