#if cond true or false on dependt we have to check other ..

employeeage =62
isAlive =True

if employeeage>=60:
    print("employee is eli for pension...")
    if isAlive:
        print("pension can relese...")
    else:
        print("pension can not relese..")    
else:
    print("employee is not ele for pension..")        
    print("employee is ele for pensiong after ",(60-employeeage) , " years ")