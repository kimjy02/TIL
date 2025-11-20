import java.util.*;

public class word_study {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    List<Character> list = new ArrayList<>();
    Map<Character, Integer> count = new HashMap<>();

    for (char c : s.toCharArray()) {
      c = Character.toUpperCase(c);
      list.add(c);

      count.put(c, count.getOrDefault(c, 0) + 1);
    }

    int maxValue = 0;
    char answer = '?';

    for (char key : count.keySet()) {
      int value = count.get(key);

      if (value > maxValue) {
        maxValue = value;
        answer = key;
      } else if (value == maxValue) {
        answer = '?';
      }
    }

    System.out.println(answer);
  }
}
