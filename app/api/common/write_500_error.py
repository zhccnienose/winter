from datetime import datetime


def write_500_error(file_name, message):
    with open(file_name, 'a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 当前时间
        f.write('\n')
        f.write(message)
        f.write("\n\n")
