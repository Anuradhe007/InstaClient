import xlsxwriter
import openpyxl

class FileGenerator:

    def createExcelFile(self, userName, createdDateTime, totalLikes, postCaption, likers, numberOfFollowers, timeStamp):

        fileName = userName+'.xlsx'
        workbook = xlsxwriter.Workbook(fileName)
        worksheet = workbook.add_worksheet()

        staticData = (
            ['User name', userName],
            ['Post created date time', createdDateTime],
            ['Caption', postCaption],
            ['Timestamp', timeStamp],
            ['Total likes', totalLikes]
        )

        # Start from the first cell. Rows and columns are zero indexed.
        col = 0
        # Iterate over the data and write it out row by row.
        for name, value in staticData:
            row = 0
            worksheet.write(row, col, name)
            worksheet.write(row+1, col, value)
            col += 1

        row = 0
        for value in likers:
            worksheet.write(row, col, "Likers")
            worksheet.write(row + 1, col, value)
            row += 1

        workbook.close()

#install anaconda
# For Linux/OS X
#sudo apt install python-pip
#pip install -U pip setuptools
#pip install pandas
#sudo apt-get install python3-openpyxl
# For Windows
#python -m pip install -U pip setuptools