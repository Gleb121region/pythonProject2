from amzqr import amzqr


def main():
    msg = 'https://github.com'
    amzqr.run(msg,
              version= 4 ,
              level='L',
              picture='шрек.gif',
              colorized=True)

if __name__ == '__main__':
    main()