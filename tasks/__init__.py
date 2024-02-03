
# -- This file is mandatory for a folder module
# it is the entry point for the module.

# -- It just imports the module functions inside its own
# namespace, which is the module namespace.

# -- import using module.file (otherwise it won't work!)
from tasks.get_task import get_task
from tasks.set_task import set_task
