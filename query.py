from model import Slambook as s
import peewee as p
db=p.SqliteDatabase('slambook.db')

def insertSlambook(_sbid,_sblfname,_sbnname,_sbbday,_sbpage,_sbgender,_sbcontact,_sbemailadd):
    x=e.insert({s.sbID:_sbid,s.sbFName:_sbfname,s.sbNName:_sbnname,
    s.sbBDay:_sbbday,s.sbAge:_sbage,s.sbGender:_sbgender,e.sbContact:_sbcontact,s.EmailAdd:_empemailadd})
    y=x.execute()
    print('{} record has been added!\n'.format(y))
    viewSlambook()

def deletequery(id):
    x=slambook.delete().where(s.sbID==id)
    n=x.execute()
    print(n,'record deleted!')
    viewSlambook()

def updateSlambook():
    viewSlambook()
    id=input('Slambook ID:')

    _sbfname=input('Fullname: ')
    _sbnname=input('Nickname: ')
    _sbbday=input('Birthday: ')
    _sbage=input('Age: ')
    _sbgender=input('Gender: ')
    _sbcontact=input('Contact: ')
    _sbemailadd=input('EmailAddress: ')
    x=s.update({s.sbFName:_empfname,s.sbNName:_empnname,
    s.sbBDay:_empbday,s.sbAge:_empage,s.sbGender:_sbgender,s.empContact:_sbcontact,e.sbEmailAdd:_empemailadd}).where(s.sbFName==fname)
    y=x.execute()
    print('{} record has been updated!\n'.format(y))
    viewSlambook()

def viewSlambook():
    sb=s.select()
    print('{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}'.
    format('ID','FullName','NickName','Birthday','Age','Gender','Contact','EmailAddress'))
    print('-'*80)
    for sl in sb:
        print('{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}'.
        format(sl.FName,sl.empNName,
        sl.empFName,sl.empNName,sl.empBDay,
        sl.empEmailAdd))
    ctr=len(sb)
    print('Total No of Records: ',ctr)

def searchSlambook():
    id=input('Slambook ID: ')
    sb=s.select().where(s.sbID.startswith(id))
    print('{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}'.
    format('ID',FullName','NickName','Birthday','Age','Gender','Contact','EmailAddress'))
    print('-'*80)
    for sl in sb:
        print('{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}'.
        format(sl.FName,sl.empNName,
        sl.empFName,em.empNName,sl.empBDay,
        sl.empEmailAdd))
    ctr=len(sb)
    print('Total No of Records: ',ctr)
