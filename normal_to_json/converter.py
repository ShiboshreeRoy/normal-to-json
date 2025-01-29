import json
from datetime import datetime

class NormalToJsonConverter:
    @staticmethod
    def convert(data, indent=None, sort_keys=False):
        """
        Convert Python data to JSON.

        Args:
            data: Python data (dict, list, str, int, float, bool, etc.).
            indent (int, optional): Pretty-print JSON with indentation. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.

        Returns:
            str: JSON string.
        """
        def default_serializer(obj):
            """
            Custom serializer for non-serializable objects.
            """
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

        return json.dumps(data, indent=indent, sort_keys=sort_keys, default=default_serializer)

    @staticmethod
    def convert_to_file(data, file_path, indent=None, sort_keys=False):
        """
        Convert Python data to JSON and save it to a file.

        Args:
            data: Python data (dict, list, str, int, float, bool, etc.).
            file_path (str): Path to the output JSON file.
            indent (int, optional): Pretty-print JSON with indentation. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
        """
        json_data = NormalToJsonConverter.convert(data, indent=indent, sort_keys=sort_keys)
        with open(file_path, "w") as file:
            file.write(json_data)