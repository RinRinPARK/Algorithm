package Stack;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class P9012 {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(bf.readLine());
        for(int i = 0; i < T; i ++) {
            int flag = 0;
            List<Character> arr = new ArrayList<>();
            String line = bf.readLine();

            for(int j = 0; j < line.length(); j ++) {
                char bracket = line.charAt(j);
                if (bracket == '(') {
                    arr.add(bracket);
                } else {
                    if (!arr.isEmpty()) {
                        arr.remove(arr.size() - 1);
                    } else {
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag == 1) {
                System.out.println("NO");
                continue;
            }
            if (!arr.isEmpty()) {
                System.out.println("NO");
                continue;
            }
            System.out.println("YES");
        }
    }
}
