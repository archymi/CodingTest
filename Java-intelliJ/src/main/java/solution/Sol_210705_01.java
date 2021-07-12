package solution;

import java.util.Arrays;
import java.util.Collections;

// https://programmers.co.kr/learn/courses/30/lessons/1835?language=java

public class Sol_210705_01 {
    public int solution(int n, String[] data) {
        int answer = 0;
        Arrays.sort(data, Collections.reverseOrder());
        System.out.println(data[0]);
        return answer;
    }
}
