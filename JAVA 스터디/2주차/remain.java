import java.util.Scanner;
import java.util.HashSet;
import java.util.Set;

public class remain {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Set <Integer> s = new HashSet<>();
    for (int i=1; i<=10; i++) {
      int A = sc.nextInt();
      s.add(A%42);
    }
    System.out.println(s.size());
  }
}