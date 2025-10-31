import sys

class name:
    def __init__(self, values):
        self.spell = values[0]
        self.sex = values[1]
        self.number = int(values[2])

    def __lt__(self, other):
        return self.spell < other.spell

    def add(self, number):
        self.number += number


class names:
    def __init__(self):
        self.parse()

    def parse(self):
        self.data = {}
        for year in range(1880, 2024):
            file = open('yob' + str(year) + '.txt')
            lines = file.readlines()
            for line in lines:
                values = line.split(',')
                if values[0] not in self.data:
                    self.data[values[0]] = name(values)
                else:
                    self.data[values[0]].add(int(values[2]))
        self.list = []
        for key in self.data:
            self.list.append(self.data[key])
        self.list.sort()
        self.data = {}
        for item in self.list:
            self.data[item.spell] = item


# shortened call for standard output and newline
def out(string):
    sys.stdout.write(string + '\n')


# shortened call for file output and newline
def fout(file, string):
    file.write(string + '\n')

outfile = open('every_name_in_SSA_database.txt',"w")

all_names = names()
for key in all_names.data:
    fout(outfile, key)
    if 'your_string_here' in key:
        print(key)

outfile.close()