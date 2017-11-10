int hammingDistance(int x, int y) {
    
    int distance = 0;
    int z = x ^ y;
    while ( z != 0) {
        if (z % 2 == 1){
            distance++;
        }
        z = z / 2;
    }
    return distance;
}
