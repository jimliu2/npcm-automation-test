import os
from robot.variables.filesetter import PythonImporter
from robot.libraries.BuiltIn import BuiltIn

def load_vars(var_path):
    builtin = BuiltIn()
    path = os.path.abspath(var_path)
    vars = PythonImporter().import_variables(path)
    _vars = {}
    print(vars)
    for name, value in vars:
        # only update var with empty one or not set
        data = builtin.get_variable_value(name)
        if not data:
            # we get name as ${name} here from importer, remove it!
            _vars[name[2:-1]] = value
            builtin.set_global_variable(name, value)
    print(_vars)
    return _vars