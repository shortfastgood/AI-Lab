package org.homedns.dpaevd.ai.lab.deepseek;

/**
 * <p> The following command was given to DeepSeek 14b: "<i>Generate a good Java implementation of the Damerau-Levenshtein distance algorithm. add inline comments to the generated code. Bee syntetic and avoid long thinking.</i>"
 * 
 * <p> The following paragraphs contains the ansver of DeepSeek:
 *
 * </p> Okay, I need to generate a good Java implementation of the Damerau-Levenshtein distance algorithm with inline comments. Let me think about how to approach this.
 * First, I should understand what Damerau-Levenshtein is. It's an edit distance that allows for transpositions, which means swapping adjacent characters. The Levenshtein distance includes insertions, deletions, and substitutions but not swaps. So I need to extend that by adding the capability to handle transpositions.
 *
 * <p>I'll start by creating a function called damerauLevenshteinDistance that takes two strings as input: str1 and str2.
 *
 * <p>The first thing I should do is check if either string is null. If so, return -1 or throw an exception. Wait, in the given code example, it returns 0 in such cases. Hmm, maybe it's better to handle nulls by returning 0 as a default since edit distance between null and something might not be meaningful.
 *
 * <p>Next, I'll get the lengths of both strings. Let len1 = str1.length() and len2 = str2.length(). If either length is zero, return the other string's length because that would represent the number of insertions or deletions needed.
 *
 * <p>I should pre-allocate a 2D array to store intermediate results for dynamic programming. The size will be (len1 + 1) by (len2 + 1). This is standard in DP approaches for edit distance.
 *
 * <p>Then, I'll initialize the first row and column of the matrix. The first row represents the cost when one string is empty, so it's filled with values from 0 to len2. Similarly, the first column is filled with 0 to len1 because that's the number of insertions needed.
 *
 * <p>Now comes the core part: filling in the DP table. For each character i in str1 and j in str2:
 *
 * <p>If characters at i-1 and j-1 are the same, the cost is the same as dp[i-1][j-1], no edit needed.
 * Otherwise, consider three operations:
 * <ol><li>Substitution: dp[i-1][j-1] + 1</li>
 * <li>Insertion: dp[i][j-1] + 1</li>
 * <li>Deletion: dp[i-1][j] + 1</li></ol>
 * <p>Take the minimum of these three.
 * But wait, Damerau-Levenshtein adds transpositions. So for adjacent characters where swapping would make them match, I need to calculate that cost as well and compare it with the current minimum.
 *
 * <p>So, if i > 1 and j > 1 (to avoid index errors), check if str1[i-2] == str2[j-2] and str1[i-1] == str2[j-1]. If so, then a transposition would make them match. The cost in this case is dp[i-2][j-2] + 1 (since swapping is one edit operation).
 *
 * <p>I'll include this condition after calculating the substitution, insertion, deletion minimum and set the current dp[i][j] to be the smaller of these two options.
 *
 * <p>Finally, I'll return the value at dp[len1][len2], which represents the minimal edit distance.
 *
 * <p>Let me outline the steps in code:
 *
 * <ol><li>Handle null or empty strings.</li>
 * <li>Initialize the DP table.</li>
 * <li>Fill in the first row and column.</li>
 * <li>Iterate through each character pair, compute the possible edits, including transpositions.</li>
 * <li>Return the computed value.</li>
 * I should add inline comments to explain each step clearly. Now, I'll write the code accordingly, making sure it's efficient and handles all edge cases.
 *
 * May 2025: The locally generated code did not compile, so I had to fix it.
 */
public interface DamerauLevenshteinDistance {

    static int damerauLevenshteinDistance(String str1, String str2) {
        // Check for null or empty strings
        if (str1 == null || str2 == null) return 0;
        
        int len1 = str1.length();
        int len2 = str2.length();
        
        // If either string is empty, distance is the length of the other string
        if (len1 == 0 || len2 == 0) {
            return Math.abs(len1 - len2);
        }

        // Create a DP table with dimensions (len1+1) x (len2+1)
        int[][] dp = new int[len1 + 1][len2 + 1];

        // Initialize the first row and column
        for (int i = 0; i <= len1; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= len2; j++) {
            dp[0][j] = j;
        }

        // Fill the DP table
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                    dp[i][j] = dp[i-1][j-1]; // No edit needed
                } else {
                    int substitutionCost = dp[i-1][j-1] + 1;
                    int insertionCost = dp[i][j-1] + 1;
                    int deletionCost = dp[i-1][j] + 1;

                    // Consider transposition if applicable
                    int min = Math.min(
                            Math.min(insertionCost, deletionCost),
                            substitutionCost
                    );
                    if (i > 1 && j > 1) {
                        if (str1.charAt(i - 2) == str2.charAt(j - 2) && 
                            str1.charAt(i - 1) == str2.charAt(j - 1)) {
                            dp[i][j] = Math.min(
                                Math.min(insertionCost, deletionCost),
                                Math.min(substitutionCost, dp[i-2][j-2] + 1)
                            );
                        } else {
                            dp[i][j] = min;
                        }
                    } else {
                        dp[i][j] = min;
                    }
                }
            }
        }

        return dp[len1][len2];
    }   
}
