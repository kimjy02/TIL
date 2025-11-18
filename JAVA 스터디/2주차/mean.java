import java.util.Scanner;

public class mean {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    double sum = 0;
    int [] score_lst = new int[N];
    int max = Integer.MIN_VALUE;
    for (int i=0; i<=N-1; i++) {
      int score = sc.nextInt();
      score_lst[i] = score;
      if (score > max) {
        max = score;
      }
    }
    for (int i=0; i<=N-1; i++) {
      sum = sum + ((double) score_lst[i]/max * 100);
    }
    System.out.println(sum/N);
  }
}
