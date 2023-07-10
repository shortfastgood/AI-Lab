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

/**
 * @author dden
 * @version $Revision: 0$
 * @TODO: add the class description here.
 * @since FR23
 * <!--$NoKeywords$-->
 */
public class ProcessKiller {

	public static void main(String[] args) {
		if (args.length == 0) {
			System.out.println("Usage: java -jar ProcessKiller.jar <pid>");
			System.exit(1);
		}
		long pid = Long.parseLong(args[0]);
		ProcessHandle.of(pid).ifPresent(ProcessHandle::destroy);
	}
}
