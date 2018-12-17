from lndynamic import LNDynamic

with open(r"/home/hme/commands.txt") as hpass:
    lines = hpass.readlines()
api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))

name = 'user'
number_of_vm=input("Nbr_of_vm ? ")
for i in range(1, int(number_of_vm)+1):
    vm_name = name + str(i)
    api.request("vm", "create",
                {'hostname': vm_name, 'plan_id': 4, 'region': 'roubaix', 'image_id': 85048,
                 'storage': 70})
