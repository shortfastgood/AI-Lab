/*
 * @(#)DamerauLevenshteinDistance.java 2023.1
 *
 * Copyright (c) 2023 by DPAEVD
 * All rights reserved
 */
package org.homedns.dpaevd.ai.lab.algorithm.openai;

/**
 * Generate by ChatGPT-4 using the commands:
 * <ol>
 *     <li>generate a good Java implementation of the Damerau-Levenshtein distance algorithm</li>
 *     <li>add inline comments to the generated code</li>
 * </ol>
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
public class DamerauLevenshteinDistance {

    public static void main(String[] args) {
        String str1 = "sitting";
        String str2 = "kitten";
        // Calculate and display the Damerau-Levenshtein distance between str1 and str2
        System.out.println("Damerau-Levenshtein distance: " + getDamerauLevenshteinDistance(str1, str2));
    }

    public static int getDamerauLevenshteinDistance(String str1, String str2) {
        int len1 = str1.length();
        int len2 = str2.length();

        // Initialize the dynamic programming table with dimensions (len1 + 1) x (len2 + 1)
        int[][] d = new int[len1 + 1][len2 + 1];

        // Fill the first row and column of the table with the index values
        for (int i = 0; i <= len1; i++) {
            d[i][0] = i;
        }
        for (int j = 0; j <= len2; j++) {
            d[0][j] = j;
        }

        // Iterate through each character in both strings
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                // Determine the cost of substitution (0 if characters are equal, 1 otherwise)
                int cost = (str1.charAt(i - 1) == str2.charAt(j - 1)) ? 0 : 1;

                // Calculate the minimum of the three possible operations: deletion, insertion, and substitution
                d[i][j] = Math.min(Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1), d[i - 1][j - 1] + cost);

                // Check for a transposition and update the table value if necessary
                if (i > 1 && j > 1 && str1.charAt(i - 1) == str2.charAt(j - 2) && str1.charAt(i - 2) == str2.charAt(j - 1)) {
                    d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + cost);
                }
            }
        }

        // Return the Damerau-Levenshtein distance, which is the value in the bottom-right corner of the table
        return d[len1][len2];
    }
}

