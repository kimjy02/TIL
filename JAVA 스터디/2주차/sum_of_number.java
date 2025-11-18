import java.math.BigInteger;
import java.util.Scanner;

public class sum_of_number {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    BigInteger num = sc.nextBigInteger();
    int sum = 0;
    while (num.compareTo(BigInteger.ZERO) > 0) {
      BigInteger digit = num.mod(BigInteger.TEN);
      sum += digit.intValue();
      num = num.divide(BigInteger.TEN);
    }
    System.out.println(sum);
  }
}
