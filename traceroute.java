/*
* Kyle Kalbach
* 01/227/2024
*
 */

 import java.io.*; 

 public class traceroute {   
     public static void main(String[] args) { 
         String ip = "www.wgal.com"; 			//  
          runTraceCommand("traceroute " + ip); 	// concat the command to the ip and pass to the method.
         java.util.Date date = new java.util.Date(); 
         System.out.println(date); // current date is important because traffic can change over time.
     }	 
  
     public static void runTraceCommand(String command) {  
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
 