package test;

public class practice_210223_01 {
	
	public static int bfs(int[] numbers, int target, int index) {
		if (index == numbers.length) {
			if (target == 0) {
				return 1;
			} else {
				return 0;
			}
		}
		return bfs(numbers, target + numbers[index], index + 1) + bfs(numbers, target - numbers[index], index + 1);
	}
	
	public static int solution(int[] numbers, int target) {
        int answer = 0;
        answer += bfs(numbers, target, 0);
        return answer;
    }

	public static void main(String[] args) {
		System.out.println(solution(new int[] {1, 1, 1, 1, 1}, 3)); // 5

	}

}
