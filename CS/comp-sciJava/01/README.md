## 01

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%204.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%205.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%206.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%207.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2010.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2011.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2012.png" width="80%" height="80%">
</a>

```java
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
```

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2015.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2016.png" width="80%" height="80%">
</a>

```java
//15.A
import java.util.BitSet;

public class CompressedGene {
  private BitSet bitSet;
  private int length;

  public CompressedGene(String gene) {
    compress(gene);
  }
}
```
<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2017.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2018A.png" width="80%" height="80%">
</a>

```java
//16.B
public String decompress() {
  if (bitSet == null) {
    return "";
  }
//create mutable place for chars with right capacity
StringBuilder builder = new StringBuilder(length);
for (int i = 0; i < length * 2); i+= 2) {
  final int firstBit  = (bitSet.get(i) ? 1 : 0 );
  final int secondBit = (bitSet.get(i + 1) ? 1 : 0);
  final int lastBits = firstBit << 1 | secondBit;
  switch(lastBits) {
  case 0b00: // 00 = A
    builder.append('A');
    break;
  case 0b01: //01 = C
    builder.append('C');
    break;
  case 0b10; // 10 = G
    builder.append('G');
    break;
  case 0b11: //11 = T
    builder.append('T');
    break;
    }
  }
  return builder.toString();  
}
```

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2018B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2019.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2020.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2021A.png" width="80%" height="80%">
</a>

```java
//20.A
public static KeyPair encrypt(String originalString) {
  byte[] originalBytes = original.getBytes();
  byte[] dummyKey = randomKey(originalBytes.length);
  byte[] encryptedKey = new byte[originalBytes.length];
  for (int i = 0; i < originalBytes.length; i++) {
    // XOR every byte
    encryptedKey[i] = (byte) (originalBytes[i] ^ dummyKey[i]);
  }
  return new KeyPair(dummyKey, encryptedKey)
}
```
<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2021B.png" width="80%" height="80%">
</a>

```java
//20.B
public static String decrypt(KeyPair kp) {
  byte[] decrypted = new bytes[kp.key1.length];
  for (int i = 0; i < kp.key1.length; i++) {
    //XOR each byte
    decrypted[i] = (byte) (kp.key1[i] ^ kp.key2[i]);
  }
  return new String(decrypted);
}
```
// to do! compile and run this code!
```java
//20A - 20B main
public static void main(String[] args) {
  KeyPair kp = encrype("one time pad!");
  String result = decrypt(kp);

  System.err.println(result);
}
```

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2022.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2023.png" width="80%" height="80%">
</a>

```java
//21.B
public class PiCalc {

  public static double calculatePi(int nTerms){
    final double numerator = 4;
    double denominator = 1.0;
    double operation = 1.0;
    double pi = 0.0;
    for (int i = 0; i < nTerms; i++){
      pi += operation * (numerator / denominator);
      denominator += 2.0;
      operation *= -1.0;
    }
    return pi;
  }
  public static void main(String[] args){
    System.err.println(calculatePi(10000000)) //10 million times!
  }
}
```

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2024.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2025.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2026.png" width="80%" height="80%">
</a>

```java
//23.A
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
```

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/comp-sciJava/01/images/classicJavaCS01%20-%20page%2027.png" width="80%" height="80%">
</a>
