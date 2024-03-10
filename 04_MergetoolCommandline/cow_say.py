import cmd
import shlex
import cowsay 


class CowSay(cmd.Cmd):

    file = None
    available_args = ['-e', '-f', '-t']

    def do_list_cows(self, arg):
        'Returns the available builtin cows: list_cows'
        print(cowsay.list_cows())
        
    def do_make_bubble(self, arg):
        'Makes a bubble with certain message: make_bubble [message]'
        message = ""
        
        if len(shlex.split(arg))!=0:
            message = arg

        print(cowsay.make_bubble(message))

    def do_cowsay(self, arg):
        'Makes cow say a specified message: cowsay [-e eyes] [-T tongue] [-f file] [message]'
    
        cow = "default"
        tongue = cowsay.Option.tongue
        eyes = cowsay.Option.eyes

        current_args = shlex.split(arg)
        dct = {}
        used = []
        message = []
        for i in range(len(current_args)):
            if i not in used:
                if current_args[i] in self.available_args:
                    dct[current_args[i]] = current_args[i+1]
                    used.append(i+1)
                else:
                    message.append(current_args[i])
        message = ' '.join(message)
        if dct.get('-e'):
            eyes = dct.get('-e')
        if dct.get('-f'):
            cow = dct.get('-f')
        if dct.get('-t'):
            tongue = dct.get('-t')
        
        print(cowsay.cowsay(message=message, cow=cow, eyes=eyes, tongue=tongue))

    def do_cowthink(self, arg):
        'Makes cow think a specified message: cowthink  [-e eyes] [-T tongue] [-f file] [message]'

        message = ""
        cow = "default"
        tongue = cowsay.Option.tongue
        eyes = cowsay.Option.eyes

        current_args = shlex.split(arg)
        dct = {}
        used = []
        message = []
        for i in range(len(current_args)):
            if i not in used:
                if current_args[i] in self.available_args:
                    dct[current_args[i]] = current_args[i+1]
                    used.append(i+1)
                else:
                    message.append(current_args[i])
        message = ' '.join(message)
        if dct.get('-e'):
            eyes = dct.get('-e')
        if dct.get('-f'):
            cow = dct.get('-f')
        if dct.get('-t'):
            tongue = dct.get('-t')

        print(cowsay.cowthink(message=message, cow=cow, eyes=eyes, tongue=tongue))
    
    def complete_cowsay(self, text, line, begidx, endidx):
        words = (line[:endidx]).split()

        if words[-1] == "-e":
            return [eye.eyes for eye in cowsay.COW_OPTIONS.values()]
        elif  words[-1] == "-T":
            return [tongue.tongue for tongue in cowsay.COW_OPTIONS.values()]
        elif words[-1] == "-f":
            return cowsay.list_cows()
        else:
            return None

    def complete_cowthink(self, text, line, begidx, endidx):
        words = (line[:endidx]).split()

        if words[-1] == "-e":
            return [eye.eyes for eye in cowsay.COW_OPTIONS.values()]
        elif  words[-1] == "-T":
            return [tongue.tongue for tongue in cowsay.COW_OPTIONS.values()]
        elif words[-1] == "-f":
            return cowsay.list_cows()
        else:
            return None

    # functions for cmd usage, from cmd documentation
    def do_record(self, arg):
        'Save future commands to filename:  RECORD cows_thoughts.cmd'

        self.file = open(arg, 'w')

    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK cows_thoughts.cmd'

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def do_bye(self, arg):
        'Stop recording, close the cowsay window, and exit:  bye'

        print('Thank you for using cowsay program')
        self.close()
        return True
    


if  __name__ == "__main__":
    CowSay().cmdloop()
