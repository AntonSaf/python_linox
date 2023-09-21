from checkers import ssh_checkout, upload_files


def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "13", "tests/p7zip-full.deb", "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "13", "echo '13' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "13", "echo '13' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
