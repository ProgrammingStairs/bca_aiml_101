# How to achieve functionality of switch control statement in python
# 1. if elif
# 2. match
# 3. dictionary

num = 7;
match num:
    case 1 | 7 : print("Week End");
    case 2 | 3 | 4 | 5 | 6 : print("Week Days");
    case _ : print("Invalid statement");
 
