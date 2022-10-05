import os,subprocess,sys,datetime
def check_root():
    euid_user = os.geteuid()
    if euid_user != 0:
        print("run as root")
        sys.exit(1)
    return euid_user


def system_update(flag: str) -> str:
    if flag == "ud":
         result = subprocess.run(['apt','update'], stdout=subprocess.PIPE)
         result2 = subprocess.run(['apt','upgrade','-y'], stdout=subprocess.PIPE)
    output = result2.stdout.decode("utf-8")
    return(output)

check_root()
log = open(f"{datetime.datetime.now()}.txt","w")
log.write(system_update("ud"))
log.close()