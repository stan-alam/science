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
