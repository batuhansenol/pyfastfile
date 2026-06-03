

def parameter_check(*args, **kwargs):
    for i, value in enumerate(args):
        if value is None:
            raise ValueError(f"Positional argument at index {i} cannot be None!")
    
    for name, value in kwargs.items():
        if value is None:
            raise ValueError(f"Argument '{name}' cannot be None!")
