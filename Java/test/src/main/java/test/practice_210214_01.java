// https://programmers.co.kr/learn/courses/30/lessons/42626?language=java
// 
package test;
import java.util.PriorityQueue;

//낮은 숫자가 우선 순위인 int 형 우선순위 큐 선언
//PriorityQueue<Integer> priorityQueueLowest = new PriorityQueue<>();

//높은 숫자가 우선 순위인 int 형 우선순위 큐 선언
//PriorityQueue<Integer> priorityQueueHighest = new PriorityQueue<>(Collections.reverseOrder());

public class practice_210214_01 {

	public static int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> prior = new PriorityQueue<Integer>(); 
        for (int i : scoville) {
        	prior.add(i);
        }
        while(true) {
        	int a = prior.poll();
        	int b = prior.poll();
        	prior.add(a + b * 2);
        	answer ++;
        	if (prior.peek() >= K)
        		break;
        	if (prior.size() <= 2) {
        		answer = -1;
        		break;
        	}
        }
        return answer;
    }

	public static void main(String[] args) {
		System.out.println(solution(new int[] {1, 2, 3, 9, 10, 12}, 7));
		
	}

}

//import java.util.*;
//class Solution {
//    public int solution(int[] scoville, int K) {
//        PriorityQueue<Integer> q = new PriorityQueue<>();
//
//        for(int i = 0; i < scoville.length; i++)
//            q.add(scoville[i]);
//
//        int count = 0;
//        while(q.size() > 1 && q.peek() < K){
//            int weakHot = q.poll();
//            int secondWeakHot = q.poll();
//
//            int mixHot = weakHot + (secondWeakHot * 2);
//            q.add(mixHot);
//            count++;
//        }
//
//        if(q.size() <= 1 && q.peek() < K)
//            count = -1;
//
//        return count;
//    }
//}
