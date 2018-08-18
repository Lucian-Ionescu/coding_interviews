#define function
def climb_stairs(steps, stairs):
   if stairs - steps >= 0:
       return stairs - steps
   return None


stairs_length = 10
step_poss = [1, 2]

print("stairs length:", stairs_length)
print("possible steps:", step_poss)

x = climb_stairs(step_poss[1], stairs_length)
x = climb_stairs(step_poss[0], stairs_length)
print(x)


#count possiblities to climb that stairs
print("# # # stairs recursive")


def climb_recursive(stairs):
    if stairs == 0:
        return 1
    elif stairs < 0:
        return 0

    return climb_recursive(stairs-1) + climb_stairs(stairs-2)


climb_recursive(10)












