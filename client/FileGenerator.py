from openpyxl import Workbook
from openpyxl import load_workbook

class FileGenerator:
    def createExcelFile(self, userName, postId, detailsList, numberOfFollowers, postCount):

        fileName = userName+'.xlsx'
        try:
            workbook = load_workbook(fileName)
        except FileNotFoundError:
            print("File not created")
            workbook = Workbook()

        worksheet = workbook.create_sheet("Sheet"+str(postCount))

        for data in detailsList:
            worksheet.append(data)

        workbook.save(fileName)
