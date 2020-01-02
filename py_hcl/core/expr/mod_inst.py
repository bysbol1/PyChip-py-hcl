from py_hcl.core.expr import ExprHolder
from py_hcl.core.stmt.connect import ConnSide
from py_hcl.utils import json_serialize


@json_serialize(json_fields=['operation', 'module_name'])
class ModuleInst(object):
    def __init__(self, module_cls):
        self.operation = 'module_inst'
        self.packed_module = module_cls.packed_module
        self.module_name = module_cls.packed_module.name


def con_module(module_cls):
    return ExprHolder(module_cls.io.hcl_type,
                      ConnSide.LF, ModuleInst(module_cls))