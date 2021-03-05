import java.util.Stack;

public class TowerHanoi {
    private final int numberOfDiscs;
    public final Stack<Integer> towerA = new Stack<>();
    public final Stack<Integer> towerB = new Stack<>();
    public final Stack<Integer> towerC = new Stack<>();

    public TowerHanoi(int discs){
      numberOfDiscs = discs;
      for int (int i = 1; i <= discs; i++) {
        towerA.push(i);
      }
    }
}
