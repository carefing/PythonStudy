"""
read utf-8 file

'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）

关键字 with 在不需要访问文件后将其关闭，这样我们不用调用close()来关闭文件
"""

def main():
    file = 'test_file/poetry.txt'
    try:
        with open(file, 'r', encoding='utf-8') as f:
            print(f.read())
            # print(f.read().rstrip())
        print('***************************')
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')
                # print(line.rstrip())
            print()
        print('***************************')
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                print(line, end='')
                # print(line.rstrip())
    except FileNotFoundError:
        print('cannot find file:', file)
    except LookupError:
        print('given unknown encode')
    except UnicodeDecodeError:
        print('decode error')

if __name__ == '__main__':
    main()