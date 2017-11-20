bool judgeCircle(char* moves) {
    int up_count = 0, down_count = 0, right_count = 0, left_count = 0, i = 0;
    while (true) {
        char character = *(moves + i);
        switch (character) {
            case 'U':
                up_count += 1;
                break;
            case 'D':
                down_count += 1;
                break;
            case 'R':
                right_count += 1;
                break;
            case 'L':
                left_count += 1;
                break;
            case '\0':
                goto Endwhile;
        }
        i++;
    }
    Endwhile: ;
    return (up_count == down_count) && (right_count == left_count) ? true : false ;
}
