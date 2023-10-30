moves=0

answer = []
def main():
    disks = int(input("Enter your number of disks:"))
    tower_of_hanoi(disks,"Start","Dest","A1","A2","A3")
    if moves >100:
        print("First 10 moves: ", answer[0:10], end= '\n\n')
        print("Last 10 moves:", answer[-10:])
    else:
        for i in range(len(answer)):
            print(answer[i])
            print("Total moves:", moves)
def tower_of_hanoi(disk, start,dest,a1,a2,a3):
    if disk ==1:
        move(disk,start,dest)
    elif disk >=2:
        start_to_a3(disk-1,start,dest,a1,a2,a3)
        move(disk,start,dest)
        a3_to_dest(disk-1,a3,a2,a1,dest)
def start_to_a3(disk,start,dest,a1,a2,a3):
    if disk==1:
        move(disk,start,dest)
        move(disk,dest,a1)
        move(disk,a1,a2)
        move(disk,a2,a3)
    elif disk >=2:
        start_to_a3(disk-1,start,dest,a1,a2,a3)
        move(disk,start,dest)
        move(disk,dest,a1)
        move(disk,a1,a2)
        a3_to_dest(disk-1,a3,a2,a1,dest)
        move(disk,a2,a3)
        dest_to_a3(disk-1,dest,a1,a2,a3)
def a3_to_dest(disk,a3,a2,a1,dest):
    if disk ==1:
        move(disk,a3,a2)
        move(disk,a2,a1)
        move(disk,a1,dest)
    elif disk >=2:
        a3_to_dest(disk-1,a3,a2,a1,dest)
        move(disk,a3,a2)
        move(disk,a2,a1)
        dest_to_a3(disk-1,dest,a1,a2,a3)
        move(disk,a1,dest)
        a3_to_dest(disk-1,a3,a2,a1,dest)
def dest_to_a3(disk,dest,a1,a2,a3):
    if disk ==1:
        move(disk,dest,a1)
        move(disk,a1,a2)
        move(disk,a2,a3)
    elif disk >=2:
        dest_to_a3(disk-1,dest,a1,a2,a3)
        move(disk,dest,a1)
        move(disk,a1,a2)
        a3_to_dest(disk-1,a3,a2,a1,dest)
        move(disk,a2,a3)
        dest_to_a3(disk-1,dest,a1,a2,a3)
def move(disk,start,dest):
    global moves
    moves+=1
    global answer
    ans =("Move "+ str(moves)+ ": Moves disk "+ str(disk)+ " from "+str(start)+ " to "+str(dest))
    answer.append(ans)
if __name__ =="__main__":
    main()
