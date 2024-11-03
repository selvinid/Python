class MultipleFunctions():

    def Subfields():
        aiNamelist=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print('Sub-fields in AI are:')
        for i in aiNamelist:
            print(i)
	         
    def isOddEven():
        num = int(input("Enter a number :"))
        if(num%2==0):
            print(f'{num} is Even number')
        else:
            print(f'{num} is Odd number')

    def Eligible():
        gender = input('Your Gender :')
        age = int(input('Your Age :'))
        if("Male"==gender):
            if(age>=21 ):
                eligible= 'eligible'
            else:
                eligible= "notEligible"
        elif("Female"==gender):
            if(age>=18 ):
                eligible=  'eligible'
            else:
                eligible=  "notEligible"
        if ("eligible"==eligible):
            print("ELIGIBLE")
        else:
             print("NOT ELIGIBLE")
        
    def percentage():
        subject1 = int(input('Subject1= '))
        subject2 = int(input('Subject2= '))
        subject3 = int(input('Subject3= '))
        subject4 = int(input('Subject4= '))
        subject5 = int(input('Subject5= '))
        totalMarksObtained = subject1+subject2+subject3+subject4+subject5
        print("Total :",totalMarksObtained)
        total =500
        percent =(totalMarksObtained/total)*100
        print("Percentage : ",percent)
        
    def triangle():
        MultipleFunctions.area()
        MultipleFunctions.perimeter()
        
    def area():
        height =int(input("Height : "))
        breadth = int(input("Breadth : "))
        print("Area formula: (Height*Breadth)/2")
        area = (height*breadth)/2
        print("Area of Triangle:",area)
               
        
    def perimeter():
        height1 =int(input("Height1 : "))
        height2 =int(input("Height2 : "))
        breadth = int(input("Breadth : "))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = height1+height2+breadth
        print("Perimeter of Triangle:",perimeter)
        

    
    