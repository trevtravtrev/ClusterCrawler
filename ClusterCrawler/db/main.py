from database import Database

def main():
    try:
        db = Database('/media/pi/"Samsung USB"/database.db')

    except Exception as e:
        print(f'main error: {e}')

if __name__ == '__main__':
    main()
