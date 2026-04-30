
from abc import ABC, abstractmethod

# InterFace


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Step 2: Receiver (actual logic wahan hoti hai)


class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, word: str):
        self.text += word

    def erase(self, length: int):
        self.text = self.text[:-length] if length else self.text

    def get_text(self):
        return self.text

# Step 3: Concrete Command


class WriteCommand(Command):
    def __init__(self, editor: TextEditor, word: str):
        self._editor = editor
        self._word = word

    def execute(self):
        self._editor.write(self._word)

    def undo(self):
        self._editor.erase(len(self._word))


class CommandManager:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def execute(self, command: Command):
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()

    def undo(self):
        if self._history:
            cmd = self._history.pop()
            cmd.undo()
            self._redo_stack.append(cmd)

    def redo(self):
        if self._redo_stack:
            cmd = self._redo_stack.pop()
            cmd.execute()
            self._history.append(cmd)


editor = TextEditor()
manager = CommandManager()

manager.execute(WriteCommand(editor, "Hello "))
manager.execute(WriteCommand(editor, "World!"))

print(editor.get_text())

manager.undo()


print(editor.get_text())
