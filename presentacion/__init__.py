"""Presentacion package initializer.

Avoid importing submodules at package import time to prevent pulling
heavy third-party dependencies (e.g. prettytable) when a single
submodule is requested.
"""

__all__ = [
	"solicitud_datos",
	"control_libro",
	"control_usuario",
	"menu_principal",
]

def __getattr__(name):
	if name in __all__:
		import importlib
		module = importlib.import_module(f"{__name__}.{name}")
		# If the module exposes a callable with the same name, return it (convenience)
		if hasattr(module, name):
			attr = getattr(module, name)
			globals()[name] = attr
			return attr
		globals()[name] = module
		return module
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
