package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class P2193 {
    //    이친수는 0으로 시작하지 않는다.
    //    이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    // BufferedReader를 이용해서 readLine()을 할 때는 exception handling을 해줘야 함.
    public static void main(String[] args) throws IOException {

        long N = Integer.parseInt(bf.readLine());

        if (N == 0 || N == 1) {
            System.out.println(1);
            return ;
        }

        ArrayList<Long> arr = new ArrayList<Long>();
        arr.add(1L);
        arr.add(1L);

        for (int i = 2; i < N; i++) {
            arr.add(arr.get(i-2) + arr.get(i-1));
        }

        System.out.println(arr.get((int) (N-1)));
    }
}

/* 메모리초과난 코드
public class P2193 {
//    이친수는 0으로 시작하지 않는다.
//    이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    static int result = 0;

    private static void DFS(String ipt, int N) {

        if (ipt.length() == N) {
            result += 1;
            return ;
        }

        if (ipt.charAt(ipt.length()-1) == '0') {
            DFS(ipt + '0', N);
            DFS(ipt + '1', N);
        } else {
            DFS(ipt + '0', N);
        }
    }

    // BufferedReader를 이용해서 readLine()을 할 때는 exception handling을 해줘야 함.
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(bf.readLine());

        // DFS
        // 문자열 남은 자리를 계속 맞나 채우면서 재귀로 방문
        DFS("1", N);
        System.out.println(result);
    }
}

 */
