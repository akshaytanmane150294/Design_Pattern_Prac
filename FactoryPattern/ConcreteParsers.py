from Parser import *


class JsonParser(Parser):
    def parse(self, data):
        return {'type': 'Json', "data": data}


class CSVParser(Parser):
    def parse(self, data):
        return {'type': 'CSV', "data": data}


class XMLParser(Parser):
    def parse(self, data):
        return {'type': 'XML', "data": data}
