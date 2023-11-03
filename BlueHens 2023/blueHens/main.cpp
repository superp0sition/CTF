#include <iostream>

int main() {
    int reg = 0;
    int cnt = 0;

Line1:
    reg = 5;        // 1
    reg *= 3;       // 2
    reg += 2;       // 3
    reg *= 5;       // 4
    if (cnt != 0)   // 5
        reg -= 1;   // 6
    printf("%c", reg);  // 7
    if (cnt != 0)   // 8
        goto Line23;// ARG: 15      // 9
    cnt += 4;       // 10
Line11:
    reg -= 4;       // 11
    cnt -= 1;       // 12
    if (cnt != 0)   // 13
        goto Line11;// ARG: 3       // 14
    cnt += 2;       // 15
Line16:
    reg -= 1;       // 16
    printf("%c", reg);  // 17
    cnt -= 1;       // 18
    if (cnt != 0)   // 19
        goto Line16; // ARG: 4       // 20
    cnt += 1;       // 21
    goto Line1; // ARG: 1;          // 22
Line23:
    cnt += 0;       // 23
    reg -= 14;      // 24
    printf("%c", reg);  // 25
    reg *= 2;       // 26
    reg -= 13;      // 27
    printf("%c", reg);  // 28
    cnt += 2;       // 29
Line30:
    reg = 13;       // 30
    reg *= 3;       // 31
    reg *= 2;       // 32
    printf("%c", reg);  // 33
    reg += 3;       // 34
    printf("%c", reg);  // 35
    reg -= 2;       // 36
    printf("%c", reg);  // 37
    reg += 1;       // 38
    printf("%c", reg);  // 39
    reg += 12;      // 40
    printf("%c", reg);  // 41
    reg -= 21;      // 42
    printf("%c", reg);  // 43
    cnt -= 1;       // 44
    if (cnt != 0)   // 45
        goto Line30; // ARG:16      // 46
    reg = 17;       // 47
    reg *= 3;       // 48
    reg *= 2;       // 49
    printf("%c", reg);  // 50
    reg = 8;        // 51
    reg *= 6;       // 52
    printf("%c", reg);  // 53
    reg *= 3;       // 54
    cnt += 6;       // 55
Line56:
    reg -= 5;       // 56
    cnt -= 1;       // 57
    if (cnt != 0)   // 58
        goto Line56; // ARG: 3       // 59
    printf("%c", reg);  // 60
    cnt += 3;       // 61
Line62:
    reg -= 7;       // 62
    cnt -= 1;       // 63
    if (cnt != 0)   // 64
        goto Line62; // ARG: 3       // 65
    reg += 2;       // 66
    printf("%c", reg);  // 67
    cnt += 3;       // 68
Line69:
    reg -= 9;       // 69
    cnt -= 1;       // 70
    if (cnt != 0)   // 71
        goto Line69; // ARG: 3       // 72
    printf("%c", reg);  // 73
    cnt += 3;       // 74
Line75:
    reg -= 6;       // 75
    cnt -= 1;       // 76
    if (cnt != 0)   // 77
        goto Line75; // ARG: 3       // 78
    reg += 1;       // 79
    printf("%c", reg);  // 80
    reg *= 2;       // 81
    reg += 6;       // 82
    printf("%c", reg);  // 83
    cnt += 8;       // 84
Line85:
    reg -= 7;       // 85
    cnt -= 1;       // 86
    if (cnt != 0)   // 87
        goto Line85; // ARG: 3       // 88
    printf("%c", reg);  // 89
    reg *= 2;       // 90
    reg += 15;      // 91
    printf("%c", reg);  // 92
    cnt += 2;       // 93
Line94:
    reg -= 11;      // 94
    cnt -= 1;       // 95
    if (cnt != 0)   // 96
        goto Line94; // ARG: 3   // 97
    printf("%c", reg);  // 98
    reg += 17;      // 99
    printf("%c", reg);  // 100
    cnt += 7;       // 101
Line102:
    reg -= 9;       // 102
    cnt -= 1;       // 103
    if (cnt != 0)   // 104
        goto Line102; // ARG: 3   // 105
    printf("%c", reg);  // 106
    reg *= 3;       // 107
    cnt += 4;       // 108
Line109:
    reg -= 7;       // 109
    cnt -= 1;       // 110
    if (cnt != 0)   // 111
        goto Line109; // ARG: 3   // 112
    printf("%c", reg);  // 113


}

