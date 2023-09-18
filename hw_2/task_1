import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    # print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    # print(result.stdout)
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False

folderin = "/home/kes/tst"
folderout = "/home/kes/out"
folderext = "/home/kes/folder1"
folderbad = "/home/kes/folder2"

def test_step1():
    # test1
    assert checkout_negative(f"cd {folderbad};  7z e arx2.7z -o{folderext} -y", "ERRORS"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout_negative(f"cd {folderbad}; 7z t arx2.7z", "ERRORS"), "test2 FAIL"

def test_step3():
    # test3
    assert checkout(f"cd {folderout}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f"cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"

def test_step6():
    # test6
    res1 = checkout(f"cd {folderin};  7z a {folderout}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {folderout}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"

def test_step7():
    # test7
    res1 = checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
    res2 = checkout(f"ls {folderext}", "test1.txt")
    res3 = checkout(f"ls {folderext}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"

def test_list_files():
    #test8
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "0 files")

def test_extract_files():
    #test9
    subprocess.run(f"7z a {folderext}/tst.7z {folderext}/test1.txt {folderext}/test2.txt", shell=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    assert checkout(f"7z x {folderext}/tst.7z -y", "Files: 2")
