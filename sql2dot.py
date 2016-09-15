import sys, getopt

table_arr = []
table_count = 0
counter = 0
foreign_arr = []

def write_tables():
  
    global table_arr
    global table_count

    for line in file:
        words = line.split()

        if 'TABLE' in words:
            table_arr.append(words[2])
            dotfile.write("%s\n" %words[2])
            table_count = table_count + 1

#MAIN---------------------------------------------------------------------------

file = open(sys.argv[1], 'rb')
dotfile = open('result.dot', 'w')

dotfile.write("digraph {\nrankdir=BT\n\n")

#LIST TABLE NODES---------------------------------------------------------------

dotfile.write("// TABLE Nodes:\n")
dotfile.write("\nnode [shape=\"box3d\" style=\"filled\" color=\"#0000FF\" fillcolor=\"#EEEEEE\" fontname=\"Courier\" ]\n\n")

write_tables()
dotfile.write("\n")

#LIST ATTRIBUTE NODES-----------------------------------------------------------

dotfile.write("// ATTRIBUTE Nodes:\n\n")
dotfile.write("node [shape=\"box\" style=\"rounded\" width=0 height=0 color=\"#00AA00\"]\n\n")

file.seek(0)

while(True):
    line = file.readline()
    if table_arr[counter] in line:
        temp_counter = counter
        counter = counter + 1
        file.readline() #this is the '('
        
        temp = file.readline()
        temp2 = temp.split()

        while(len(temp2) > 1 and temp2[0] != 'CONSTRAINT'):
            dotfile.write(table_arr[temp_counter] + "_" + temp2[0])
            dotfile.write('[label="' + temp2[0])

            if 'PRIMARY' and 'REFERENCES' in temp2:
                dotfile.write('" fontname="Courier-Bold" style="rounded" color="#0000FF"]\n')  
                foreign_arr.append(table_arr[temp_counter] + "_" + temp2[0] + " -> " + temp2[temp2.index('REFERENCES') + 1])
            elif 'PRIMARY' in temp2:
                dotfile.write('" fontname="Courier-Bold"]\n')  
            elif 'REFERENCES' in temp2:
                dotfile.write('" style ="rounded" color="#0000FF"]\n')
                foreign_arr.append(table_arr[temp_counter] + "_" + temp2[0] + " -> " + temp2[temp2.index('REFERENCES') + 1])
            else:
                dotfile.write('"]\n')

            temp = file.readline()
            temp2 = temp.split()
    
    if (counter == table_count):
        break

#LIST EDGES---------------------------------------------------------------------

dotfile.write("\n// EDGES of Type: Table --> Attribute\n\n")
dotfile.write("edge [color=\"#00AA00\" dir=none]\n\n")

file.seek(0)
counter = 0

while(True):
    line = file.readline()
    if table_arr[counter] in line:
        temp_counter = counter
        counter = counter + 1
        file.readline() #this is the '('
        
        temp = file.readline()
        temp2 = temp.split()

        while(len(temp2) > 1 and temp2[0] != 'CONSTRAINT'):
            dotfile.write(table_arr[temp_counter] + " -> " + table_arr[temp_counter] + "_" + temp2[0] + "\n")

            temp = file.readline()
            temp2 = temp.split()
    
    if (counter == table_count):
        break

#LIST FOREIGN EDGES-------------------------------------------------------------

dotfile.write("\n//EDGES of Type: Foreign Key\n\n")

dotfile.write("edge [color=red dir=foward style=dashed label=\" FK\" fontname=\"Verdana\" fontcolor=red fontsize=10]\n\n")

for i in foreign_arr:
    dotfile.write(i + "\n")

#CLOSING BRACE------------------------------------------------------------------
dotfile.write("}")