class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int stepsInTotal = 0;
        int remainingCapacity = capacity;
        for (int i=0; i<plants.length; i++) {
            int p = plants[i];
            if (remainingCapacity >= p) {
                // capacity is enough for next plant, no need to go back
                remainingCapacity -= p;
            } else {
                // capacity is not enough for next plant, need to go back now
                stepsInTotal = stepsInTotal + i * 2;
                remainingCapacity = capacity - p;
            }
            // safe to go to next plant
            stepsInTotal += 1;
        }
        return stepsInTotal;
    }
}
