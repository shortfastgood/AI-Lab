/*
 * @(#)LevenshteinDistance.java 2023.1
 *
 * Copyright (c) 2023 by DPAEVD
 * All rights reserved
 */
package org.homedns.dpaevd.ai.lab.human;

import java.util.List;

/**
 * Implementation of the Levenshtein distance algorithm.
 *
 * <a href="https://en.wikipedia.org/wiki/Levenshtein_distance">Documentation by Wikipedia</a>
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
public interface LevenshteinDistance {

    /**
     * This method was translated from the Haskell implementation by ChatGPT
     * <pre>
     *  lDistance :: Eq a => [a] -> [a] -> Int
     *  lDistance [] t = length t -- If s is empty, the distance is the number of characters in t
     *  lDistance s [] = length s -- If t is empty, the distance is the number of characters in s
     *  lDistance (a : s') (b : t') =
     *    if a == b
     *      then lDistance s' t' -- If the first characters are the same, they can be ignored
     *        else
     *          1
     *            + minimum -- Otherwise try all three possible actions and select the best one
     *              [ lDistance (a : s') t', -- Character is inserted (b inserted)
     *                lDistance s' (b : t'), -- Character is deleted  (a deleted)
     *                lDistance s' t' -- Character is replaced (a replaced with b)
     *              ]
     * </pre>
     * @param s the original string (character sequence
     * @param t the target string (character sequence)
     * @return the Levenshtein distance between the two strings
     * @param <T> the type of the elements in the list
     */
    static <T> int lDistance(List<T> s, List<T> t) {
        if (s.isEmpty()) {
            return t.size();
        } else if (t.isEmpty()) {
            return s.size();
        } else {
            T a = s.get(0);
            T b = t.get(0);

            if (a.equals(b)) {
                return lDistance(s.subList(1, s.size()), t.subList(1, t.size()));
            } else {
                int insert = lDistance(s, t.subList(1, t.size()));
                int delete = lDistance(s.subList(1, s.size()), t);
                int replace = lDistance(s.subList(1, s.size()), t.subList(1, t.size()));

                return 1 + Math.min(insert, Math.min(delete, replace));
            }
        }
    }

    /**
     * Adaptation of the full matrix implementation for comparison tests.
     * @param s the original string
     * @param t the target string
     * @return the Levenshtein distance between the two strings.
     */
    static int levenshteinDistanceFromFullMatrix(String s, String t) {
        return levenshteinDistanceWithFullMatrix(s.toCharArray(), t.toCharArray());
    }

    /**
     * Adaptation of the Haskell translation to Java for comparison tests.
     * @param s the original string
     * @param t the target string
     * @return the Levenshtein distance between the two strings.
     */
    static int levenshteinDistanceFromHaskell(final String s, final String t) {
        List<Character> listS = s.chars().mapToObj(c -> (char) c).toList();
        List<Character> listT = t.chars().mapToObj(c -> (char) c).toList();
        return lDistance(listS, listT);
    }

    /**
     * Adaptation of the two matrix rows implementation for comparison tests.
     * @param s the original string
     * @param t the target string
     * @return the Levenshtein distance between the two strings.
     */
    static int levenshteinDistanceFromTwoMatrixRows(String s, String t) {
        return levenshteinDistanceWithTwoMatrixRows(s.toCharArray(), t.toCharArray());
    }

    /**
     * This method is described on Wikipedia, copilot did generate the Java code starting from the name of the method
     * and the declaration of the arguments.
     * @param s the original string (character sequence)
     * @param t the target string (character sequence)
     * @return the Levenshtein distance between the two strings
     */
    static int levenshteinDistanceWithFullMatrix(final char[] s, final char[] t) {
        int[][] d = new int[s.length + 1][t.length + 1];

        for (int i = 0; i <= s.length; i++) {
            d[i][0] = i;
        }
        for (int j = 0; j <= t.length; j++) {
            d[0][j] = j;
        }
        for (int i = 1; i <= s.length; i++) {
            for (int j = 1; j <= t.length; j++) {
                int cost = (s[i - 1] == t[j - 1]) ? 0 : 1;
                d[i][j] = Math.min(Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1), d[i - 1][j - 1] + cost);
            }
        }
        return d[s.length][t.length];
    }

    /**
     * This method is described on Wikipedia, copilot did generate the Java code starting from the name of the method.
     *
     * @param s the original string (character sequence)
     * @param t the target string (character sequence)
     * @return the Levenshtein distance between the two strings.
     */
    static int levenshteinDistanceWithTwoMatrixRows(final char[] s, final char[] t) {
        int[] v0 = new int[t.length + 1];
        int[] v1 = new int[t.length + 1];

        for (int i = 0; i < v0.length; i++) {
            v0[i] = i;
        }
        for (int i = 0; i < s.length; i++) {
            v1[0] = i + 1;

            for (int j = 0; j < t.length; j++) {
                int cost = (s[i] == t[j]) ? 0 : 1;
                v1[j + 1] = Math.min(Math.min(v1[j] + 1, v0[j + 1] + 1), v0[j] + cost);
            }

            // optimization suggested by Intellij
            //
            System.arraycopy(v1, 0, v0, 0, v0.length);
            //
            //for (int j = 0; j < v0.length; j++) {
            //    v0[j] = v1[j];
            //}
        }
        return v1[t.length];
    }

}
