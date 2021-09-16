from importlib import import_module
from pkgutil import walk_packages


def walk_modules(mod_path: str = "app.handler") -> None:
    """
    递归导入 modules

    Args:
        mod_path: str -- 绝对路径/相对路径 eg app.handler
    """
    mod = import_module(mod_path)
    path: list = getattr(mod, "__path__", [])

    for _, modname, ispkg in walk_packages(path=path, prefix=f"{mod.__name__}."):
        if not ispkg:
            import_module(modname)
