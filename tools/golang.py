from .env import BUILD_DIR
from subprocess import check_call, check_output

class GoLang:
    "Manages golang."

    def __init__(self, build_dir=BUILD_DIR):
        self.build_dir = build_dir
        self._go_command = 'go'

    def run(self,args,env):
        command = [self._go_command] + args
        print(' '.join(command))
        check_call(command, cwd=self.build_dir, env=env)