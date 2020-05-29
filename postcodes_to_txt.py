def range_include_end(start, end):
  return range(start, end+1)

postcodes = [
[*range_include_end(2311,2312)], 
[*range_include_end(2328,2411)], 
[*range_include_end(2420,2490)], 
[*range_include_end(2536,2551)], 
[*range_include_end(2575,2594)], 
[*range_include_end(2618,2739)], 
[*range_include_end(2787,2899)], 
[*range_include_end(4124,4125)], 
4133, 
4211, 
[*range_include_end(4270,4272)], 
4275, 
4280, 
4285, 
4287, 
[*range_include_end(4307,4499)], 
4510, 
4512, 
[*range_include_end(4515,4519)], 
[*range_include_end(4522,4899)], 
3139, 
[*range_include_end(3211,3334)], 
[*range_include_end(3340,3424)], 
[*range_include_end(3430,3649)], 
[*range_include_end(3658,3749)], 
3753, 
3756, 
3758, 
3762, 
3764, 
[*range_include_end(3778,3781)], 
3783, 
3797, 
3799, 
[*range_include_end(3810,3909)], 
[*range_include_end(3921,3925)], 
[*range_include_end(3945,3974)], 
3979, 
[*range_include_end(3981,3996)], 
[*range_include_end(6041,6044)], 
[*range_include_end(6055,6056)], 
6069, 
6076, 
[*range_include_end(6083,6084)], 
6111, 
[*range_include_end(6121,6126)], 
[*range_include_end(6200,6799)]
]

postcodes_flat = []
for item in postcodes:
  if isinstance(item, int):
    postcodes_flat.append(item)
  else:
    for range_include_end in item:
        postcodes_flat.append(range_include_end)

with open('postcodes.txt', 'w') as file:
    file.write(str(postcodes_flat).strip())