class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string x = "";
    int i = 0, j = 0;
    while (i < word1.length() and j < word2.length())
    {
            x += word1[i]; i++;
            x += word2[j];
            j++;
    }
    while (i < word1.length())
    {
        x += word1[i];
        i++;
    }
    while (j < word2.length())
    {
        x += word2[j];
        j++;
    }
    return x;
    }
};
