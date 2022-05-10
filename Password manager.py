class BasePasswordManager:
    """docstring for BasePasswordManager."""
    passwords = list()
    def __init__(self):
        self.developer = "raju"
    def old_passwords(self):
        self.old_passwords_list = self.passwords
        if len(self.old_passwords_list) > 0:
            self.current_password = self.old_passwords_list[-1]

    def get_password(self):
        self.old_passwords()
        if len(self.old_passwords_list) == 0:
            return "No password is there please set a password"
        return self.current_password

    def is_correct(self,string):
        if self.current_password:
            if string==self.current_password:
                return True
        return False
class passwordmanager(BasePasswordManager):
    def __init__(self):
        pass
    def set_password(self,new_password):
        if len(new_password)<6:
            print("minimum 6 characters is required for password")
        else:
            if len(self.passwords) > 0:
                newpasswprd_level = self.get_level(new_password)
                curpassword_level = self.get_level(self.passwords[-1])
                if newpasswprd_level >= curpassword_level:
                    self.passwords.append(new_password)
                    print("Password succesfully changed!")
                else:
                    print("Password not updated due to security reasons please enter a higher level strength password to update!")
            else:
                self.passwords.append(new_password)
                print("New Password succesfully Added!")

    def get_level(self,string):
        st = str(string)
        if len(st)<6:
            print("minimum 6 characters is required for password\n")
        if st.isdigit() or st.isnumeric() or st.isalpha():
            return 0
        elif st.isalnum():
            return 1
        else:
            return 2


password = input("Enter a Password:").strip()
obj = passwordmanager()
# obj.old_passwords()
# print(obj.get_password())
obj.set_password(password)
if obj.get_password()=="No password is there please set a password":
    print(obj.get_password())
    print("\nEnter a Password to set password:")
    password = input().strip()
    obj.set_password(password)
else:
    print(obj.get_password())
# print(obj.get_level("raju"))
# print(obj.get_password())
