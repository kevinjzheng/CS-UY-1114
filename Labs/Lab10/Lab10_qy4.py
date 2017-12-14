
lst = [['Header1', 'Header2', 'Header3', 'Header4'], ['R1C1', 'R1C2', 'R1C3',
    'R1C4'], ['R2C1', 'R2C2', 'R2C3', 'R2C4'], ['R3C1', 'R3C2', 'R3C3', 'R3C4']]

def html_table_generator(lst,file_to_write_to):
    f = open(file_to_write_to,"w")
    print("<html>", file = f)
    print("\t","<table>", file = f)
    for i in range(len(lst)):
        print("\t","\t","<tr>",file = f)
        for j in range(len(lst[i])):
            print("\t","\t","\t","<th>",lst[i][j],"</th>",file = f)
        print("\t","\t","</tr>",file = f)
    print("\t", "</table>", file=f)
    print("</html>", file=f)

html_table_generator(lst,'html_maker.html')