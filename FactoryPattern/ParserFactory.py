from ConcreteParsers import *


class ParserFactory:
    def create_parser(self, filetype: str):
        parser = {'json': JsonParser,
                  'csv': CSVParser,
                  'xml': XMLParser}

        if filetype not in parser:
            raise ValueError(f'Unknown Parser:{filetype}')

        return parser[filetype]()


objParser = ParserFactory()
nameparser = objParser.create_parser("csv")
print(nameparser.parse("name,age\nAlice,25"))
