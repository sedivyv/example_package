from .internal_sal.py import load_data_file
from .internal_sal.py import count_average_salary

def sedivyvsalstat(input_path: str, year1: int, year2: int) -> float:
    avg1 = count_average_salary(load_data_file(input_path, year1))
    avg2 = count_average_salary(load_data_file(input_path, year2))
    print(avg2-avg1)
    return(avg2 - avg1)