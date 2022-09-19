import csv
import os
import sys
from settings.config import BASE_DIR


class CsvHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_line(self, line_num):
        try:
            with open(self.file_path, "r", encoding='gbk') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                datas = [line for index, line in enumerate(csv_reader) if index + 1 == line_num][0]
            return datas
        except Exception as e:
            sys.exit(f'errors：读取{self.file_path}文件失败 {e}')

    def read_lines(self, from_line, to_line):
        try:
            datas = []
            with open(self.file_path, "r", encoding='gbk') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                for index, line in enumerate(csv_reader):
                    if from_line <= index + 1 <= to_line:
                        datas.append(line)
            return datas
        except Exception as e:
            sys.exit(f'errors：读取{self.file_path}文件失败 {e}')

    def read_all(self):
        with open(self.file_path, "r", encoding='gbk') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            datas = [line for line in csv_reader]
        return datas

    def get_test_cases(self):
        test_cases = []
        all_cases_data = self.read_all()
        for cases_data in all_cases_data:
            case = {}
            case['search_world'] = cases_data['输入搜索数据']
            case['expect_data'] = cases_data['预期结果']
            test_cases.append(case)
        return test_cases


file_path = os.path.join(BASE_DIR, 'data', 'data.csv')
csv_handler = CsvHandler(file_path)

if __name__ == '__main__':
    file_path = os.path.join(BASE_DIR, 'data', 'data.csv')
    csv_handler = CsvHandler(file_path)
    # print(csv_handler.read_all())
    print(csv_handler.get_test_cases())
    # print(csv_handler.read_line(1))
    # print(csv_handler.read_line(2))
    # print(csv_handler.read_line(3))
    # print(csv_handler.read_line(4))
    # print(csv_handler.read_lines(2,3))
