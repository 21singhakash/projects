#@akash_singh
#This is the main.py file responsible for calling the app_func functionality.
import app
import sys

def main():
    url = sys.argv[1]
    app.app_func(url)
if __name__ == '__main__':
    main()
