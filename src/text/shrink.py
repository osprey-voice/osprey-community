from osprey.voice import Context, insert

shrink_map = {
    'administrator': 'admin',
    'administrators': 'admins',
    'allocate': 'alloc',
    'alternate': 'alt',
    'apartment': 'apt',
    'application': 'app',
    'applications': 'apps',
    'architecture': 'arch',
    'argument': 'arg',
    'arguments': 'args',
    'attribute': 'attr',
    'attributes': 'attrs',
    'authenticate': 'auth',
    'binary': 'bin',
    'boolean': 'bool',
    'buffer': 'buf',
    'button': 'btn',
    'calculate': 'calc',
    'certificate': 'cert',
    'character': 'char',
    'column': 'col',
    'command': 'cmd',
    'compare': 'cmp',
    'concatenate': 'concat',
    'condition': 'cond',
    'configuration': 'config',
    'configure': 'config',
    'constant': 'const',
    'context': 'ctx',
    'contribute': 'contrib',
    'control': 'ctrl',
    'decrement': 'dec',
    'define': 'def',
    'delete': 'del',
    'descending': 'desc',
    'destination': 'dest',
    'develop': 'dev',
    'developer': 'dev',
    'development': 'dev',
    'dictionary': 'dict',
    'different': 'diff',
    'directory': 'dir',
    'distribution': 'dist',
    'divider': 'div',
    'division': 'div',
    'document': 'doc',
    'documents': 'docs',
    'else if': 'elif',
    'environment': 'env',
    'error': 'err',
    'escape': 'esc',
    'execute': 'exec',
    'extend': 'ext',
    'extension': 'ext',
    'favorite': 'fav',
    'format': 'fmt',
    'frequency': 'freq',
    'function': 'func',
    'generation': 'gen',
    'generator': 'gen',
    'image': 'img',
    'implement': 'impl',
    'incorporate': 'inc',
    'incorporated': 'inc',
    'include': 'inc',
    'increment': 'inc',
    'initialize': 'init',
    'integer': 'int',
    'iterate': 'iter',
    'iterator': 'iter',
    'language': 'lang',
    'length': 'len',
    'library': 'lib',
    'line': 'ln',
    'memory': 'mem',
    'message': 'msg',
    'microphone': 'mic',
    'minimum': 'min',
    'miscellaneous': 'misc',
    'navigate': 'nav',
    'navigation': 'nav',
    'number': 'num',
    'object': 'obj',
    'operations': 'ops',
    'option': 'opt',
    'package': 'pkg',
    'parameter': 'param',
    'parameters': 'params',
    'position': 'pos',
    'previous': 'prev',
    'production': 'prod',
    'psychology': 'psych',
    'random': 'rand',
    'rectangle': 'rect',
    'reference': 'ref',
    'references': 'refs',
    'repeat': 'rep',
    'request': 'req',
    'result': 'res',
    'return': 'ret',
    'revision': 'rev',
    'sequence': 'seq',
    'source': 'src',
    'square root': 'sqrt',
    'standard': 'std',
    'standard error': 'stderr',
    'standard in': 'stdin',
    'standard out': 'stdout',
    'string': 'str',
    'structure': 'struct',
    'synchronize': 'sync',
    'synchronous': 'sync',
    'synthesizer': 'synth',
    'system': 'sys',
    'temperature': 'temp',
    'temporary': 'tmp',
    'text': 'txt',
    'user': 'usr',
    'user id': 'uid',
    'utilities': 'utils',
    'utility': 'util',
    'value': 'val',
    'variable': 'var',
    'vector': 'vec',
    'velocity': 'vel',
    'vocabulary': 'vocab',
    'volume': 'vol',

    # months,
    'january': 'jan',
    'february': 'feb',
    'march': 'mar',
    'april': 'apr',
    'june': 'jun',
    'july': 'jul',
    'august': 'aug',
    'september': 'sept',
    'october': 'oct',
    'november': 'nov',
    'december': 'dec',
}

ctx = Context('shrink')
ctx.set_commands({
    'shrink <shrink>': lambda m: insert(shrink_map[m['shrink']]),
})
ctx.set_lists({
    'shrink': shrink_map.keys(),
})
