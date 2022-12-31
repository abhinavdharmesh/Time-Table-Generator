import random
import pymysql as pym
fp=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]

############################.F.U.N.C.T.I.O.N._.O.N.E.##########################

def Senior_Class():

    #--------------------------.S.U.B.J.E.C.T.S.-----------------------------#
    
    maj_sub=[]
    ext_sub=[]
    yee=[maj_sub,fp]
    
    #------------------------.S.U.B.J.E.C.T._.I.N.P.U.T.---------------------#
    
    ms=int(input("How many main subjects are there--"))
    f=input("Which is the first period--")
    fp.append(f)
    for i in range(ms-1):
        os=input("Enter Other Main Subjects--")
        maj_sub.append(os)
   
    #------------------------------------------------------#
    esn=int(input("Enter Number of Extra Subjects--"))
    for i in range(esn):
        es=input("Enter Subject--")
        ext_sub.append(es)

    
    #---------------------------.F.I.R.S.T.D.A.Y.----------------------------#
        
    for i in maj_sub:
       l1.append(i)
    rcm=random.choice(maj_sub)
    l1.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l1.append(ryee)
    rem=random.choice(ext_sub)
    l1.append(rem)
    random.shuffle(l1)
    print(fp+l1)
   
    #-------------------------_.S.E.C.O.N.D._.D.A.Y._------------------------#
        
    for i in maj_sub:
       l2.append(i)
    rcm=random.choice(maj_sub)
    l2.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l2.append(ryee)
    rem=random.choice(ext_sub)
    l2.append(rem)
    random.shuffle(l2)
    print(fp+l2)
   
    #-------------------------_.T.H.I.R.D._.D.A.Y._--------------------------#
        
    for i in maj_sub:
       l3.append(i)
    rcm=random.choice(maj_sub)
    l3.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l3.append(ryee)
    rem=random.choice(ext_sub)
    l3.append(rem)
    random.shuffle(l3)
    print(fp+l3)
      
    #-------------------------_.F.O.U.R.T.H._.D.A.Y._------------------------#
        
    for i in maj_sub:
       l4.append(i)
    rcm=random.choice(maj_sub)
    l4.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l4.append(ryee)
    rem=random.choice(ext_sub)
    l4.append(rem)
    random.shuffle(l4)
    print(fp+l4)

     
    #-------------------------_.F.I.F.T.H._.D.A.Y._--------------------------#
        
    for i in maj_sub:
       l5.append(i)
    rcm=random.choice(maj_sub)
    l5.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l5.append(ryee)
    rem=random.choice(ext_sub)
    l5.append(rem)
    random.shuffle(l5)
    print(fp+l5)
    
    #-------------------------_.S.I.X.T.H._.D.A.Y._--------------------------#
        
    for i in maj_sub:
       l6.append(i)
    rcm=random.choice(maj_sub)
    l6.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l6.append(ryee)
    rem=random.choice(ext_sub)
    l6.append(rem)
    random.shuffle(l6)
    print(fp+l6)
#-----------------------------------------------------------------------------#
    
    #---------------------------------first_day-----------------------------------#

    val1="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("First Day",fp[0],l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6])
    cursor.execute(val1)
    mycon.commit()
    
    #---------------------------------second_day----------------------------------#
    
    val2="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Second Day",fp[0],l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6])
    cursor.execute(val2)
    mycon.commit()
    
    #---------------------------------third_day-----------------------------------#
    
    val3="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Third Day",fp[0],l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6])
    cursor.execute(val3)
    mycon.commit()
    
    #---------------------------------fourth_day----------------------------------#
    
    val4="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Fourth Day",fp[0],l4[0],l4[1],l4[2],l4[3],l4[4],l4[5],l4[6])
    cursor.execute(val4)
    mycon.commit()
    
    #---------------------------------fifth_day-----------------------------------#
    
    val5="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Fifth Day",fp[0],l5[0],l5[1],l5[2],l1[3],l5[4],l5[5],l5[6])
    cursor.execute(val5)
    mycon.commit()
    
    #---------------------------------sixth_day-----------------------------------#
    
    val6="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Sixth Day",fp[0],l6[0],l6[1],l6[2],l6[3],l6[4],l6[5],l6[6])
    cursor.execute(val6)
    mycon.commit()
    


###########################.F.U.N.C.T.I.O.N._.T.W.O.###########################

def Junior_Class():

    #--------------------------.S.U.B.J.E.C.T.S.-----------------------------#
    
    maj_sub=[]
    ext_sub=[]
    yee=[maj_sub,fp]
    
    #------------------------.S.U.B.J.E.C.T._.I.N.P.U.T.---------------------#
    
    ms=int(input("How many main subjects are there--"))
    f=input("Which is the first period--")
    fp.append(f)
    for i in range(ms-1):
        os=input("Enter Other Main Subjects--")
        maj_sub.append(os)
   
    #------------------------------------------------------#
    esn=int(input("Enter Number of Extra Subjects--"))
    for i in range(esn):
        es=input("Enter Subject--")
        ext_sub.append(es)

   #------------------------------------------------------------------------#

    
   #---------------------------.F.I.R.S.T.D.A.Y.----------------------------#
        
    for i in maj_sub:
       l1.append(i)
    rcm=random.choice(maj_sub)
    l1.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l1.append(ryee)
    rem=random.choice(ext_sub)
    l1.append(rem)
    random.shuffle(l1)
    print(fp+l1)
   
    #-------------------------_.S.E.C.O.N.D._.D.A.Y._------------------------#
        
    for i in maj_sub:
       l2.append(i)
    rcm=random.choice(maj_sub)
    l2.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l2.append(ryee)
    rem=random.choice(ext_sub)
    l2.append(rem)
    random.shuffle(l2)
    print(fp+l2)
   
    #-------------------------_.T.H.I.R.D._.D.A.Y._--------------------------#
        
    for i in maj_sub:
       l3.append(i)
    rcm=random.choice(maj_sub)
    l3.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l3.append(ryee)
    rem=random.choice(ext_sub)
    l3.append(rem)
    random.shuffle(l3)
    print(fp+l3)
      
    #-------------------------_.F.O.U.R.T.H._.D.A.Y._------------------------#
        
    for i in maj_sub:
       l4.append(i)
    rcm=random.choice(maj_sub)
    l4.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l4.append(ryee)
    rem=random.choice(ext_sub)
    l4.append(rem)
    random.shuffle(l4)
    print(fp+l4)

     
    #-------------------------_.F.I.F.T.H._.D.A.Y._--------------------------#
        
    for i in maj_sub:
       l5.append(i)
    rcm=random.choice(maj_sub)
    l5.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l5.append(ryee)
    rem=random.choice(ext_sub)
    l5.append(rem)
    random.shuffle(l5)
    print(fp+l5)
    
    #-------------------------_.S.I.X.T.H._.D.A.Y._--------------------------#
        
    for i in maj_sub:
       l6.append(i)
    rcm=random.choice(maj_sub)
    l6.append(rcm)
    rye=random.choice(yee)
    ryee=random.choice(rye)
    l6.append(ryee)
    rem=random.choice(ext_sub)
    l6.append(rem)
    random.shuffle(l6)
    print(fp+l6)

#-----------------------------------------------------------------------------#
    
    #---------------------------------first_day-----------------------------------#

    val1="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("First Day",fp[0],l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6])
    cursor.execute(val1)
    mycon.commit()
    
    #---------------------------------second_day----------------------------------#
    
    val2="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Second Day",fp[0],l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6])
    cursor.execute(val2)
    mycon.commit()
    
    #---------------------------------third_day-----------------------------------#
    
    val3="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Third Day",fp[0],l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6])
    cursor.execute(val3)
    mycon.commit()
    
    #---------------------------------fourth_day----------------------------------#
    
    val4="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Fourth Day",fp[0],l4[0],l4[1],l4[2],l4[3],l4[4],l4[5],l4[6])
    cursor.execute(val4)
    mycon.commit()
    
    #---------------------------------fifth_day-----------------------------------#
    
    val5="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Fifth Day",fp[0],l5[0],l5[1],l5[2],l1[3],l5[4],l5[5],l5[6])
    cursor.execute(val5)
    mycon.commit()
    
    #---------------------------------sixth_day-----------------------------------#
    
    val6="insert into time(Day,I,II,III,IV,V,VI,VII,VIII)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("Sixth Day",fp[0],l6[0],l6[1],l6[2],l6[3],l6[4],l6[5],l6[6])
    cursor.execute(val6)
    mycon.commit()
    

############################_.M.Y.S.Q.L._.C.O.D.E._###########################
    
mycon=pym.connect(host="localhost",user="root",password="123",database="okp")
cursor=mycon.cursor()
cursor.execute('''CREATE TABLE time(
        Day char(10) ,
        I char(10),
        II char(10),
        III char(10),
        IV char(10),
        V char(10),
        VI char(10),
        VII char(10),
        VIII char(10));''')

#-----------------------------------------------------------------------------#

while len(l1)>7:
    l1.pop()
while len(l2)>7:
    l2.pop()
while len(l3)>7:
    l3.pop()
while len(l4)>7:
    l4.pop()
while len(l5)>7:
    l5.pop()
while len(l6)>7:
    l6.pop()

############################_.M.A.I.N._.B.O.D.Y._##############################
clas=int(input("Enter Class--"))
if clas>8:
    Senior_Class()
elif clas<8:
    Junior_Class()
