from inspect import signature, Parameter, _ParameterKind

async def ha(a: int, b: int) -> int:
    return a + b

s = signature(ha)

print(dir(s))

p = Parameter('value', kind=_ParameterKind.KEYWORD_ONLY, default=4, annotation=int)
p2 = Parameter('value2', kind=_ParameterKind.KEYWORD_ONLY, default=5, annotation=int)

print(p)

print(s)

print(s.replace(parameters=[p, p2], return_annotation=bool))
