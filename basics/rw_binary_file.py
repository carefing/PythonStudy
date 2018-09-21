"""
read utf-8 file
"""

def main():
    file_src = 'test_file/test_pic.png'
    file_dst = 'test_file/test_pic_copy.png'
    try:
        with open(file_src, 'rb') as fs_src:
            data = fs_src.read()
        with open(file_dst, 'wb') as fs_dst:
            fs_dst.write(data)
    except FileNotFoundError:
        print('cannot find file')
    except IOError:
        print('read or write error')
    print('Copy \'%s\' to \'%s\' finished' % (file_src, file_dst))

if __name__ == '__main__':
    main()