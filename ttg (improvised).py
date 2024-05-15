import random
import pymysql as pym

def get_subjects():
    maj_sub = []
    ext_sub = []

    ms = int(input("How many main subjects are there--"))
    f = input("Which is the first period--")
    fp = [f]

    for i in range(ms - 1):
        os = input("Enter Other Main Subjects--")
        maj_sub.append(os)

    esn = int(input("Enter Number of Extra Subjects--"))
    for i in range(esn):
        es = input("Enter Subject--")
        ext_sub.append(es)
    
    return maj_sub, ext_sub, fp

def generate_schedule(maj_sub, ext_sub, fp):
    days = []
    for _ in range(6):
        day_schedule = maj_sub[:]
        day_schedule.append(random.choice(maj_sub))
        day_schedule.append(random.choice(random.choice([maj_sub, fp])))
        day_schedule.append(random.choice(ext_sub))
        random.shuffle(day_schedule)
        days.append(fp + day_schedule[:7])
    return days

def insert_schedule_into_db(days, cursor, mycon):
    day_names = ["First Day", "Second Day", "Third Day", "Fourth Day", "Fifth Day", "Sixth Day"]
    for day_name, day_schedule in zip(day_names, days):
        val = "insert into time(Day, I, II, III, IV, V, VI, VII, VIII) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            day_name, *day_schedule)
        cursor.execute(val)
        mycon.commit()

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS time(
        Day CHAR(10),
        I CHAR(10),
        II CHAR(10),
        III CHAR(10),
        IV CHAR(10),
        V CHAR(10),
        VI CHAR(10),
        VII CHAR(10),
        VIII CHAR(10));''')

def main():
    mycon = pym.connect(host="localhost", user="root", password="123", database="okp")
    cursor = mycon.cursor()
    create_table(cursor)

    clas = int(input("Enter Class--"))
    maj_sub, ext_sub, fp = get_subjects()
    days = generate_schedule(maj_sub, ext_sub, fp)
    insert_schedule_into_db(days, cursor, mycon)

    mycon.close()

if __name__ == "__main__":
    main()
