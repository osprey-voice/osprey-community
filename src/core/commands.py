import subprocess
from sys import platform

from osprey.voice import Context


def is_program_running(name):
    return subprocess.run(['pgrep', name], capture_output=True).returncode == 0


def clear_notifications(m):
    if platform == 'win32':
        pass
    elif platform == 'darwin':
        pass
    else:
        if is_program_running('mako'):
            subprocess.run('makoctl dismiss -a'.split())


ctx = Context('commands')
ctx.set_rules({
    'clear notifications': clear_notifications,
})
