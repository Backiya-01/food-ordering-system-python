from User import User
class UserManager:
    __Users=[]
    @classmethod
    def AddUser(cls,userObj):
        if isinstance(userObj,User):
            cls.__Users.append(userObj)
        else:
            print("Invalid User")
    @classmethod
    def FindUser(cls,mailid,pwd):
        for user in cls.__Users:
            if user.mailid==mailid and user.password==pwd:
                return user
        return None
            