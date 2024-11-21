import csv
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader

from .baseclass import FileParserBaseClass

#### csv file parser currently not used
class CSVParser(FileParserBaseClass):
    def __init__(self,filename):
        self.file_name=filename
    
    def parse(self):
        try:
            with open(self.file_name) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                return csv_reader
        except:
            return None


class PDFParser(FileParserBaseClass):
    def __init__(self, filename):
        self.file_name = filename
    
    def parse(self):
        try:
            loader = PyPDFLoader(self.file_name)
            pages = loader.load_and_split()
            return pages
        except:
            return None


class TextFileParser(FileParserBaseClass):
    def __init__(self, filename):
        self.file_name = filename
    
    def parse(self):
        try:
            loader = TextLoader(self.file_name)
            loader.load()
            return loader
        except FileNotFoundError:
            return None
        except Exception as e:
            return None


class FileParserFactory():
    def __init__(self,file_type,file_name) -> None:
        self.type=file_type
        self.file_parsers={
            "csv":CSVParser(file_name),
            "pdf":PDFParser(file_name),
            "txt":TextFileParser(file_name)
        }

    def parse(self):
        return self.file_parsers[self.type].parse()


