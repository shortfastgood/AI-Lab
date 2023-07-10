/* *****************************************************************************
 * CREALOGIX AG
 * Defense
 * Maneggstrasse 17
 * CH-8041 Zuerich
 *
 * http://defense.crealogix.com
 *******************************************************************************
 *
 * $Author: First Last$
 * $Date: 12.4.18 12:29:06 MEST$
 * $Revision: 4$
 *
 * $Project: project$
 * $Folder: directory$
 * $Workfile: file.java$
 *
 * Description: see JavaDoc comment of this class.
 *
 ***************************************************************************** */
package org.homedns.dpaevd.ai.lab.os.openai;

import java.util.stream.Stream;

/**
 * Generate by ChatGPT-4 using the command: "<em>How to list all live processes in the operating system using a java program ?</em>"
 * @author dden
 * @version $Revision: 0$
 * @since FR23
 * <!--$NoKeywords$-->
 */
public class SimpleListProcesses {
    public static void main(String[] args) {
        Stream<ProcessHandle> allProcesses = ProcessHandle.allProcesses();
        allProcesses.forEach(process -> {
            ProcessHandle.Info processInfo = process.info();
            String command = processInfo.command().orElse("N/A");
            System.out.println("PID: " + process.pid() + ", Command: " + command);
        });
    }
}
