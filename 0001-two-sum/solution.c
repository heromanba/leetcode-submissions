/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int* target_indice;
    target_indice = (int*) malloc(sizeof(int)*2);
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (*(nums+i) + *(nums+j) == target) {
                target_indice[0] = i;
                target_indice[1] = j;
            }
        }
    }
    return target_indice;
    
}
