# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', 'kb\\', 'bc_simple_rules_questions.krb'):
           [1636624774.3513508, 'bc_simple_rules_questions_bc.py'],
         ('', 'kb\\', 'questions.kqb'):
           [1636624774.3770537, 'questions.qbc'],
        },
        compiler_version)

