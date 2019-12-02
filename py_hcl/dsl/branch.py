import py_hcl.core.stmt_factory.branch as cb


class when(object):
    def __init__(self, cond_expr):
        cb.do_when_init(cond_expr)

    def __enter__(self):
        cb.do_when_enter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        cb.do_when_exit()


class else_when(object):
    def __init__(self, cond_expr):
        cb.do_else_when_init(cond_expr)

    def __enter__(self):
        cb.do_else_when_enter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        cb.do_else_when_exit()


class otherwise(object):
    def __init__(self):
        cb.do_otherwise_init()

    def __enter__(self):
        cb.do_otherwise_enter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        cb.do_otherwise_exit()