public class Solution {
    public bool hasDuplicate(int[] nums) 
    {
        HashSet<int> lastValues = new HashSet<int>();
        
        for(int i = 0; i < nums.Length; i++)
        {
            if (lastValues.TryGetValue(nums[i], out int number))
            {
                return true;
            }
            else
            {
                lastValues.Add(nums[i]);
            }
        }

        return false;
    }
}