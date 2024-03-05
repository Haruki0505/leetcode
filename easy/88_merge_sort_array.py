nums1_1 = [1,2,3,0,0,0]
m_1 = 3
nums2_1 = [2,5,6]
n_1 = 3
nums1_2 = [1]
m_2 = 1
nums2_2 = []
n_2 = 0
nums1_3 = [0]
m_3 = 0
nums2_3 = [1]
n_3 = 1

# def merge_sort(nums1, m, nums2, n):
#   nums1[m:] = nums2
#   result = nums1.sort()
#   print(result)
def merge_sort(nums1, m, nums2, n):
  while n > 0:
    if m <= 0 or nums1[m-1] <= nums2[n-1]:
      nums1[m+n-1] = nums2[n-1]
      n -= 1
    else:
      nums1[m+n-1] = nums1[m-1]
      m -= 1

def main():
  merge_sort(nums1_1, m_1, nums2_1, n_1)
  merge_sort(nums1_2, m_2, nums2_2, n_2)
  merge_sort(nums1_3, m_3, nums2_3, n_3)

if __name__ == '__main__':
  main()