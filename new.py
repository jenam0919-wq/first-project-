class student:
    collage_name ="nit mjgyofd66iige"

    def __init__(self,name,mark):
        self.name = name
        self.mark =mark

    def get_avg(self):
        sum=0
        for val in self.mark:
            sum+= val
            print("hi", self.name ,"your get_avg score is : "sum/3)
       

   

s1 =student("manoj",[56,45,25])
s1.get_avg()

print(student.collage_name)