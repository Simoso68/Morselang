from subprocess import run, DEVNULL
from threading import Thread
from sys import stdout, exit
from platform import system
from time import sleep

completed = False

def msg():
    while True:
        for m in ["\r[|] Building from source ...", "\r[/] Building from source ...", "\r[-] Building from source ...", "\r[\] Building from source ...", "\r[|] Building from source ...", "\r[/] Building from source ...", "\r[-] Building from source ...", "\r[\] Building from source ..."]:
            if completed:
                stdout.write("\r[✔] Building process completed!")
                stdout.flush()
                exit()
            stdout.write(m)
            stdout.flush()
            sleep(0.3)

buildmsg = Thread(target=msg)
buildmsg.start()

if system() == "Windows": name = "morselang.exe"
elif system() == "Linux": name = "morselang"
elif system() == "Darwin": name = "morselang.app"
else: name = "copy"

run(["mkdir", "out"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
run(["pyinstaller", "--noconfirm", "--onefile", "--name", name, "src/main.py"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
with open(f"dist/{name}", "rb") as c:
    with open(f"out/{name}", "wb") as p:
        p.write(c.read())
        p.close()

if system() == "Windows":
    run(["rmdir", "dist", "/f", "/Q"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
    run(["rmdir", "build", "/f", "/Q"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
    run(["del", "morselang.spec", "/f", "/Q"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
elif system() == "Linux" or system() == "Darwin":
    run(["rm", "-rf", "dist"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
    run(["rm", "-rf", "build"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
    run(["rm", "-f", "morselang.spec"], stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)

completed = True