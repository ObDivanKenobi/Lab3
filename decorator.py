def a_decorator_rounding_float(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        result = function_to_decorate(*args, **kwargs)
        if isinstance(result, int): return result
        return round(result, 2)
    return a_wrapper_accepting_arbitrary_arguments