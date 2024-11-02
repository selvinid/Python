class FindPercent():
    def percentage():        
        subject1 = int(input('Subject1= '))
        subject2 = int(input('Subject2= '))
        subject3 = int(input('Subject3= '))
        subject4 = int(input('Subject4= '))
        subject5 = int(input('Subject5= '))
        
        totalmarksObtained = subject1+subject2+subject3+subject4+subject5
        total = 500
        print("Total : ",totalmarksObtained)
        percent = (totalmarksObtained/total)*100
        print("Percentage : ",percent) 
