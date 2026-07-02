class FileReader:
    def read_lines(self, file_path):
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []   