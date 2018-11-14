from openpyxl import Workbook
from openpyxl import load_workbook
import datetime

class FileGenerator:
    def createExcelFile(self, userName, postCreatedTime, detailsList, filePath, postCount):
        fg = FileGenerator()
        fileName = fg.fileNameCreator(userName, postCreatedTime, postCount)
        workbook = Workbook()
        worksheet = workbook.active

        for data in detailsList:
            worksheet.append(data)

        workbook.save(filePath+fileName)

    def fileNameCreator(self, userName, postCreationTime, postCount):
        spentTimeInMinutes = (datetime.datetime.now()-postCreationTime).days * 24 * 60
        hours = spentTimeInMinutes/60
        minutes = spentTimeInMinutes%60
        todayDate = datetime.datetime.now()

        fileName = userName+'-Post-'+str(postCount)+'-Likes After '
        if hours>0:
            fileName = fileName + str(hours) + ' hours ' + str(minutes) + ' minutes_' + todayDate.strftime('%b %d,%Y')+'.xlsx'
        else:
            fileName = fileName + str(minutes) + 'minutes_' + todayDate.strftime('%b %d,%Y') + '.xlsx'

        return fileName