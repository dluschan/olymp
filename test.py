#python3 test.py /Users/white/Documents/Projects/olymp/2014-15/river.py /Users/white/Documents/Учебные_Материалы/олимпиады/Всероссийская_Олимпиада_Школьников/информатика/2014-15/ru-olymp-regional-2015-archive/day1/river

import sys
import os
import shutil
import fnmatch
import filecmp

etalonsuffix = ".a"
mysuffix     = ".b"
updir        = "../"
tmpdir       = "tmp/"
testpath     = "tests/"
diff         = "diff.txt"
taskname     = sys.argv[2] + "/"

if os.path.exists(tmpdir) == True:
    print("Warning! Temporary directory already exists!")
    answer = input("Remove it?")
    if answer in ["Y", "y", "Yes", "yes"]:
        shutil.rmtree(tmpdir)
    else:
        print("Exit")
        exit(100)

os.mkdir(tmpdir)
os.chdir(tmpdir)
for path, dirname, filelist in os.walk(updir + taskname + testpath):
    for name in filelist:
        f, ext = os.path.splitext(name)
        if ext == "" and f != ".DS_Store":
            etalon = name + etalonsuffix
            output = name + mysuffix
            os.system("python3 " + updir + sys.argv[1] + " < " + os.path.join(path, name) + " > " + output)
            shutil.copy(os.path.join(path, etalon), etalon)
            os.system("diff " + output + " " + etalon + " > " + diff)
            if os.path.getsize(diff) != 0:
                print("Error! Test number " + name)
                os.system("cat " + diff)
                os.chdir(updir)
                shutil.rmtree(tmpdir)
                exit(1)

print("Ok")
os.chdir(updir)
shutil.rmtree(tmpdir)
exit(0)
