import Util.FileProcessor as FR
"""
path = "C:\\\\Users\\\\I_Rin\\\\Documents\\\\Dev\\\\College_KnowledgeEngineering\\\\convert_out.txt"
test = FR.file_read_section(path, "19980101", "19980120")
veri = FR.file_read_section(path, "19980121", "19980125")
for i in range(len(test)):
    FR.file_write("./test.txt", test[i])

for i in range(len(veri)):
    FR.file_write("./veri.txt", veri[i])
"""


def GetWord(line):
    """输入：文件读入的一行字符串|返回值：二维列表，二维列表的第二个属性为词性"""
    # line = self.__f.readline()
    splt = line.split('  ')
    out = []
    for v in splt:
        if v[0] == '[':
            out.append([v[1:v.find('/')], v[v.find('/'):]])
        else:
            out.append([v[0:v.find('/')], v[v.find('/'):]])
    return out


Ls = []


def make_diction(result):

    for line in result:
        t = GetWord(line)
        for i in range(len(t)):
            if i != 0:
                if t[i][0] not in Ls:
                    Ls.append(t[i][0])


if __name__ == "__main__":
    testPath = "C:\\Users\\I_Rin\\Documents\\Dev\\College_KnowledgeEngineering\\convert_out.txt"
    result = FR.file_read_section(testPath, "19980101", "19980131")
    make_diction(result)
    wordVec = FR.file_read(
        "C:\\Users\\I_Rin\\Documents\\Dev\\College_KnowledgeEngineering\\Two\\data\\ctb.50d.vec")
    output = []
    for line in wordVec:
        if line[0:line.find(' ')] in Ls:
            output.append(line+"\n")

    for o in output:
        FR.file_write("./outVect.txt", o)
    # print(Ls)

# self.topList.sort(
#     key=lambda parameter_list: parameter_list[1], reverse=True)
