#binary search
import array
def binarysearch(a,l,h,x):
	if (h>=l):
		mid=(l+h)//2
		if a[mid]==x:
			return mid
		elif a[mid]>x:
			return binarysearch(a,l,mid-1,x)
		else:
			return binarysearch(a,mid+1,h,x)
	else:
		return 1
arr=[]
n=int(input("Enter the size of array"))
for i in range(n):
        y=int(input("Enter the element"))
        arr.append(y)
print(arr)
x=int(input("enter the elment to search"))
result=binarysearch(arr,0,len(arr)-1,x)
if result!=1:
	print("Element {} is present at index {}".format(x,result))
else:
	print("Elment is not present")
