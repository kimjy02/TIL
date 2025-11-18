import java.util.Scanner;

public class max {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int A = sc.nextInt();
    int num = 1;
    for (int i=2; i<=9; i++) {
      int B = sc.nextInt();
      if (A < B) {
        A = B;
        num = i;
      }
    }
    System.out.println(A);
    System.out.println(num);
  }
}