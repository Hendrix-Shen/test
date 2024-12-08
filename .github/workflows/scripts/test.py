import os

def main():
    with open(os.environ['GITHUB_OUTPUT'], 'w') as f:
        l1 = '\n'.join(['123', '456'])
        l2 = '\n'.join(['111', '222'])
    
        f.write('test1<<EOF\n')
        f.write(f'{l1}\n')
        f.write('EOF\n')
    
        f.write('test2<<EOF\n')
        f.write(f'{l2}\n')
        f.write('EOF\n')


if __name__ == '__main__':
    main()