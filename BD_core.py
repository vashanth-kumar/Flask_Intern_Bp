import pandas as pd
import csv
class DB:
    global m,indx
    m = []

    def create(self,name,bg,location,no):
        #global name, bg, location, no, k, m
        #k = int(input("Enter the no of donor's need to be added:"))
        #for i in range(k):
            a = []


            a.append(name)
            a.append(bg)
            a.append(location)
            a.append(no)
            print("Recorded updated succesfully")
            m.append(a)
            with open("new_file.csv", "a+") as my_csv:
                csvWriter = csv.writer(my_csv, delimiter=',')
                csvWriter.writerows(m)
            print("====================================================")
            return ("details Added Succesfully")

    #def create(self,name,bg,location,no):
    #def update(self,ch,old,new):






    def search(self,blood_type,loc):
        #print(m)

        file = open('new_file.csv', mode='r')
        csfile = csv.reader(file)
        a = []
        for i in csfile:
            # print(m[i][1])
            if blood_type == i[1] and loc==i[2]:
                a.append(i)
        file.close()
        return a



    def all_donor(self):

        print("======Total Donar======")
        # blood_type = input("Enter the blood group:")
        file = open('new_file.csv', mode='r')
        a=[]
        csfile = csv.reader(file)
        for i in csfile:
            a.append(i)
        return a
            #print(i)

        #print("====================================================")



    def delete(self):
        no = input("\nEnter the name:")

        file = open('new_file.csv', mode='r')
        csfile = csv.reader(file)
        a = []
        for i in csfile:
            # print(m[i][1])
            if no == i[1]:
                a.append(i)
                del i
        file.close()

        print(a)
        print("====================================================")
        return("delete Operation")



class user(DB):

    def login(self):
        global name, password
        name=str(input("    \n\tEnter the Username :"))
        password=input("\n\tEnter the password :")
        print("\n\tLogined")
    def signup(self):
        name1 = str(input("    \n\tEnter the Username :"))
        password1 = input("\n\tEnter the password :")
        if name1==name or password1  == password:
            print("\n\t signin succesfully")


    def log_out(self):
        return("Log Out")
    def user_details(self):
        return('succesfully submitted')

class admin(DB):
    def send(self):
        return "Alert sended"
   
    def request(self):
        return("request sended")
    def bd_view(self):
        #IT WILL SEARCH FOR THE DONOR
        obj_DB.search()
        obj_DB.create()
        obj_DB.update()
        obj_DB.delete()
        #login and logout
        obj_DB.login()
        obj_DB.log_out()

        return("bd values")






class update:
    def update_name(self,old,new):
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))
            for i in lst:
                if i[0] == old:
                    indx = lst.index(i) - 1




            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'Name'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "Name"] = new
            log.to_csv("new_file.csv", index=False)
            return ("update Succesfulluy!")

    def update_bloodgroup(self,old,new):

        file = open('new_file.csv', mode='r')
        lst = list(csv.reader(file))


        for i in lst:
            if i[0] == old:
                indx = lst.index(i) - 1


        df = pd.read_csv("new_file.csv")
        df.loc[indx, 'blood_grp'] = new
        df.to_csv("new_file.csv", index=False)
        log = pd.read_csv("new_file.csv")
        log.loc[indx, "blood_grp"] = new
        log.to_csv("new_file.csv", index=False)
        print("=====Details Updated=====")

    def update_location(self, old, new):
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))


            for i in lst:
                if i[0] == old:

                    indx = lst.index(i) - 1



            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'location'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "location"] = new
            log.to_csv("new_file.csv", index=False)

    def update_no(self, old, new):
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))


            for i in lst:
                if i[0] == old:

                    indx = lst.index(i) - 1


            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'no'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "no"] = new
            log.to_csv("new_file.csv", index=False)
            print("=====Details Updated=====")



obj_DB=admin()