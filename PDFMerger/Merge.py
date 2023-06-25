import os
from pypdf import PdfMerger

# path of the folder where pdfs are present
folder = os.listdir(r'C:\Users\91990\Downloads\Prog_Codes\Python\MergeThese')

a = PdfMerger()

for file in folder:
    if file.endswith(".pdf"):
        b = os.path.join(r'C:\Users\91990\Downloads\Prog_Codes\Python\MergeThese', file)
        print(b)
        a.append(b)

# location where merged pdf file will get created
a.write("MergeThese\merged.pdf")
a.close()
print("done")
