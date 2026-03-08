from UI import MainLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EFPlanner")
        self.setFixedSize(800, 600)

        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.mainLayout = QHBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        buttonLayout = QVBoxLayout()
        button = QPushButton("Load Characters")
        button.setFixedSize(100, 30)
        buttonLayout.addWidget(button)
        buttonLayout.setHorizontalSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        buttonLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainLayout.addLayout(buttonLayout)

        charMngr = CharacterManager()
        charWidget = CharacterListWidget(charMngr)

        self.mainLayout.addLayout(charWidget)

class CharacterListWidget(QVBoxLayout):
    charMngr:CharacterManager
    def __init__(self, charMngr:CharacterManager):
        super().__init__()
        self.charMngr = charMngr

        # read character.data
        chars = self.charMngr.get()
        # loop over character list and create CharacterWidget for each
        for c in chars:
            testLabel = QLabel(c.name)
            testLabel.setMaximumSize(5000, 100)
            self.addWidget(testLabel)
        self.setAlignment(Qt.AlignmentFlag.AlignTop)
        
class CharacterWidget(QWidget):
    def __init__(self):
        super().__init__()

        # add a context menu here maybe for handling Edit/Delete stuff
        layout = QVBoxLayout()
        self.setLayout(layout)

        titleLayout = QHBoxLayout()
        layout.addLayout(titleLayout)

        statLayout = QGridLayout()
        layout.addLayout(statLayout)

class CharacterManager():
    __list:set[Character]
    __filepath:str

    def __init__(self, filepath:str|None = None):
        print()
        if filepath == None:
            self.__filepath = "Data\\characters.data"
        else:
            self.__filepath = filepath

    def get(self) -> set[Character]:
        self.__list = self.__load()
        if self.__list == None:
            return set[Character]
        return self.__list
        

    def add(self, character:Character):
        self.__list.add(character)
        self.__save()
    
    def __save(self):
        content = ["Name,Potential,Elite,Level,BATK,BS,CS,Ult,Trust,MaxPassive1,Passive1,MaxPassive2,Passive2,MaxBase1,Base1,MaxBase2,Base2\r\n"]
        for c in self.__list:
            content.append(f"{c.name},{c.potential},{c.level},{c.batk},{c.bs},{c.cs},{c.ult},{c.trust},{c.maxPassive1},{c.passive1},{c.maxPassive2},{c.passive2},{c.maxBase1},{c.base1},{c.maxBase2},{c.base2}\r\n")
        with open(self.__filepath, "w") as file:
            file.writelines(content)

    def __load(self) -> set[Character]:
        content:list[str]
        characters = set[Character]()
        with open(self.__filepath, "r") as file:
            content = file.readlines()
        for c in content:
            if c.startswith("Name"):
                continue
            split = c.split(',')
            name = split.pop(0)
            parsedSplit = list[int]()
            for s in split:
                parsedSplit.append(int(s))
            characters.add(Character(name, parsedSplit))
        return characters
    
class Character():
    name:str
    potential:int
    level:int
    batk:int
    bs:int
    cs:int
    ult:int
    trust:int
    maxPassive1:int
    passive1:int
    maxPassive2:int
    passive2:int
    maxBase1:int
    base1:int
    maxBase2:int
    base2:int
    def __init__(self, name:str = "New", 
                 potential:int = 0, 
                 level:int = 0, 
                 batk:int = 0, 
                 bs:int = 0, 
                 cs:int = 0, 
                 ult:int = 0, 
                 trust:int = 0, 
                 maxPassive1:int = 0, 
                 passive1:int = 0, 
                 maxPassive2:int = 0, 
                 passive2:int = 0, 
                 maxBase1:int = 0, 
                 base1:int = 0, 
                 maxBase2:int = 0, 
                 base2:int = 0, 
                 values:list[int]|None = None):
        self.name = name
        if values == None:
            self.potential = potential
            self.level = level
            self.batk = batk
            self.bs = bs
            self.cs = cs
            self.ult = ult
            self.trust = trust
            self.maxPassive1 = maxPassive1
            self.passive1 = passive1
            self.maxPassive2 = maxPassive2
            self.passive2 = passive2
            self.maxBase1 = maxBase1
            self.base1 = base1
            self.maxBase2 = maxBase2
            self.base2 = base2
        else:
            self.potential = values[0]
            self.level = values[1]
            self.batk = values[2]
            self.bs = values[3]
            self.cs = values[4]
            self.ult = values[5]
            self.trust = values[6]
            self.maxPassive1 = values[7]
            self.passive1 = values[8]
            self.maxPassive2 = values[9]
            self.passive2 = values[10]
            self.maxBase1 = values[11]
            self.base1 = values[12]
            self.maxBase2 = values[13]
            self.base2 = values[14]
        