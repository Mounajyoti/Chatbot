def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")