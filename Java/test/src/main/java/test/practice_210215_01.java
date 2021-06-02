// https://programmers.co.kr/learn/courses/30/lessons/42748?language=java
package test;

import java.util.ArrayList;
import java.util.Arrays;

public class practice_210215_01 {
	
	public static int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> answerList = new ArrayList<>();
        for(int[] intArr : commands) {
        	int[] arraySlice = Arrays.copyOfRange(array, intArr[0] - 1, intArr[1]);
    		Arrays.sort(arraySlice);
    		answerList.add(arraySlice[intArr[2] - 1]);
        }
        
        int[] answer = new int[answerList.size()];
        
        for(int i = 0; i < answer.length; i++) {
        	answer[i] = answerList.get(i);
        }
        return answer;
    }

	public static void main(String[] args) {
		System.out.println(solution(new int[]{1, 5, 2, 6, 3, 7, 4}, new int[][] {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}})); // {5, 6, 3}
	}

}
