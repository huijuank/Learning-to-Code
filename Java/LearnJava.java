/*
Learn Java
Everything I learn about Java
*/

public class LearningJava {
  // Every Java application must contain main() method (entry point)
  // This method accepts a single argument: an array of elements of type String
  public static void main(String[] args) {
    
    // print line
    System.out.println("Hello world!");
    
    // variables
    String name = "Hui Juan"; // double quotes
    int age = 22; // allow positive, negative, zero, no decimals
    boolean schooling = True;
    char gender = 'f'; // single quotes, single character
    double bank = 123.45; // decimal
    float wallet = (float)12.5;
    long ic = 9280374;
    short icShort = 74;
    byte b = 20;
    final double pi = 3.141592; // variable cannot be changed or will produce error
    
    // Math Operations
    int years = 5;
    int newage;
    newage = age + years; // 27
    newage = age - years; // 17
    newage = age * years; // 110
    newage = age / years; // 4
    newage = age % years; // 2
    
    // Comparison Operators
    boolean result = age > years;
    /*
    > greater than
    < less than
    >= greater than or equals to
    <= less than or equals to
    == equals to
    != not equals to
    */
    
    // Compound Assignment Operators
    age += 5; // same for - * / %
    
    // Increment and Decrement Operators
    years++ // years = 6, increase by 1
    years-- // years = 5, decrease by 1
      
    
    boolean nameCheck = name.equals("Joanne"); // use this to compare Strings, not ==
    
  }

}


/*
Compile class file: javac LearnJava.java // converted to .class file (byte code)
Execute compiled file: java LearnJava

Whitespace: ignored
Statement: end with ;
Static typing: variable type checked at compile time to catch errors before execution
Order of operations: PMDModAS
*/
