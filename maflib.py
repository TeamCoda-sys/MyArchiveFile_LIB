from zipfile import ZipFile
# EC

def makeFile(name, ext):
    mafObj = ZipFile(name + '.' + ext, 'w')
    