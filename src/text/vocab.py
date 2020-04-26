from osprey.voice import Context, insert

vocab_list = [
    'changelog',
    'config',
    'Erlang',
    'formatter',
    'GitLab',
    'grep',
    'json',
    'Kaldi',
    'kinesis',
    'Neovim',
    'readd',
    'struct',
    'subprocess',
    'tig',
    'TypeScript',
    'vim',
    'vocab',
]

ctx = Context('vocab')
ctx.set_rules({
    'vocab <vocab>': lambda m: insert(m['vocab']),
})
ctx.set_lists({
    'vocab': vocab_list,
})
