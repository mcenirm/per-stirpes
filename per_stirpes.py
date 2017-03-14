import psutil


def main(argv=None):
    process = psutil.Popen(*argv)
    process.wait()
    returncode = process.returncode
    return returncode
