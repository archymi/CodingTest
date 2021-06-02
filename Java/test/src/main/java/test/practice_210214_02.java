// https://programmers.co.kr/learn/courses/30/lessons/42627
package test;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class practice_210214_02 {
	
	public static int solution(int[][] jobs) {
        int answer = 0;
        int time = 0;
        int jobCount = 0;
        int jobsIndex = 0;
        
        PriorityQueue<int[]> jobHeap = new PriorityQueue<int[]>((o1, o2) -> o1[1] - o2[1]);
        
        // jobs
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        
        while(jobCount < jobs.length) {
        	while (jobsIndex < jobs.length && jobs[jobsIndex][0] <= time) {
        		jobHeap.add(jobs[jobsIndex++]);
        	}
        	if (jobHeap.isEmpty()) {
        		time=jobs[jobsIndex][0];
        	} else {
        		int[] tmp = jobHeap.poll();
        		answer += tmp[1] + time - tmp[0];
        		time += tmp[1];
        		jobCount ++;
        	}
        }
        return (int) Math.floor(answer / jobCount);
    }

	public static void main(String[] args) {
		System.out.println(solution(new int[][] {{0, 3}, {1, 9}, {2, 6}})); // 9

	}

}
