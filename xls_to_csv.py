import glob
import pandas as pd

def translate_file(fileglob):
    outdir = "./out"
    for filename in glob.glob(fileglob):
        filenameseg_list = filename.split(".")
        print(filename)
        try:
            xls = pd.ExcelFile(filename)
        except :
            continue
        for sheet_name in xls.sheet_names:
            sheet = xls.parse(sheet_name)
            print(sheet_name)
            print(type(sheet))
            if sheet.empty:
                continue
            csv_name = outdir+filenameseg_list[1]+sheet_name+".csv"
            sheet.to_csv(csv_name)

def main():
    translate_file("./*.xls")
    translate_file("./*.xlsx")

if __name__ == '__main__':
    main()
