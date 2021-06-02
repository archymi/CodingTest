// https://programmers.co.kr/learn/courses/30/lessons/43162?language=java
package test;

public class practice_210223_02 {
	public static boolean[] dfs(int[][] computers, int index, boolean[] visited) {
		visited[index] = true;
		for(int i = 0; i < computers[index].length; i++) {
			if (i != index && !visited[i] && computers[index][i] == 1) {
				visited = dfs(computers, i, visited);
			}
		}
		return visited;
	}
	
	public static int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n]; // 초기값은 모두 false로 자동 초기화.
        for (int i = 0; i < n; i++) {
        	if (!visited[i]) {
        		answer++;
        		dfs(computers, i, visited);
        	}
        }
        
        
        return answer;
    }
	
	public static void main(String[] args) {
		System.out.println(solution(3, new int[][] {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}})); // 2;
	}

}
