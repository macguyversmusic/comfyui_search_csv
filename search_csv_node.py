import csv
import os

class search_csv:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Path": ("STRING", {"default": "", "multiline": False}),  
                "Row": ("INT", {"default": 0, "min": 0, "max": 10000}),  # User selects row number
                "Column": ("INT", {"default": 1, "min": 1, "max": 100}),  # User selects column number
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Output",)

    FUNCTION = "search_csv"

    CATEGORY = "utils/search_csv"

    def search_csv(self, Path, Row, Column):
        # Check if file exists
        if not os.path.exists(Path):
            return (f"Error: The file {Path} does not exist.",)

        # Read CSV file
        try:
            with open(Path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = list(csv.reader(csvfile, delimiter=','))  # Convert to list to access by index

                if Row >= len(reader):  # Check if row exists
                    return (f"Error: Row {Row} does not exist in the file.",)

                if Column >= len(reader[Row]):  # Check if column exists in the row
                    return (f"Error: Column {Column} does not exist in row {Row}.",)

                return (str(reader[Row][Column]),)

        except Exception as e:
            return (f"Error reading CSV: {str(e)}",)

# Dictionary mapping
NODE_CLASS_MAPPINGS = {
    "Search CSV": search_csv
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "search_csv": "Search CSV"
}
