from pyspare import deco_vector

from way.fs import get_files

SRC = '/home/hazen/pyramid/foba/tests/asset'

print(SRC, ':', deco_vector(get_files(SRC, predicate=lambda f: not f.startswith('_'), extension='.py')))
