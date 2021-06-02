// https://programmers.co.kr/learn/courses/30/lessons/42746
package test;

import java.util.Arrays;
import java.util.Comparator;

public class practice_210215_02 {
	
	public static String solution(int[] numbers) {
		// ���ڸ� ���ڿ��� ��ȯ
		String[] result = new String[numbers.length];
		for (int i = 0; i < numbers.length; i++) {
			result[i] = String.valueOf(numbers[i]);
		}

		// ����
		Arrays.sort(result, new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				return ((o2 + o1).compareTo(o1 + o2));
			}
		});
		
		// 0�� ������ �ִ� �迭�� ��� �ϳ��� 0�� ����
		if (result[0].equals("0")) {
			return "0";
		}

		String answer = "";
		// ���ĵ� ���� �ϳ��� ��ġ��
		for (String a : result) {
			answer += a;
		}
		return answer;
    }

	public static void main(String[] args) {
		// System.out.println(solution(new int[] {6, 10, 2})); // "6210"
		System.out.println(solution(new int[] {3, 30, 34, 5, 9})); // "9534330"
	}

}

//import java.util.ArrayList;
//import java.util.Collections;
//import java.util.List;
//
//class Solution {
//    public String solution(int[] numbers) {
//        String answer = "";
//
//        List<Integer> list = new ArrayList<>();
//        for(int i = 0; i < numbers.length; i++) {
//            list.add(numbers[i]);
//        }
//        Collections.sort(list, (a, b) -> {
//            String as = String.valueOf(a), bs = String.valueOf(b);
//            return -Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as));
//        });
//        StringBuilder sb = new StringBuilder();
//        for(Integer i : list) {
//            sb.append(i);
//        }
//        answer = sb.toString();
//        if(answer.charAt(0) == '0') {
//            return "0";
//        }else {
//            return answer;
//        }
//    }
//}

//import java.util.*;
//import java.util.stream.*;
//
//class Solution {
//    public String solution(int[] numbers) {
//        String answer = "";
//        answer = Arrays.stream(numbers)
//        .mapToObj(String::valueOf)
//        .sorted((s1, s2) -> -s1.concat(s2).compareTo(s2.concat(s1)))
//        .reduce("", (s1, s2) -> s1.equals("0") && s2.equals("0") ? "0" : s1.concat(s2));
//        return answer;
//    }
//}
