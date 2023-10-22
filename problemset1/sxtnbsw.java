import java.util.Scanner;


public class sxtnbsw{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        int nLines = Integer.parseInt(input);

        String[][] arrs = new String[nLines][2]; //hmm

        for(int i=0; i<nLines; i++){
            String in = scanner.nextLine();
            String[] inArr = in.split(" ");
            arrs[i] = inArr;
        }

        scanner.close(); //dont need input past this point

        for(int i=0; i<arrs.length; i++){
            parseArr(arrs[i]);
        }
    }

    public static void parseArr(String[] inArr){
        if((Long.parseLong(inArr[0]) * Long.parseLong(inArr[1])) != Long.parseLong(inArr[2])){
            System.out.println("16 BIT S/W ONLY");
        }else{
            System.out.println("POSSIBLE DOUBLE SIGMA");
        }
    }
}
