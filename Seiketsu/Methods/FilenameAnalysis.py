import Seiketsu.Methods.Patterns

class FilenameAnalyzer():
    def scan(self, path):
        for keyword in Seiketsu.Methods.Patterns.keywords():
            if keyword in path.lower():
                return True, keyword