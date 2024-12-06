#Activity Selection
from tabulate import tabulate
def activity_selection(activities, n):
    selected_activities = []
    activities.sort(key=lambda x: x[2])
    i = 0
    selected_activities.append(activities[i])
    for j in range(1, n):
        if activities[j][1] >= activities[i][2]:
            selected_activities.append(activities[j])
            i = j
    return selected_activities
n = 0
all_activities = []
all_process = True
while all_process:
    s = int(input("\nEnter the start time of the activity: "))
    f = int(input("Enter the finish time of the activity: "))
    n = n + 1
    all_activities.append([n, s, f])
    ch = input("\nDo you want to add another activity? (y/n): ")
    if ch.lower() == 'n':
        all_process = False
result = activity_selection(all_activities, len(all_activities))
print("\nMaximum number of activities that can be performed are: " + str(len(result)) + "\n")
print("Activities that can selected are as follows: ")
headers = ["Activity Number", "Start-Time", "End-Time"]
print(tabulate(result, headers=headers, tablefmt='grid'))
