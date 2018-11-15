from openpyxl import Workbook
import datetime
import math

class FileGenerator:
    def createExcelFile(self, userName, postCreatedTime, detailsList, filePath):
        fg = FileGenerator()
        fileName = fg.fileNameCreator(userName, postCreatedTime)
        workbook = Workbook()
        worksheet = workbook.active

        for data in detailsList:
            worksheet.append(data)

        workbook.save(filePath+fileName)

    def fileNameCreator(self, userName, postCreationTime):
        todayDate = datetime.datetime.now()
        spentTimeInMinutes = math.ceil((datetime.datetime.strptime(todayDate.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S") - postCreationTime).seconds / 60)
        hours = math.floor(spentTimeInMinutes/60)

        fileName = userName+'-'+str(postCreationTime)+'-Likes After '
        if hours > 0:
            fileName = fileName + str(hours) + ' hours ' + str(spentTimeInMinutes % 60) + ' minutes_' + todayDate.strftime('%b %d,%Y')+'.xlsx'
        else:
            fileName = fileName + str(spentTimeInMinutes) + 'minutes_' + todayDate.strftime('%b %d,%Y') + '.xlsx'

        return fileName