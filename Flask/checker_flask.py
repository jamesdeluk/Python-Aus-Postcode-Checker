import sys
# import json

def range_inclusive(start, end):
    return range(start, end+1)

postcodes = [
[*range_inclusive(2311, 2312)], [*range_inclusive(2328, 2411)], [*range_inclusive(2420, 2490)], [*range_inclusive(2536, 2551)], [*range_inclusive(2575, 2594)], [*range_inclusive(2618, 2739)], [*range_inclusive(2787, 2899)], [*range_inclusive(4124, 4125)], 4133, 4211, [*range_inclusive(4270, 4272)], 4275, 4280, 4285, 4287, [*range_inclusive(4307, 4499)], 4510, 4512, [*range_inclusive(4515, 4519)], [*range_inclusive(4522, 4899)], 3139, [*range_inclusive(3211, 3334)], [*range_inclusive(3340, 3424)], [*range_inclusive(3430, 3649)], [*range_inclusive(3658, 3749)], 3753, 3756, 3758, 3762, 3764, [*range_inclusive(3778, 3781)], 3783, 3797, 3799, [*range_inclusive(3810, 3909)], [*range_inclusive(3921, 3925)], [*range_inclusive(3945, 3974)], 3979, [*range_inclusive(3981, 3996)], [*range_inclusive(6041, 6044)], [*range_inclusive(6055, 6056)], 6069, 6076, [*range_inclusive(6083, 6084)], 6111, [*range_inclusive(6121, 6126)], [*range_inclusive(6200, 6799)]
]
# https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/work-holiday-417/specified-work
# Correct as of 30/05/2020

postcodes_flat = []
for item in postcodes:
    if isinstance(item, int):
        postcodes_flat.append(item)
    else:
        for range_inclusive in item:
            postcodes_flat.append(range_inclusive)

# file = 'Resources/au_postcodes.json'

# with open(file) as json_file:
#     data = json.load(json_file)

def check(postcode):
    # for region in data:
    #     if region['postcode'] == postcode:
    #         print(region['place_name'])
    if postcode in postcodes_flat:
        result = "^_^ Regional"
    else:
        result = "ㅠㅠ Not regional"
    return result