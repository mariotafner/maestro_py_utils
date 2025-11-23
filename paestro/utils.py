import pytz
import random
import string
from datetime import datetime, timedelta
from PIL import Image
from io import BytesIO
import base64
import gzip
import io

class Paestro:
    """Utility class with static methods for common operations."""
    
    @staticmethod
    def test():
        """Prints 'paestro' to the console. Test method."""
        print("paestro")
        
    @staticmethod
    def random_id():
        """
        Generates a random hexadecimal ID of 16 characters.
        
        Returns:
            str: String with 16 random hexadecimal characters.
        """
        return ''.join(random.choices('abcdef0123456789', k=16))

    @staticmethod
    def random_string(length: int, chars: str = (string.ascii_letters + string.digits)):
        """
        Generates a random string with the specified length.
        
        Args:
            length (int): Length of the string to be generated.
            chars (str, optional): Characters to be used in generation. 
                                  Default: uppercase letters, lowercase letters and digits.
        
        Returns:
            str: Random string with the specified length.
        """
        return ''.join(random.choices(chars, k=length))

    @staticmethod
    def datetime(custom_tz=None):
        """
        Returns the current date and time.
        
        Args:
            custom_tz (int, optional): Timezone offset in hours. 
                                      If None, uses São Paulo timezone.
        
        Returns:
            datetime: Datetime object with the current date and time.
        """
        if custom_tz is not None:
            now = datetime.now()
            now = now + timedelta(hours=custom_tz)
            return now
        else:
            tz = pytz.timezone("America/Sao_Paulo") 
            return datetime.now(tz)
        
    @staticmethod
    def dateCompare(date1, date2):
        """
        Compares two dates and returns the comparison result.
        
        Args:
            date1 (datetime): First date to be compared.
            date2 (datetime): Second date to be compared.
        
        Returns:
            int: 1 if date1 > date2, -1 if date1 < date2, 0 if date1 == date2.
        
        Raises:
            TypeError: If date1 or date2 are not datetime objects.
        """
        if not isinstance(date1, datetime) or not isinstance(date2, datetime):
            raise TypeError("date1 and date2 must be datetime objects")
        if date1 > date2:
            return 1
        elif date1 < date2:
            return -1
        else:
            return 0

    @staticmethod
    def unitToSeconds(value, unit):
        """
        Converts a value from a time unit to seconds.
        
        Args:
            value (int|float): Value to be converted.
            unit (str): Time unit. Options: 'seconds', 'minutes', 'hours', 
                       'days', 'weeks', 'months', 'years'.
        
        Returns:
            int|float: Value converted to seconds.
        
        Raises:
            ValueError: If the unit is not one of the valid options.
        """
        if unit == 'seconds':
            return value
        elif unit == 'minutes':
            return value * 60
        elif unit == 'hours':
            return value * 60 * 60
        elif unit == 'days':
            return value * 60 * 60 * 24
        elif unit == 'weeks':
            return value * 60 * 60 * 24 * 7
        elif unit == 'months':
            return value * 60 * 60 * 24 * 30
        elif unit == 'years':
            return value * 60 * 60 * 24 * 365
        else:
            raise ValueError("unit must be seconds, minutes, hours, days, weeks, months or years")
        
    @staticmethod
    def secondsToUnit(seconds, unit):
        """
        Converts a value in seconds to another time unit.
        
        Args:
            seconds (int|float): Value in seconds to be converted.
            unit (str): Target time unit. Options: 'seconds', 'minutes', 
                       'hours', 'days', 'weeks', 'months', 'years'.
        
        Returns:
            float: Value converted to the specified unit.
        
        Raises:
            ValueError: If the unit is not one of the valid options.
        """
        if unit == 'seconds':
            return seconds
        elif unit == 'minutes':
            return seconds / 60
        elif unit == 'hours':
            return seconds / 60 / 60
        elif unit == 'days':
            return seconds / 60 / 60 / 24
        elif unit == 'weeks':
            return seconds / 60 / 60 / 24 / 7
        elif unit == 'months':
            return seconds / 60 / 60 / 24 / 30
        elif unit == 'years':
            return seconds / 60 / 60 / 24 / 365
        else:
            raise ValueError("unit must be seconds, minutes, hours, days, weeks, months or years")
        
    @staticmethod
    def dateAdd(date, value, unit):
        """
        Adds a time value to a date.
        
        Args:
            date (datetime): Base date to add the value to.
            value (int|float): Value to be added.
            unit (str): Time unit. Options: 'seconds', 'minutes', 'hours', 
                       'days', 'weeks', 'months', 'years', 'datetime'.
                       If 'datetime', the value is treated as seconds directly.
        
        Returns:
            datetime: New date with the value added.
        
        Raises:
            TypeError: If date is not a datetime object.
        """
        if not isinstance(date, datetime):
            raise TypeError("date must be a datetime object")
        if unit == 'datetime':
            return date + timedelta(seconds=value)
        else:
            return date + timedelta(seconds=Paestro.unitToSeconds(value, unit))
        
    @staticmethod
    def secondsBetween(date1, date2):
        """
        Calculates the absolute difference in seconds between two dates.
        
        Args:
            date1 (datetime): First date.
            date2 (datetime): Second date.
        
        Returns:
            float: Absolute difference in seconds between the two dates.
        
        Raises:
            TypeError: If date1 or date2 are not datetime objects.
        """
        if not isinstance(date1, datetime) or not isinstance(date2, datetime):
            raise TypeError("date1 and date2 must be datetime objects")
        
        return abs((date2 - date1).total_seconds())

    @staticmethod
    def dateToJsDate(date):
        """
        Converts a datetime object to JavaScript-compatible format (ISO string).
        
        Args:
            date (datetime): Date to be converted.
        
        Returns:
            str|None: String in ISO format (with 'T' instead of space) or None 
                     if date is not a datetime object.
        """
        if not isinstance(date, datetime):
            return None
        return str(date).replace(' ', 'T')

    @staticmethod
    def fill_zeros(value, length):
        """
        Pads a value with leading zeros until it reaches the specified length.
        
        Args:
            value: Value to be padded (will be converted to string).
            length (int): Desired length of the resulting string.
        
        Returns:
            str: String padded with leading zeros.
        """
        return str(value).zfill(length)

    @staticmethod
    def randomize_list(list):
        """
        Randomly shuffles the elements of a list (modifies the original list).
        
        Args:
            list (list): List to be shuffled.
        
        Returns:
            list: The same list (shuffled) passed as parameter.
        """
        random.shuffle(list)
        return list

    @staticmethod
    def random_int(min, max):
        """
        Generates a random integer within a range.
        
        Args:
            min (int): Minimum value (inclusive).
            max (int): Maximum value (inclusive).
        
        Returns:
            int: Random integer between min and max (inclusive).
        """
        return random.randint(min, max)

    @staticmethod
    def seconds_to_duration(seconds):
        """
        Converts a value in seconds to a human-readable duration string in Portuguese.
        
        Args:
            seconds (int|float): Value in seconds to be converted.
        
        Returns:
            str: Formatted string with the duration (e.g., "2 dias, 3 horas e 15 minutos").
        """
        units = [
            (24 * 3600, "dia"),
            (3600, "hora"),
            (60, "minuto"),
            (1, "segundo"),
        ]
        result = []
        for divisor, unit in units:
            value, seconds = divmod(seconds, divisor)
            if value > 0:
                result.append(f"{value} {unit}{'s' if value > 1 else ''}")

        if len(result) > 1:
            return " e ".join([", ".join(result[:-1]), result[-1]])
        else:
            return result[0]
        
    @staticmethod
    def split_chunks(array, chunk_size=1):
        """
        Splits a list or string into chunks of the specified size.
        
        Args:
            array (list|str): List or string to be split.
            chunk_size (int, optional): Size of each chunk. Default: 1.
        
        Returns:
            list: List containing the chunks of the original array.
        """
        return [array[i:i+chunk_size] for i in range(0, len(array), chunk_size)]

    @staticmethod
    def random_choice(array):
        """
        Selects a random element from a list or string.
        
        Args:
            array (list|str): List or string from which to select an element.
        
        Returns:
            Random element from the array.
        """
        return random.choice(array)

    @staticmethod
    def string_pad_left(string, length, char=' '):
        """
        Pads a string to the left with a character until it reaches the specified length.
        
        Args:
            string (str): String to be padded.
            length (int): Desired length of the resulting string.
            char (str, optional): Character used for padding. Default: space (' ').
        
        Returns:
            str: String padded to the left.
        """
        return char * (length - len(string)) + string

    @staticmethod
    def string_pad_right(string, length, char=' '):
        """
        Pads a string to the right with a character until it reaches the specified length.
        
        Args:
            string (str): String to be padded.
            length (int): Desired length of the resulting string.
            char (str, optional): Character used for padding. Default: space (' ').
        
        Returns:
            str: String padded to the right.
        """
        return string + char * (length - len(string))

    @staticmethod
    def remove_duplicated_spaces(text):
        """
        Removes duplicated spaces from a text, keeping only one space between words.
        
        Args:
            text (str): Text to be processed.
        
        Returns:
            str: Text with duplicated spaces removed.
        """
        return ' '.join(text.split())

    @staticmethod
    def date_weekday(date):
        """
        Returns the weekday of a date (1=Monday, 2=Tuesday, ..., 7=Sunday).
        
        Args:
            date (datetime): Date from which to get the weekday.
        
        Returns:
            int: Weekday number (1-7, where 1 is Monday and 7 is Sunday).
        """
        return [1,2,3,4,5,6,0][date.weekday()]

    @staticmethod
    def datetime_set_time(datetime, time):
        """
        Sets the time of a datetime object while keeping the date.
        
        Args:
            datetime (datetime): Datetime object to be modified.
            time (str): Time string in 'HH:MM:SS' format.
        
        Returns:
            datetime: New datetime object with the time set and microseconds zeroed.
        """
        hours, minutes, seconds = time.split(':')
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        return datetime.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
    
    @staticmethod
    def msort(arr, key=None):
        """
        Sorts a list using the bubble sort algorithm.
        
        Args:
            arr (list): List to be sorted (will be modified).
            key (str|list|None, optional): Key(s) for sorting if arr contains dictionaries.
                                         If None, sorts elements directly.
                                         If list, sorts by multiple keys in order.
        
        Returns:
            list: The same sorted list (modified in-place).
        """
        def compare(a, b):
            if key is None:
                return a < b
            else:
                if type(key) == list:
                    for k in key:
                        if a[k] < b[k]:
                            return True
                        elif a[k] > b[k]:
                            return False
                    return False
                else:
                    return a[key] < b[key]
        
        while True:
            for i in range(len(arr)):
                if i == 0:
                    continue
                
                if (compare(arr[i], arr[i-1])):
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    break
            else:
                return arr
            
    @staticmethod
    def reduce_jpeg_quality(source_path, target_path, quality=100):
        """
        Reduces the quality of a JPEG image and saves it to a new file.
        
        Args:
            source_path (str): Path of the source JPEG file.
            target_path (str): Path where to save the image with reduced quality.
            quality (int, optional): Image quality (0-100). Default: 100.
        """
        im1 = Image.open(source_path)
        buffer = BytesIO()
        im1.save(buffer, "JPEG", quality=quality)
        with open(target_path, "wb") as handle:
            handle.write(buffer.getvalue())
            
    @staticmethod
    def file_to_base64(source_path):
        """
        Converts a file to base64 string.
        
        Args:
            source_path (str): Path of the file to be converted.
        
        Returns:
            str: Base64 string representing the file content.
        """
        with open(source_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
        
    @staticmethod
    def base64_to_file(base64_string, target_path):
        """
        Converts a base64 string to a file.
        
        Args:
            base64_string (str): Base64 string to be decoded.
            target_path (str): Path where to save the decoded file.
        """
        with open(target_path, "wb") as image_file:
            image_file.write(base64.b64decode(base64_string))
            
    @staticmethod
    def gzip_compress(string):
        """
        Compresses a string using gzip.
        
        Args:
            string (str): String to be compressed.
        
        Returns:
            bytes: Compressed data in gzip format.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(string, str):
            raise TypeError("Input needs to be a string")

        bytes_buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=bytes_buffer, mode='wb') as f:
            f.write(string.encode('utf-8'))
            
        compressed_bytes = bytes_buffer.getvalue()
        return compressed_bytes
    
    @staticmethod
    def gzip_decompress(compressed_bytes):
        """
        Decompresses gzip data to string.
        
        Args:
            compressed_bytes (bytes): Compressed data in gzip format.
        
        Returns:
            str: Decompressed string.
        
        Raises:
            TypeError: If the input is not bytes.
        """
        if not isinstance(compressed_bytes, bytes):
            raise TypeError("Input needs to be bytes")

        bytes_buffer = io.BytesIO(compressed_bytes)
        with gzip.GzipFile(fileobj=bytes_buffer, mode='rb') as f:
            decompressed_string = f.read().decode('utf-8')
        return decompressed_string
    
    @staticmethod
    def save_file_bytes(data, target_path):
        """
        Saves binary data to a file.
        
        Args:
            data (bytes): Binary data to be saved.
            target_path (str): File path where to save the data.
        """
        with open(target_path, "wb") as file:
            file.write(data)
            
    @staticmethod
    def read_file_bytes(source_path):
        """
        Reads the binary content of a file.
        
        Args:
            source_path (str): Path of the file to be read.
        
        Returns:
            bytes: Binary content of the file.
        """
        with open(source_path, "rb") as file:
            return file.read()