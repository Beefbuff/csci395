/*
* Kyle Kalbach
* 01/24/2024
*
 */

import java.io.*; 

public class Pingip {   
	public static void main(String[] args) { 
		String ip = "8.8.8.8"; 			// Google Ip address. 
 		runPingCommand("ping -c 10 " + ip); 	// concat the command to the ip and pass to the method.
		java.util.Date date = new java.util.Date(); 
		System.out.println(date); // gives us the current date (why is this important?) 
	}	 
 
	public static void runPingCommand(String command) {  
		try { 
			Process p = Runtime.getRuntime().exec(command); 
			BufferedReader InputStream = new BufferedReader(new InputStreamReader(p.getInputStream())); 
			String s = " "; 
			while ((s = InputStream.readLine()) != null) { 
				System.out.println(s); 
			}
		} catch (Exception e) { 
			e.printStackTrace();
		}
 	}
}
