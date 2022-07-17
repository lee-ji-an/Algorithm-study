package math;

import java.util.Scanner;
public class BOJ_10430 {
	public static void main(String[] args) {
		String s;
		int a, b, c;
		Scanner sc = new Scanner(System.in);
		s = sc.nextLine();
		String[] ArrayStr = s.split(" ");
		a = Integer.parseInt(ArrayStr[0]);
		b = Integer.parseInt(ArrayStr[1]);
		c = Integer.parseInt(ArrayStr[2]);
		
		System.out.println((a+b)%c);
		System.out.println(((a%c)+(b%c))%c);
		System.out.println((a*b)%c);
		System.out.println(((a%c)*(b%c))%c);
	}
	
}
