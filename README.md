# 📦 Design Patterns in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Concepts-green?style=flat)
![Patterns](https://img.shields.io/badge/Design-Patterns-orange?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

> A comprehensive collection of commonly used **Software Design Patterns** implemented in Python — built to write cleaner, scalable, and maintainable code.

---

## 📌 Overview

This repository demonstrates the implementation of commonly used software design patterns in Python. Design patterns provide reusable solutions to common software design problems and help in building **scalable, maintainable, and clean systems**.

This project is created to strengthen understanding of **object-oriented design principles** and improve code structure for real-world applications.

---

## 🎯 Objectives

- ✅ Understand core design patterns and their use cases
- ✅ Implement patterns using Python
- ✅ Improve code reusability and maintainability
- ✅ Apply patterns in real-world scenarios

---

## 🧠 Design Patterns Covered

### 1. 🏗️ Creational Patterns
> Focus on object creation mechanisms.

| Pattern | Description |
|--------|-------------|
| Singleton | Ensures only one instance of a class exists |
| Factory Method | Creates objects without specifying exact class |
| Abstract Factory | Factory of factories |
| Builder | Constructs complex objects step by step |
| Prototype | Creates objects by copying existing ones |

---

### 2. 🔗 Structural Patterns
> Deal with object composition and relationships.

| Pattern | Description |
|--------|-------------|
| Adapter | Converts one interface to another |
| Decorator | Adds behavior to objects dynamically |
| Facade | Provides a simplified interface |
| Proxy | Controls access to another object |
| Composite | Treats individual and composite objects uniformly |

---

### 3. 🔄 Behavioral Patterns
> Focus on communication between objects.

| Pattern | Description |
|--------|-------------|
| Observer | Notifies multiple objects about state changes |
| Strategy | Selects algorithm at runtime |
| Command | Encapsulates a request as an object |
| State | Alters behavior when internal state changes |
| Template Method | Defines skeleton of an algorithm |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts:** OOP — Encapsulation, Inheritance, Polymorphism, Abstraction

---

## 📂 Project Structure

```
design-patterns/
│
├── creational/
│   ├── singleton.py
│   ├── factory.py
│   ├── abstract_factory.py
│   ├── builder.py
│   └── prototype.py
│
├── structural/
│   ├── adapter.py
│   ├── decorator.py
│   ├── facade.py
│   ├── proxy.py
│   └── composite.py
│
├── behavioral/
│   ├── observer.py
│   ├── strategy.py
│   ├── command.py
│   ├── state.py
│   └── template_method.py
│
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/akshaytanmane150294/Design_Pattern_Prac.git
```

**2. Navigate to the folder:**
```bash
cd FactoryPattern
```

**3. Run any pattern file:**
```bash
python FactoryPattern/PluginFact.py
```

---

## 💡 Example: Singleton Pattern

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True ✅ — Same instance returned
```

**When to use:** Database connections, Logger, Config Manager — anywhere only ONE instance should exist.

---

## 💡 Example: Factory Pattern

```python
class PluginFactory:
    _plugins = {}

    @classmethod
    def register(cls, name: str, plugin_class):
        cls._plugins[name] = plugin_class
        print(f"Plugin Registered: {name}")

    @classmethod
    def create(cls, name: str):
        return cls._plugins[name]()
```

**When to use:** When object creation logic should be centralized and decoupled from usage.

---

## 📈 Real-World Use Cases

- 🖥️ Scalable backend systems
- 🔧 Microservices architecture
- 🌐 API design
- ⚙️ Distributed systems
- 🧩 Plugin systems

---

## 📚 Learning Outcomes

By completing this project, you will:

- 💡 Gain strong understanding of design patterns
- 🧹 Write cleaner and more maintainable code
- 🎯 Be better prepared for software engineering interviews
- 🔍 Recognize patterns in open-source codebases

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repo
2. Create a new branch: `git checkout -b feature/pattern-name`
3. Commit your changes: `git commit -m "Add: XYZ pattern"`
4. Push to the branch: `git push origin feature/pattern-name`
5. Submit a Pull Request ✅

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and share!

---

<p align="center">Made with ❤️ by <strong>Akshay Tanmane</strong></p>
<p align="center">
  <a href="https://github.com/akshaytanmane150294">GitHub</a> •
  <a href="https://www.linkedin.com/in/akshay-tanmane-6a6ab1117/">LinkedIn</a> •
  <a href="https://porfolioat.vercel.app/">Portfolio</a>
</p>
