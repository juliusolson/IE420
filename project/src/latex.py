import numpy as np


def latex_matrix(arr):
    s = "\\begin{bmatrix}"
    for r in range(arr.shape[0]):
        row = " & ".join([str(x)[0:6] for x in arr[r,:]])
        s+="\n"+row + " \\\\"        
    s+="\n\\end{bmatrix}"
    print(s)

def latex_table(df):
	s = "\\begin{table}[H]" + "\n"
	s+= "\\begin{center}" + "\n"
	s+= "\\begin{tabular}{ || c | c | c ||}" + "\n"
	s+= "\\hline" +"\n"
	s+= " & ".join(["\\textbf{" + c + "}" for c in df.columns]) + "\\\\ \n"
	s+= "\\hline" +"\n"
	for row in df.values:
		s += " & ".join([str(val) for val in row]) + "\\\\ \n"
	s += "\\hline \n"
	s += "\\end{tabular}" + "\n"
	s += "\\end{center}" + "\n"
	s += "\\end{table}" + "\n"
	
	f = open("tmp.txt", "a")
	f.write(s)
	f.close()
	