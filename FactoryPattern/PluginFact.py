from ConcreteParsers import *


class PluginFactory:
    _plugin = {}

    @classmethod
    def register(cls, name: str, plugin_class):
        cls._plugin[name] = plugin_class
        print(f"Plugin Registered: {name}")

    @classmethod
    def create(cls, name: str):
        if name not in cls._plugin:
            raise ValueError(f"Unknown Plugin:{name}")
        return cls._plugin[name]()


obj = PluginFactory()
obj.register("Json", JsonParser)
obj.register("CSV", CSVParser)
obj.register("XML", XMLParser)

parser = obj.create("CSV")
result = parser.parse("name,age\nAlice,25")
print(result)
