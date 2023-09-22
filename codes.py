from languages import languages


def get_params(params):
    params_list = []
    for i, _ in enumerate(params):
        params_list.append(f'test["input"][{i}]')
    return ', '.join(params_list)


def get_function(params, func):
    params = get_params(params)
    return f'{func}({params})'


def get_code(language, code, func, params):
    prefix = languages[language]['prefix']
    function = get_function(params, func)
    suffix = languages[language]['suffix'](function)
    return prefix + code + suffix