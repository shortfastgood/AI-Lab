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
package org.homedns.dpaevd.ai.lab.os.human;

import java.util.*;
import java.util.stream.IntStream;

/**
 * Programmed by human with the help of Copilot.
 * @author dden
 * @version $Revision: 0$
 * @since FR23
 * <!--$NoKeywords$-->
 */
public class ListProcesses {

    private static final Map<Long, ProcessInfo> alreadyProcessed = new HashMap<>();

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

    public static List<ProcessInfo> getProcesses() {
        List<ProcessInfo> processes = new ArrayList<>();
        ProcessHandle.allProcesses()
                .sorted(Comparator.comparing(ProcessHandle::pid))
                .filter(ProcessHandle::isAlive)
                .forEach(process -> {
            ProcessHandle.Info processInfo = process.info();
            String command = processInfo.commandLine().orElse("N/A");
            String[] arguments = processInfo.arguments().orElse(new String[0]);
            processes.add(new ProcessInfo(process.pid(), command, arguments));
        });
        return processes;
    }

    public static void buildProcessTree(final ProcessHandle parent, final int level) {
        if (parent != null) {
            parent.children()
                    .sorted(Comparator.comparing(ProcessHandle::pid))
                    .filter(ProcessHandle::isAlive)
                    .forEach(process -> {
                if (!alreadyProcessed.containsKey(process.pid())) {
                    ProcessInfo processInfo = new ProcessInfo(
                            process.pid(), process.info().command().orElse("N/A"),
                            process.info().arguments().orElse(new String[0]));
                    IntStream.range(0, level).forEach(i -> System.out.print(" "));
                    System.out.print("PID: " + processInfo.getPid() + ", Command: " + processInfo.getCommand());
                    if (processInfo.arguments != null && processInfo.getArguments().length > 0) {
                        System.out.print(", Arguments: " + String.join(" ", processInfo.getArguments()));
                    }
                    System.out.println();
                    alreadyProcessed.put(processInfo.getPid(), processInfo);
                }
                buildProcessTree(process, level + 1);
            });
        }
    }

    public static void main(String[] args) {
        List<ProcessInfo> allProcesses = getProcesses();
        allProcesses.forEach(process -> {
            if (!alreadyProcessed.containsKey(process.getPid())) {
                System.out.print("PID: " + process.getPid() + ", Command: " + process.getCommand());
                if (process.arguments != null && process.getArguments().length > 0) {
                    System.out.print(", Arguments: " + String.join(" ", process.getArguments()));
                }
                System.out.println();
                alreadyProcessed.put(process.getPid(), process);
                buildProcessTree(ProcessHandle.of(process.getPid()).orElse(null), 1);
            }
        });
    }
}
