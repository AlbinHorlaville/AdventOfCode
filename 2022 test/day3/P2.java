import java.io.*;  

class Main {
    public static void main(String[] argv){
        try{
            File file = new File("input.txt");
            FileReader fr = new FileReader(file);   //reads the file  
            BufferedReader br = new BufferedReader(fr);  //creates a buffering character input stream
            int sum = 0;

            while (true){
                String elf_1 = br.readLine();
                if (elf_1==null){
                    break;
                }
                String elf_2 = br.readLine();
                String elf_3 = br.readLine();
                String badge;

                int len_elf_1 = elf_1.length();
                int len_elf_2 = elf_2.length();
                int len_elf_3 = elf_3.length();

                System.out.println(len_elf_1);
                System.out.println(len_elf_2);
                System.out.println(len_elf_3);                
            }
            fr.close();
            br.close();
        }catch(IOException e){  
            e.printStackTrace();  
            }  
    }
}