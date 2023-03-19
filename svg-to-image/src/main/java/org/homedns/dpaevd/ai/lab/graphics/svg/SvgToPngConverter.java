/*
 * @(#)SvgToPngConverter.java 2023.1
 *
 * Copyright (c) 2023 by DPAEVD
 * All rights reserved
 */
package org.homedns.dpaevd.ai.lab.graphics.svg;

import java.io.FileOutputStream;
import java.io.OutputStream;

import org.apache.batik.transcoder.TranscoderException;
import org.apache.batik.transcoder.TranscoderInput;
import org.apache.batik.transcoder.TranscoderOutput;
import org.apache.batik.transcoder.image.ImageTranscoder;
import org.apache.batik.transcoder.image.PNGTranscoder;


/**
 * ChatGPT:
 * <ul>
 *     <li><strong>EN</strong>: Generate a Java algorithm that loads an SVG file and transforms it into a PNG image.
 *     Please provide only the code, I don't need a description.</li>
 *
 *     <li><strong>IT</strong>: Genera un algoritmo in Java che carichi un file SVG e lo trasformi in un'immagine PNG.
 *     Per favore solo il codice, la descrizione non mi serve.</li>
 * </ul>
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
public class SvgToPngConverter {

    public static void main(String[] args) throws Exception {
        String svgURI = "src/main/draw/flags/germany.svg";
        String pngURI = "src/main/draw/flags/germany.png";

        PNGTranscoder t = new PNGTranscoder();
        t.addTranscodingHint(ImageTranscoder.KEY_FORCE_TRANSPARENT_WHITE, true);

        TranscoderInput trIn = new TranscoderInput(svgURI);

        try (OutputStream ostream = new FileOutputStream(pngURI)) {
            TranscoderOutput trOut = new TranscoderOutput(ostream);
            t.transcode(trIn, trOut);
        } catch (TranscoderException e) {
            e.printStackTrace();
        }
    }
}

