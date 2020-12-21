def checkmove(x,y,xnew,ynew,type):
    if xnew == x and ynew==x or x<1 or x>8 or y < 1 or y > 8 or xnew <1 or xnew >8 or ynew<1 or ynew>8:
        return False
    if type == "fou":
        if ynew-y == xnew-x:
            return True
    elif type == "cavalier":
        if (abs(xnew-x) == 2 and abs(ynew-y)==1) or (abs(ynew-y)==2 and abs(xnew-x)==1):
            return True
    elif type == "tour":
        if xnew == x or ynew == y:
            return True
    return False

# print(checkmove(1,1,1,1,"fou")) #should print False
# print(checkmove(1,1,5,1,"tour"))#should print True
# print(checkmove(0,1,4,3,"tour"))#should print False
# print(checkmove(1,1,3,3,"fou"))#should print True
# print(checkmove(2,2,4,3,"cavalier"))#should print True
# print(checkmove(2,2,4,4,"cavalier")) #should print False
# print(checkmove(4,5,1,2,"fou"))#should print True
