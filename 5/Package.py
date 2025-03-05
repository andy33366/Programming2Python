from Toy import Toy

class Package:
    def __init__(self, content, label):
        self.content = content
        self.label = label

    def getContent(self):
        return self.content

    def getLabel(self):
        return self.label
