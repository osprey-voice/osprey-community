from osprey.voice import Context, insert

vocab_list = [
    'backtrace',
    'bifurcate',
    'bitwise',
    'callable',
    'cardioid',
    'changelog',
    'committer',
    'config',
    'deallocate',
    'deallocated',
    'deallocating',
    'delimiter',
    'delimiters',
    'delineator',
    'delineators',
    'Erlang',
    'Flatpak',
    'formatter',
    'formatters',
    'GitLab',
    'Gitter',
    'grep',
    'homeserver',
    'Kaldi',
    'kinesis',
    'lints',
    'Neovim',
    'nondeterminism',
    'nondeterministic',
    'prepend',
    'readd',
    'README',
    'refactor',
    'reinstantiate',
    'struct',
    'structs',
    'subcommand',
    'subcommands',
    'subprocess',
    'subprocesses',
    'sudo',
    'tendinitis',
    'tendinosis',
    'tendon',
    'tendons',
    'tig',
    'todo',
    'Todoist',
    'TypeScript',
    'Unicode',
    'uninstalling',
    'vim',
    'vocab',
]

vocab_map = {
    'free b s d': 'FreeBSD',
    'h top': 'htop',
    'j query': 'jQuery',
    'mac o s': 'macOS',
    'net b s d': 'NetBSD',
    'n vim': 'nvim',
    'open b s d': 'OpenBSD',
    'pip x': 'pipx',
    'p s util': 'psutil',
    'u t f 8': 'UTF-8',
    'x eighty six': 'x86',
    'x eighty six sixty four': 'x86_64',
}
vocab_map.update({word: word for word in vocab_list})

ctx = Context('vocab')
ctx.set_commands({
    'vocab <vocab>': lambda m: insert(vocab_map[m['vocab']]),
    'vocab upper <vocab>': lambda m: insert(vocab_map[m['vocab']].capitalize()),
    'vocab lower <vocab>': lambda m: insert(vocab_map[m['vocab']].lower()),
    'vocab all caps <vocab>': lambda m: insert(vocab_map[m['vocab']].upper()),
})
ctx.set_choices({
    'vocab': vocab_map.keys(),
})
