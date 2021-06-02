// https://programmers.co.kr/learn/courses/30/lessons/42840
package test;

import java.util.*;

public class practice_210222_02 {
	
	public static int[] solution(int[] answers) {
        ArrayList<Integer> answerList = new ArrayList<Integer>();
		int[] one_test = new int[] {1, 2, 3, 4, 5};
		int[] two_test = new int[] {2, 1, 2, 3, 2, 4, 2, 5};
		int[] three_test = new int[] {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
		
		int[] answerCount = new int[] {0, 0, 0};
		
		for (int i = 0; i < answers.length; i++) {
			if (answers[i] == one_test[i % 5])
				answerCount[0]++;
			if (answers[i] == two_test[i % 8])
				answerCount[1]++;
			if (answers[i] == three_test[i % 10])
				answerCount[2]++;
		}

		int max = 0;
		int maxIndex = 0;
		for (int i = 0; i < 3; i++) {
			if (answerCount[i] >= max) {
				max = answerCount[i];
				maxIndex = i;
			}
		}
		for (int i = 0; i < 3; i++) {
			if (max == answerCount[i]) {
				answerList.add(i + 1);
			}
		}
		
		int[] answer = new int[answerList.size()];
		for (int i = 0; i < answerList.size(); i ++) {
			answer[i] = answerList.get(i);
		}
        return answer;
    }

	public static void main(String[] args) {
		System.out.println(Arrays.toString(solution(new int[] {1, 2, 3 ,4, 5})));
		System.out.println(Arrays.toString(solution(new int[] {1, 3, 2, 4, 2})));
	}

}

//
//import java.util.ArrayList;
//class Solution {
//    public int[] solution(int[] answer) {
//        int[] a = {1, 2, 3, 4, 5};
//        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
//        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
//        int[] score = new int[3];
//        for(int i=0; i<answer.length; i++) {
//            if(answer[i] == a[i%a.length]) {score[0]++;}
//            if(answer[i] == b[i%b.length]) {score[1]++;}
//            if(answer[i] == c[i%c.length]) {score[2]++;}
//        }
//        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
//        ArrayList<Integer> list = new ArrayList<>();
//        if(maxScore == score[0]) {list.add(1);}
//        if(maxScore == score[1]) {list.add(2);}
//        if(maxScore == score[2]) {list.add(3);}
//        return list.stream().mapToInt(i->i.intValue()).toArray();
//    }
//}