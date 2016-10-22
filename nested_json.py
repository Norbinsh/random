json_data = { }


# yield from recursion
def deepiter(x, prefix=''):
    if isinstance(x, list):
        for i, v in enumerate(x):
            yield from deepiter(v, prefix+'[{!r}]'.format(i)) # {!r} = __repr_
            # formatting
    elif isinstance(x, dict):
        for k, v in x.items():
            yield from deepiter(v, prefix+'[{!r}]'.format(k))
    else:
        yield '{} = {!r}'.format(prefix, x)

for s in deepiter(json_data):
    print(s)















