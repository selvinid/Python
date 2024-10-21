class EligiblityForMarriage():   
    def Eligible(gender,age):
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
        return eligible
         