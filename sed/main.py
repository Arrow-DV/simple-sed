"""
Simple Sed ( Linux / Unix Text Processor Command)
Basic Functions :
[+] Read String
[+] Replace String
[+] Delete String
[+] Search For String Indexes
"""
class Sed:
    def __init__(self, filepath: str):
        with open(filepath, "r") as file:
            self.file_content = file.read()

    def delete_string(self, target_string: str, limit: int = -1):
        self.file_content = self.file_content.replace(target_string, "", limit)
        return self  

    def replace_string(self, old_word: str, new_word: str, limit: int = -1):
        self.file_content = self.file_content.replace(old_word, new_word, limit)
        return self

    def search_string(self, target_str: str):
        words = self.file_content.split()
        positions = [i for i, word in enumerate(words) if word == target_str]
        print(f"{positions}")
        return self

    def print(self):
        print(self.file_content)
        return self

Sed("file.txt").replace_string("ali", "mohamed").print()
print("-"*30)
Sed("file.txt").delete_string("###").print()
print("-"*30)
Sed("file.txt").search_string("ali")
