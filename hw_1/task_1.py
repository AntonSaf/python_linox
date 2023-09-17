import subprocess

def check_output(cmd, txt):
    out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    # print(out.stdout)
    if out.returncode == 0:
        if txt in out.stdout:
            return True
        else:
            return False
    else:
        return f'error command: {cmd}'

cmd = "cat /etc/os-release"
txt = "jammy"

print(check_output(cmd, txt))
