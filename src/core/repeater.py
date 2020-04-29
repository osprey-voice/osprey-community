from osprey.voice import Context, repeat

ctx = Context('repeater')
ctx.set_commands({
    'repeat <n>': lambda m: repeat(m['n'] - 1),
    'repeat <n> more': lambda m: repeat(m['n']),
})
