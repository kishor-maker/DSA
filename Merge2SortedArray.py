arr1=[3,6,8,9]
arr2=[4,5,6,7]
merge=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
        merge.append(arr1[i])
        i+=1
    else:
        merge.append(arr2[j])
        j+=1
print(merge)

---

## 💡 Core Logic — Two Pointer Technique
1. Create two pointers `i` and `j` starting at index `0` for both arrays.  
2. Compare `arr1[i]` and `arr2[j]`.  
   - Take the **smaller element**, add it to `merged`, and move that pointer forward.  
3. Repeat until one array finishes.  
4. Append remaining elements from the unfinished array.  
5. ✅ Result is a fully merged sorted array.

---

## 📝 Algorithm
1. Initialize an empty array `merge` to store the merged elements.
2. Use two pointers `i` and `j` to track the current index of `arr1` and `arr2`.
3. Compare elements at these pointers and append the smaller one to `merge`.
4. Move the pointer forward in the array from which the element was taken.
5. If one array is exhausted, append the remaining elements of the other array.
6. Return the merged array.