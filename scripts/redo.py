import os
import glob
import zipfile


if __name__ == "__main__":
    # Select input and outputs files by origin format ========
    files = glob.glob("*")
    answers = list(filter(lambda x: x.endswith('.a'),files))
    tests = list(filter(lambda x: x.isdigit(), files))

    # Change format to hackerrank zip ========================
    if not os.path.exists("input"):
        os.makedirs("input")
    if not os.path.exists("output"):
        os.makedirs("output")

    for ai, ao in zip(tests, [os.path.join("input", t) for t in tests]):
        os.replace(ai, ao)
    for ai, ao in zip(answers, [os.path.join("output", a) for a in answers]):
        os.replace(ai, ao)

    files_in = glob.glob("input/*")
    files_out = glob.glob("output/*")

    # for fin in files_in:
    #     os.rename(fin, fin+".txt")
    # for fout in files_out:
    #     os.rename(fout, fout.replace(".a", ".txt"))

    # for fin in files_in:
    #     os.rename(fin, os.path.join(os.path.split(fin)[0], "input"+ os.path.split(fin)[1]))

    # for fout in files_out:
    #     os.rename(fout, os.path.join(os.path.split(fout)[0], "output"+ os.path.split(fout)[1]))

    zf = zipfile.ZipFile("testcases.zip", "w")
    for dirname, subdirs, files in os.walk("input"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    for dirname, subdirs, files in os.walk("output"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

