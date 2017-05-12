class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.name = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, reflection = {}, First appeared in {}".format(self.name,
                                                                             self.typing,
                                                                             self.reflection,
                                                                             self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
