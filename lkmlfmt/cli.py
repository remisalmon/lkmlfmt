import sys
import lkml


def cli():
    if len(sys.argv) == 1:
        print("usage: lkmlfmt file ...")

        sys.exit(1)

    for file in sys.argv[1:]:
        print("formatting {}".format(file))

        with open(file, mode="r+") as file_object:
            data = lkml.load(file_object)
            file_object.seek(0)
            lkml.dump(data, file_object)
            file_object.truncate()
            file_object.write("\n")

    return
