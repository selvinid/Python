class EligiblityForMarriage():   
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
         