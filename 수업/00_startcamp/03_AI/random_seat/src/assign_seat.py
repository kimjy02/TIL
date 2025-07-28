import random
import os
import sys

# 명단 파일 경로 (txt 또는 xlsx)
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../output')

TXT_FILENAME = '4반 데이터 트랙 명단.txt'
XLSX_FILENAME = 'students.xlsx'


def read_names_from_txt(filepath):
    with open(filepath, encoding='utf-8') as f:
        names = [line.strip() for line in f if line.strip()]
    return names


def read_names_from_xlsx(filepath):
    try:
        import openpyxl
    except ImportError:
        print('openpyxl 패키지가 필요합니다. 설치 후 다시 실행하세요.')
        sys.exit(1)
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active
    names = [str(cell.value).strip() for cell in ws['A'] if cell.value]
    return names


def get_student_names():
    txt_path = os.path.join(DATA_DIR, TXT_FILENAME)
    xlsx_path = os.path.join(DATA_DIR, XLSX_FILENAME)
    if os.path.exists(txt_path):
        return read_names_from_txt(txt_path)
    elif os.path.exists(xlsx_path):
        return read_names_from_xlsx(xlsx_path)
    else:
        print(f'명단 파일이 없습니다. data 폴더에 "{TXT_FILENAME}" 또는 "{XLSX_FILENAME}"를 넣어주세요.')
        sys.exit(1)


def assign_seats(names):
    if len(names) != 28:
        print(f'명단 인원 수가 28명이 아닙니다. 현재 인원: {len(names)}')
        sys.exit(1)
    random.shuffle(names)
    seats = []
    # 4줄 × 6명 (2분단, 한 줄에 3명씩)
    for i in range(4):
        left = names[i*6:i*6+3]
        right = names[i*6+3:i*6+6]
        seats.append([left, right])
    # 마지막 줄 2명씩
    last_left = names[24:26]
    last_right = names[26:28]
    seats.append([last_left, last_right])
    return seats


def print_seat_table(seats):
    print("-"*49)
    print("{:^49}".format("칠판"))

    def make_row(left, right, is_last=False):
        # 각 분단 3자리, 빈 자리는 공백
        left_full = left + [''] * (3 - len(left))
        if is_last:
            # 오른쪽 분단: 첫번째 칸 비우고 두번째, 세번째에만 이름
            right_full = [''] + right + [''] * (2 - len(right))
        else:
            right_full = right + [''] * (3 - len(right))
        row = '| ' + ' | '.join(f'{name:^6}' for name in left_full) + ' |   | ' + ' | '.join(f'{name:^6}' for name in right_full) + ' |'
        return row

    # 상단 테두리
    print('+' + '---------'*3 + '+   +' + '---------'*3 + '+')
    for i, (left, right) in enumerate(seats):
        is_last = (i == 4)
        print(make_row(left, right, is_last=is_last))
        print('+' + '---------'*3 + '+   +' + '---------'*3 + '+')


def save_seat_table(seats, filename='seat_result.txt'):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
        for left, right in seats:
            left_str = ' '.join(f'{name:6}' for name in left)
            right_str = ' '.join(f'{name:6}' for name in right)
            f.write(f'{left_str} | {right_str}\n')


def main():
    names = get_student_names()
    seats = assign_seats(names)
    print('랜덤 자리 배치 결과:')
    print_seat_table(seats)
    save_seat_table(seats)
    print(f'결과가 {os.path.join(OUTPUT_DIR, "seat_result.txt")}에 저장되었습니다.')

if __name__ == '__main__':
    main()
