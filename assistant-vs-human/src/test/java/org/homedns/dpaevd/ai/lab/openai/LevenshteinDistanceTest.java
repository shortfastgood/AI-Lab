package org.homedns.dpaevd.ai.lab.openai;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

/**
 * Test suite for LevenshteinDistance.
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
public class LevenshteinDistanceTest {

    @Test
    void testLevenshteinDistance() {
        assertEquals(0, LevenshteinDistance.calculate("kitten", "kitten"));
        assertEquals(1, LevenshteinDistance.calculate("kitten", "sitten"));
        assertEquals(1, LevenshteinDistance.calculate("kitten", "kittens"));
        assertEquals(3, LevenshteinDistance.calculate("Saturday", "Sunday"));
        assertEquals(7, LevenshteinDistance.calculate("abcdefg", "zyxwvuts"));
    }
}
