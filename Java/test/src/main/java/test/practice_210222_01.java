// https://programmers.co.kr/learn/courses/30/lessons/42747
package test;

import java.util.Arrays;

public class practice_210222_01 {
	public static int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        if (citations[citations.length - 1] == 0) {
        	return 0;
        }
        if (citations.length == 1) {
        	return 1;
        }
        boolean[] answerList = new boolean[citations[citations.length - 1]];
        
        int start = 1;
        for (int i = 0; i < citations[citations.length - 1]; i++) {
        	int count = 0;
        	for (int c : citations) {
        		if ( c >= start ) {
        			count ++;
        		}
        	}
        	if (count >= start) {
        		answerList[i] = true;
        	} else {
        		answerList[i] = false;
        	}
        	if (i > 0) {
        		if (answerList[i-1] == true && answerList[i] == false) {
        			return start - 1;
        		}
        	}
        	start++;
        }
        
        return answer;
    }

	public static void main(String[] args) {
		System.out.println(solution(new int[] {10, 10})); // 

	}
}


//import java.util.*;
//
//class Solution {
//    public int solution(int[] citations) {
//        Arrays.sort(citations);
//
//        int max = 0;
//        for(int i = citations.length-1; i > -1; i--){
//            int min = (int)Math.min(citations[i], citations.length - i);
//            if(max < min) max = min;
//        }
//
//        return max;
//    }
//}