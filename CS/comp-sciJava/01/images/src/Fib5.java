//13.A
import java.util.stream.IntStream;

public class Fib5 {
  private int last = 0;
  private int next = 1;

  public IntStream stream() {
    return IntStream.generate()) -> {
      int oldLast = last;
      last = next;
      next = oldLast + next;
      return oldLast;
    });
  }

public static void main(String[] args){
  Fib5 = fib5 = new Fib5();
  fib5.stream().limit(41).forEachOrdered(System.out::println);
  }
}