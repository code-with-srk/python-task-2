


from MathOp.addOp import addValue
from MathOp.subOp import subValue
from MathOp.mulOp import mulValue
from MathOp.divOp import divValue




if __name__ =='__main__':
    print('this is main code')
    val1 = int(input('enter first number = '))
    val2 = int(input('enter second number = '))
    op = input('which math op you want to do ?')

    if op.lower() == 'add':
        a1 = addValue(val1 ,val2  )
        print(f'addition= {a1}')
      
    elif  op.lower() == 'sub':
        a2 = subValue(val1 - val2)
        print('substract',a2)

    elif  op.lower() == 'mul':
        a3 = mulValue(val1 * val2)
        print('multiplication',a3)

    elif  op.lower() == 'div':
        a4 = divValue(val1 / val2)
        print('division',a4)


    else:
        print('please choose correct operation ,add,sub,mul,div')