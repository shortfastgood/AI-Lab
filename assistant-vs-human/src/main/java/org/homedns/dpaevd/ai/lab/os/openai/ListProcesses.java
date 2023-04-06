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

import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * <p>Generate by ChatGPT-4 using the commands:</p>
 * <ol>
 *     <li>"<em>How to list all live processes in the operating system using a java program ?</em>"</li>
 *
 *     <li>"<em>Add the static class ProcessInfo having the final properties pid (long), command (String) and arguments (String[]) to ListProcesses. Generate also getters and setters.</em>"</li>
 *     <li>"<em>Add the static method getProcesses returning a list of ProcessInfos containing all processes.</em>"</li>
 *     <li>"<em>Add the static void method buildProcessTree taking the parameters parent (ProcessHandle) and level (int).
 *     If the parent is null or the level is negative the method returns immediately. The method handles recursively all children.
 *     The method builds a ProcessInfo for each child. The method prints out PID and command. If any available it also prints the arguments.
 *     The printed line has indentation: add so many spaces as the value of the level.</em>"</li>
 *     <li>"<em>The programm should take care of the processes already printed out to avoid doubles.</em>"</li>
 *     <li>"<em>The list of processes should be sorted by PID</em>"</li>
 *     <li>"<em>buildProcessTree should sort the children by PID</em>"</li>
 *     <li>"<em>the methods' arguments should be final</em>"</li>
 * </ol>
 * @author dden
 * @version $Revision: 0$
 * @since FR23
 * <!--$NoKeywords$-->
 */
public class ListProcesses {

    private static final Set<Long> printedPids = new HashSet<>();

    public static void main(String[] args) {
        List<ProcessHandle> topLevelProcesses = ProcessHandle.allProcesses()
                .filter(process -> process.parent().isEmpty())
                .sorted(Comparator.comparingLong(ProcessHandle::pid))
                .toList();

        topLevelProcesses.forEach(process -> buildProcessTree(process, 0));
    }

    public static void buildProcessTree(ProcessHandle parent, int level) {
        if (parent == null || level < 0) {
            return;
        }

        long pid = parent.pid();
        if (!printedPids.add(pid)) {
            return;
        }

        ProcessHandle.Info processInfo = parent.info();
        String command = processInfo.command().orElse("N/A");
        String[] arguments = processInfo.arguments().orElse(new String[]{});
        ProcessInfo pInfo = new ProcessInfo(pid, command, arguments);

        String indentation = " ".repeat(level);
        System.out.print(indentation + "PID: " + pInfo.getPid() + ", Command: " + pInfo.getCommand());
        if (arguments.length > 0) {
            System.out.print(", Arguments: " + String.join(" ", pInfo.getArguments()));
        }
        System.out.println();

        List<ProcessHandle> sortedChildren = parent.children()
                .sorted(Comparator.comparingLong(ProcessHandle::pid))
                .toList();
        sortedChildren.forEach(child -> buildProcessTree(child, level + 1));
    }

    public static class ProcessInfo {
        private final long pid;
        private final String command;
        private final String[] arguments;

        public ProcessInfo(long pid, String command, String[] arguments) {
            this.pid = pid;
            this.command = command;
            this.arguments = arguments;
        }

        public long getPid() {
            return pid;
        }

        public String getCommand() {
            return command;
        }

        public String[] getArguments() {
            return arguments;
        }
    }
}