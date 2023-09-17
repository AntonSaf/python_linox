import subprocess
import string
def check_output(cmd, txt):
    out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    check_str = out.stdout.translate(str.maketrans(' ', ' ', string.punctuation)).split("\n")
    if out.returncode == 0:
        for el in check_str:
            print(el)
            if txt in el:
                return True
        return False
    else:
        return f'Некорректный вызов: {cmd}'

cmd = "cat /etc/os-release"
txt = "jammy"

print(check_output(cmd, txt))
