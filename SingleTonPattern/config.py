

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Python ka default object creation
            cls._instance.settings = {"db_url": "prod_db"}
        return cls._instance

    def set(self, key: str, value):
        self.settings[key] = value

    def get(self, key: str):
        return self.settings.get(key)


c1 = Singleton()
c1.set("db_url", "mysql://localhost/mydb")

c2 = Singleton()
print(c2.get("db_url"))
