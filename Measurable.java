
// Task: Implement an interface in Java named Measurable with a single method getMeasure(), which returns a double. Then, create a class Employee that implements Measurable. The class should have a private instance variable salary of type double, a constructor to set this salary, and an implementation of getMeasure() that returns the salary. Demonstrate using this interface and class by creating an instance of Employee and printing its measure.

public interface Measurable{
    double getMeasure();
}

public class Employee implements Measurable{
    private double salary;

    public Employee(double salary){
        this.salary = salary;
    }
    @Override
    public double getMeasure(){
        return this.salary;
    }

    public static void main(String[] args){
        Measurable myEmployee = new Employee(2.0);
    System.out.println(myEmployee.getMeasure);

    }
}

