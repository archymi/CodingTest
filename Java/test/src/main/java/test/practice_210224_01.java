package test;

import java.util.Arrays;

// https://programmers.co.kr/learn/courses/30/lessons/42860?language=java

public class practice_210224_01 {
    public static final char[] alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

    public static int betweenAlphabet(char a, char b) {
        int start = 0;
        int end = 0;
        for (int i = 0; i < alphabet.length; i++) {
            if (alphabet[i] == a)
                start = i;
            if (alphabet[i] == b)
                end = i;
            if (start != 0 && end != 0)
                break;
        }
        return Math.min(Math.abs(a-b), Math.abs(a + 26 - b));
    }
    public static boolean matchChar(char[] a, char[] b) {
        if (a.length != b.length) {
            return false;
        }
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i])
                return false;
        }
        return true;
    }
    public static int solution(String name) {
        int answer = 0;
        int index = 0;
        int max = name.length() - 1;
        int min = 0;
        char[] origin = new char[name.length()];
        char[] right = name.toCharArray();
        
        int count = 0;
        // initialize  origin with "A"
        for (int i = 0; i < origin.length; i++) {
            origin[i] = 'A';
        }

        while(true) {
            int leftChoice = 0;
            int rightChoice = 0;
            char[] copy;

            if(origin[index] != right[index]) {
                answer += betweenAlphabet(origin[index], right[index]);
                origin[index] = right[index];
            }
            if (matchChar(origin, right)) {
                break;
            }
            
            copy = Arrays.copyOf(origin, origin.length);
            // in case rightChoice
            for (int i = 1; i <name.length(); i++) {
            	rightChoice += betweenAlphabet(copy[(index + i) % name.length()], right[(index + i) % name.length()]) + 1;
            	copy[(index + i) % name.length()] = right[(index + i) % name.length()];
            	if (matchChar(copy, right)) {
                    break;
                }
            }
            
            copy = Arrays.copyOf(origin, origin.length);
            // in case leftChoice
            for (int i = 1; i <name.length(); i++) {
            	leftChoice += betweenAlphabet(copy[(index + name.length() - i) % name.length()], right[(index + name.length() - i) % name.length()]) + 1;
            	copy[(index + name.length() - i) % name.length()] = right[(index + name.length() - i) % name.length()];
            	if (matchChar(copy, right)) {
                    break;
                }
            }
            
            if (rightChoice < leftChoice) {
                index = (index + 1) % name.length();
            } else {
            	index = (name.length() + index - 1) % name.length();
            }
            answer++;
        }
        return answer;
    }

    public static void main(String[] args) {
//        System.out.println(solution(new String("JEROEN"))); // 56;
//        System.out.println(solution(new String("JAN"))); // 11;
    	System.out.println(solution(new String("BBBAAAB"))); // 9;
        System.out.println(solution(new String("ABABAAAAABA"))); // 11;
    }
}
