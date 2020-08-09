import os


def isYash(filename):
    with open(filename,"r") as f:
        filecontent = f.read()
    if "yash" in filecontent.lower():
        return True
    else:
        return False
if __name__ == "__main__":
    dir = os.listdir()
    count = 0
    print(dir)
    for item in dir:
        if item.endswith("txt"):
            Flag = isYash(item)
            if(Flag):
                print(f"******Yash is found in {item} ******")
                count += 1
            else:
                print(f"Yash not Found in {item}")
    print("******* Yash Summery *******")
    print(f"Yash Found in {count} Files")