package test;
import java.util.*;

public class practice_210225_01 {
	public boolean[] isPrime = new boolean[10000000];

	// 소수를 구한다.
	public void primeNumber() {
		Arrays.fill(this.isPrime, true);
		this.isPrime[0] = false;
		this.isPrime[1] = true;
		// true if prime number.
		for(int i = 2; i < Math.sqrt(10000000); i ++) {
			// 이미 체크된 애들은 skip.
			if (this.isPrime[i] == false)
				continue;
			
			// i의 배수들은 걸러준다.
			for (int j = i*i; j < this.isPrime.length; j = j + i) {
				this.isPrime[j] = false;
			}
		}
	}
	
	// permutation 을 구한다.
	public ArrayList<Integer> permutation(ArrayList<Integer> input, ArrayList<Integer> result, int count) {
		
		return result;
	}
	
	public int solution(String numbers) {
        int answer = 0;
        primeNumber();
        for (int i = 0; i < numbers.length(); i++) {
        	System.out.println(numbers.charAt(i));
        }
        return answer;
    }

	public void main(String[] args) {
		// TODO Auto-generated method stub
		solution("17");
	}

}
