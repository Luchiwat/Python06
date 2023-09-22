#<18=เด็ก 19-45=หนุ่ม >46แก่

#รับค่า , ตรวจสอบอายุ , แสดงช้ือโปรแกรม

def showProgramName():
    print('---โปรแกรมตรวจสอบอายุ---')

def inputData():
    name = input('ชื้อ : ')
    age = int(input('อายุ : '))
    return name,age

def checkShowStatus(name,age) :
    if age <=18:
        print(f'คุณ {name} อายุ {age} ปี เป็นเด็ก')
    if age >=19 and age <=45:
        print(f'คุณ {name} อายุ {age} ปี เป็นคนหนุ่ม')
    else :
        print(f'คุณ {name} อายุ {age} ปี เป็นคนแก่')

print('---------------------------------------')
showProgramName()
print('---------------------------------------')
name,age = inputData()
print('---------------------------------------')
checkShowStatus(name,age)
print('---------------------------------------')
