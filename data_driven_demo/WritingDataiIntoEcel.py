import openpyxl

class dataDriven():
    def write_data(self):
        path = "C:\\Users\\fathih\\PycharmProjects\\Python Automation\\data_driven_demo\\Book2.xlsx"
        workbook = openpyxl.load_workbook(path)

        sheet=workbook.active

        for r in range(1,6):
            for c in range(1,4):
                sheet.cell(row=r,column=c).value="Welcome to Automation"

        workbook.save(path)



aa=dataDriven()
aa.write_data()