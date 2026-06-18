import os

dir = ""

def main():
    this_set = set()
    this_set.add("hi")
    print(this_set)

    contents = os.listdir(dir)
    for file in contents:
        # get current filename

        if file in this_set:
            print(file + " was skipped\n")
            continue
        else:
            print(file)
   #     f = open(dir + "\\" + file)
        file_name = input("input file name: ")
        os.rename(dir + "\\" + str(file), dir + "\\" + file_name + ".mp3")
        this_set.add(file_name)
    #    f.close()
    

if __name__ ==  '__main__':
    main()
