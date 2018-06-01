from collections import defaultdict
import itertools
import sys
tri_list = []
tri = defaultdict(list)
square = defaultdict(list)
penta = defaultdict(list)
hexa = defaultdict(list)
hepta = defaultdict(list)
octa = defaultdict(list)

for n in range(1,10000):
  three = n * (n+1)/2
  if three >= 10000:
    break
  if three >= 1000:
    tri[str(three)[:2]].append(three)
    tri_list.append(three)

  four = n * n
  if 1000 <= four and four < 10000:
    square[str(four)[:2]].append(four)

  five = n*(3*n-1)/2
  if 1000 <= five and five < 10000:
    penta[str(five)[:2]].append(five)

  six = n*(2*n-1)
  if 1000 <= six and six < 10000:
    hexa[str(six)[:2]].append(six)

  seven = n*(5*n - 3)/2
  if 1000 <= seven and seven < 10000:
    hepta[str(seven)[:2]].append(seven)

  eight = n*(3*n - 2)
  if 1000 <= eight and eight < 10000:
    octa[str(eight)[:2]].append(eight)

print len(tri_list)
print tri_list

def Search(perm, idx, nums):
  if idx == 5 and str(nums[-1])[2:] == str(nums[0])[:2]:
    print nums
    print sum(nums)
    sys.exit(0)

  if idx == 5:
    return
  if perm[idx] == "4":
    possibilities = square[str(nums[-1])[2:]]
  elif perm[idx] == "5":
    possibilities = penta[str(nums[-1])[2:]]
  elif perm[idx] == "6":
    possibilities = hexa[str(nums[-1])[2:]]
  elif perm[idx] == "7":
    possibilities = hepta[str(nums[-1])[2:]]
  elif perm[idx] == "8":
    possibilities = octa[str(nums[-1])[2:]]

  for x in possibilities:
    if x not in nums:
      nums.append(x)
      Search(perm, idx+1, nums)
      del nums[-1]


for x in tri_list:
  for y in itertools.permutations("45678"):
    Search("".join(y), 0,  [x])


