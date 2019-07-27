cache = {}
def HasProductSumSet(n, k):
  """Returns if the number n has a product-sum set of size k.
  """
  if n < k:
    return False
  if n == 0 and k == 0:
    return True
  if n < 1:
    return False
  if k <= 0:
		return False
  if k == 1:
    return True
  if (n, k) in cache:
    return cache[(n, k)]
  i = 2
  while i*i <= n:
    if n % i == 0:
      subnumber = n / i
      num_ones_required = n - subnumber - i
      if HasProductSumSet(subnumber, k - num_ones_required - 1):
        cache[(n, k)] = True
        return True
    i += 1
  cache[(n, k)] = False
  return False


MAX_N = 12000
curr_lowest = 2
answers = set()
for i in range(2, MAX_N+1):
  if i % 100 == 0:
    print i
  while not HasProductSumSet(curr_lowest, i):
    curr_lowest += 1
  answers.add(curr_lowest)

print sum(answers)
#144011661
#print answers
      
"""
k=2: 4 = 2 x 2 = 2 + 2
k=3: 6 = 1 x 2 x 3 = 1 + 2 + 3
k=4: 8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6
k=7: 12 = 1 x 1 x 1 x 1 x 1 x 3 x 4 = 1 + 1 + 1 + 1 + 1 + 3 + 4
k=8: 12 = 1 x 1 x 1 x 1 x 1 x 2 x 2 x 3 = 1 + 1 + 1 + 1 + 1 + 2 + 2 + 3
k=9: 15 = 1 x 1 x 1 x 1 x 1 x 1 x 1 x 3 x 5 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 3 + 5
k=10:16 = 1 x 1 x 1 x 1 x 1 x 1 x 1 x 1 x 4 x 4 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 4 + 4
k=11:16 = 1 x 1 x 1 x 1 x 1 x 1 x 1 x 1 x 2 x 2 x 4 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 4
k=12:16 = 1 x 1 x 1 x 1 x 1 x 1 x 1 x 1 x 2 x 2 x 2 x 2 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 2 + 2

Can I do 15 with a set of 9?
  If we divide by 3 then we need 7 1s to make up for the loss of 7. So can we do 5 with a set of 1? Yes.
  So we can do 15 with a set of 9.

Can I do 15 with a set of 10?
  If we divide by 3 then we need 7 1s to make up for the loss of 7. So can we do 5 with a set of 2?
  Can I do 5 with a set of 2?
    If we divide by 5 then we need 4 1s to make up for the loss of 4. So can we do 1 with a set of -3? No.
  So we cannot do 5 with a set of 2.
So we cannot do 15 with a set of 10.

Can I do 16 with a set of 10?
  If we divide by 2 then we need 6 1s to make up for the loss of 8. So can we do 8 with a set of 3?
  Can I do 8 with a set of 3?
    If we divide by 2 then we need 2 1s to make up for the loss. So can we do 4 with a set of 0? No.
    If we divide by 4 then we need 2 1s to make up for the loss. So can we do 2 with a set of 0? No. 
    So we cannot do 8 with a set of 3.
  So we cannot divide by 2.

  If we divide by 4 then we need 8 1s to make up for the loss. So can we do 4 with a set of 1? Yes.
  So yes we can do 16 with a set of 10.

Can I do 16 with a set of 11?
  If we divide by 2 then we need 6 1s to make up for the loss of 8. So can we do 8 with a set of 4? And the answer is yes.

Can I do 16 with a set of 12?
  If we divide by 2 then we need 6 1s to make up for the loss. So can we do 8 with a set of 5? And the answer is yes and we're done

12000, we have to solve: "Can I do X with a set of Y" where "0 <= Y <= X <= 6000". ~36 million operations is doable
"""
