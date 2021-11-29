# Calender
Provides day of any given date and year
                                                                          
                                                                     LOGIC

Step-1: Year-1

Centuary &  Leap/Ordinary Year
        |                                          |
Centuary/4                             year/4
 
                
             
                       Quotient*2                  Year-Quotient*1

For Centuary,
100- 5
200-3
300-1
400-0

Step-2:  (Sum of Step1) / 7 = Remainder 


Step-3: Running months,

Sum of running months / 7 = Remainder 


Step-4: (Step2+Step3 odd days) / 7 = Remainder 

Days are as follows:

            0 - Sunday
            1 - Monday
            2 - Tuesday
            3 - Wednesday
            4 - Thursday
            5 - Friday
            6 - Saturday
















#Example: What was the day of the week on 16th July,1776 ?

Step-1: 1776-1=1775

                                                        1775


                    

                  1700                                                       75/4
          
        
         1600          100                                       18*2           (75-18)*1


          0             5                                         36      +        57       =  93/7  
                                                                                            =  2

Step-2: (0+5+2) / 7 = 0

Step-3: 16th July,1776
 
              January-31
              February-29
              March-31
              April-30
              May-31
              June-30
              July-16
                  198
                  = 198 / 7 = 2

Step-4: 0 + 2 = 2 (Tuesday) 
