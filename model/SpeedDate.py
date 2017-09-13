import peewee
from peewee import MySQLDatabase
import csv

db = MySQLDatabase('speed_dates', user='root', passwd='')


class SpeedDate(peewee.Model):
    # match - 0/1
    match = peewee.FloatField()

    # Partner 1

    # Attractive
    attr_1 = peewee.FloatField()
    # Interest
    shar_1 = peewee.FloatField()
    # Ambitious
    amb_1 = peewee.FloatField()
    # Fun
    fun_1 = peewee.FloatField()
    # Intelligent
    intel_1 = peewee.FloatField()
    # Sincere
    sinc_1 = peewee.FloatField()

    # Partner 2

    # Attractive
    attr_2 = peewee.FloatField()
    # Interest
    shar_2 = peewee.FloatField()
    # Ambitious
    amb_2 = peewee.FloatField()
    # Fun
    fun_2 = peewee.FloatField()
    # Intelligent
    intel_2 = peewee.FloatField()
    # Sincere
    sinc_2 = peewee.FloatField()

    # Partner 1 General

    # Attractive
    attr_3 = peewee.FloatField()
    # Interest
    shar_3 = peewee.FloatField()
    # Ambitious
    amb_3 = peewee.FloatField()
    # Fun
    fun_3 = peewee.FloatField()
    # Intelligent
    intel_3 = peewee.FloatField()
    # Sincere
    sinc_3 = peewee.FloatField()

    # Partner 2 General

    # Attractive
    attr_4 = peewee.FloatField()
    # Interest
    shar_4 = peewee.FloatField()
    # Ambitious
    amb_4 = peewee.FloatField()
    # Fun
    fun_4 = peewee.FloatField()
    # Intelligent
    intel_4 = peewee.FloatField()
    # Sincere
    sinc_4 = peewee.FloatField()

    class Meta:
        database = db

    @staticmethod
    def load_data():
        with open('speed_dating.csv', 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f)
            dates = list(reader)
        i = 0
        for d in dates[1:]:
            try:
                grades_A, grades_B = SpeedDate.get_grades(d, dates)
            except:
                pass

            """
            print("%s %s %s %s %s %s %s" % (d[12], d[98], d[99], d[100], d[101], d[102], d[103]))
            print(' '.join(grades_A))
            print("%s %s %s %s %s %s" % (d[69], d[70], d[71], d[72], d[73], d[74]))
            print(' '.join(grades_B))
            print("================================================================")
            """

            date = SpeedDate(match=d[12],
                             attr_1=d[98], sinc_1=d[99], intel_1=d[100], fun_1=d[101], amb_1=d[102], shar_1=d[103],
                             attr_2=grades_A[0], sinc_2=grades_A[1], intel_2=grades_A[2], fun_2=grades_A[3],
                             amb_2=grades_A[4], shar_2=grades_A[5],
                             attr_3=d[69], sinc_3=d[70], intel_3=d[71], fun_3=d[72], amb_3=d[73], shar_3=d[74],
                             attr_4=grades_B[0], sinc_4=grades_B[1], intel_4=grades_B[2], fun_4=grades_B[3],
                             amb_4=grades_B[4], shar_4=grades_B[5])
            # skip null values
            try:
                date.save()
            except:
                pass

    """
        Convert object of type Data to list.
    """

    @staticmethod
    def to_list(dt):
        list = []
        list.extend((dt.match, dt.attr_1, dt.shar_1, dt.amb_1, dt.fun_1, dt.intel_1, dt.sinc_1,
                     dt.attr_2, dt.shar_2, dt.amb_2, dt.fun_2, dt.intel_2, dt.sinc_2,
                     dt.attr_3, dt.shar_3, dt.amb_3, dt.fun_3, dt.intel_3, dt.sinc_3,
                     dt.attr_4, dt.shar_4, dt.amb_4, dt.fun_4, dt.intel_4, dt.sinc_4))
        return list

    @staticmethod
    def get_grades(d, dates):
        # row[11] = pid
        # row[10] = partner

        for row in dates:
            if row[0] == d[11] and row[1] == d[10] and row[10] == d[1] and row[11] == d[0]:
                return [row[98], row[99], row[100], row[101], row[102], row[103]], [row[69], row[70], row[71], row[72],
                                                                                    row[73], row[74]]


# if __name__ == "__main__":
#     SpeedDate.create_table()
#     SpeedDate.load_data()
