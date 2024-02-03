
# -- This is a basic one file module.

# -- Code written outside of function will be run ONCE
# during the first import of the module, or direct run.
print("First 'items' module import")


if __name__ == "__main__":

    # -- It is possible to run code when a module is directly
    # called from the python interpreter.
    # This code will not be run during an import.

    print("The module is directly run.")


def get_item():

    item = "this is a get item"
    return item
