package org.homedns.dpaevd.ai.lab.human;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Test suite for LevenshteinDistance.
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
class LevenshteinDistanceTest {

    @Test
    void levenshteinDistanceFromFullMatrixTest() {
        assertEquals(0, LevenshteinDistance.levenshteinDistanceFromFullMatrix("kitten", "kitten"));
        assertEquals(1, LevenshteinDistance.levenshteinDistanceFromFullMatrix("kitten", "sitten"));
        assertEquals(1, LevenshteinDistance.levenshteinDistanceFromFullMatrix("kitten", "kittens"));
        assertEquals(3, LevenshteinDistance.levenshteinDistanceFromFullMatrix("Saturday", "Sunday"));
        assertEquals(8, LevenshteinDistance.levenshteinDistanceFromFullMatrix("abcdefg", "zyxwvuts"));
    }

    @Test
    void levenshteinDistanceFromHaskellTest() {
        assertEquals(0, LevenshteinDistance.levenshteinDistanceFromHaskell("kitten", "kitten"));
        assertEquals(1, LevenshteinDistance.levenshteinDistanceFromHaskell("kitten", "sitten"));
        assertEquals(1, LevenshteinDistance.levenshteinDistanceFromHaskell("kitten", "kittens"));
        assertEquals(3, LevenshteinDistance.levenshteinDistanceFromHaskell("Saturday", "Sunday"));
        assertEquals(8, LevenshteinDistance.levenshteinDistanceFromHaskell("abcdefg", "zyxwvuts"));
    }

    @Test
    void levenshteinDistanceFromTwoMatrixRowTest() {
        assertEquals(0, LevenshteinDistance.levenshteinDistanceFromTwoMatrixRows("kitten", "kitten"));
        assertEquals(1, LevenshteinDistance.levenshteinDistanceFromTwoMatrixRows("kitten", "sitten"));
        assertEquals(1, LevenshteinDistance.levenshteinDistanceFromTwoMatrixRows("kitten", "kittens"));
        assertEquals(3, LevenshteinDistance.levenshteinDistanceFromTwoMatrixRows("Saturday", "Sunday"));
        assertEquals(8, LevenshteinDistance.levenshteinDistanceFromTwoMatrixRows("abcdefg", "zyxwvuts"));
    }
}