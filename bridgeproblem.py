MAX_GROUP_SIZE = int(input())
PEOPLE_SIZE = int(input())
persons = {}
for i in range(PEOPLE_SIZE):
   name = input()
   num = int(input())
   persons[name] = num


def BestGroup(startGroup, MAX_GROUP_SIZE, oneAhead):
   values = []
   if len(startGroup) < MAX_GROUP_SIZE:
       MAX_GROUP_SIZE = len(startGroup)
   for i in range(len(startGroup)-MAX_GROUP_SIZE+1):
       currentValue = 0
       nextBestGroup = []
       nextGroup = dict(startGroup)
       for ii in range(MAX_GROUP_SIZE):
           currentValue += startGroup[list(startGroup.keys())[i+ii]]
           nextGroup[list(startGroup.keys())[i+ii]] = -1
           nextBestGroup.append([list(startGroup.keys())[i+ii]])
       if oneAhead != True and MAX_GROUP_SIZE > 1:
           nextGroupReset = []
           newgroup = {}
           for person in list(nextGroup.keys()):
               if nextGroup[person] == -1:
                   if newgroup != {}:
                       nextGroupReset.append(newgroup)
                   newgroup = {}
               else:
                   newgroup[person] = nextGroup[person]
           nextGroupReset.append(newgroup)
           for Currentgroup in nextGroupReset:
               NewBestGroup, NewGroup = BestGroup(Currentgroup, MAX_GROUP_SIZE, True)
               if len(NewBestGroup) != MAX_GROUP_SIZE:
                   for person in NewBestGroup:
                       pass
                       currentValue -= int(nextGroup[person])
       values.append(currentValue)
   medianValue = sum(values)/len(values)
   peakValue = 0
   peakIndex = 0
   i = 0
   for value in values:

       if value > peakValue:
           peakValue = value
           peakIndex = i
       i += 1

   bestGroup = []
   for i in range(MAX_GROUP_SIZE):
       startGroup[list(startGroup.keys())[peakIndex + i]] = -1
       bestGroup.append(list(startGroup.keys())[peakIndex + i])
   groupReset = []
   newgroup = {}

   for person in startGroup:
       if startGroup[person] == -1:
           if newgroup != {}:
               groupReset.append(newgroup)
           newgroup = {}
       else:
           newgroup[person] = startGroup[person]
   groupReset.append(newgroup)

   return bestGroup, groupReset


groups = []
values = []
if PEOPLE_SIZE % MAX_GROUP_SIZE != 0:
   going = True
   NewGroups = [dict(persons)]
   firstAttempt = False
   while going:
       for group in NewGroups:
           if group == {}:
               NewGroups.remove(group)
       for group in NewGroups:
           CurrentBestGroup, NewGroup = BestGroup(group, MAX_GROUP_SIZE, firstAttempt)
           NewGroups.remove(group)
           NewGroups += NewGroup
           firstAttempt = True

           if CurrentBestGroup != []:
               groups.append(CurrentBestGroup)
       if NewGroups == []:
           going = False
else:
   for i in range(int(PEOPLE_SIZE / MAX_GROUP_SIZE)):
       group = []
       for ii in range(MAX_GROUP_SIZE):
           group.append(list(persons.keys())[ii + i*MAX_GROUP_SIZE])
       groups.append(group)
totalTime = 0
for group in groups:
   groupTime = 0
   for person in group:
       if persons[person] > groupTime:
           groupTime = persons[person]
   totalTime += groupTime

order = {}
for i in range(len(groups)):
   order[list(persons.keys()).index(groups[i][0])] = i
neworder = list(order.keys())
neworder.sort()

finalGroups = []
for i in neworder:
   finalGroups.append(groups[order[i]])

print("Total Time: " + str(totalTime))
for group in finalGroups:
   print(*group)
