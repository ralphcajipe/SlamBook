import peewee as p
db=p.SqliteDatabase('slambook.db')
class Slambook(p.Model):
    sbID=p.CharField()
    sbFName=p.CharField()
    sbNName=p.CharField()
    sbBDay=p.CharField()
    sbAge=p.CharField()
    sbGender=p.CharField()
    sbContact=p.CharField()
    sbEmailAdd=p.CharField()

    class Meta:
        database=db
        table_name='tblSlambook'
Slambook.create_table()
