from colorama import Fore, Style
class Menu:
    def __init__(self,options):
        self.optionsDict = options
        self.optionsList= list(self.optionsDict)

    def showOptions(self):
        for index,option in enumerate(self.optionsList):
            print(f"{index+1}. {option}") 


    def executeSelect(self,choicedValue,*arg):
        self.choicedOption = choicedValue-1
        self.selectOption= self.optionsList[self.choicedOption]

        if 0 <= self.choicedOption <= len(self.optionsList):
            self.optionsDict[self.selectOption](*arg)

