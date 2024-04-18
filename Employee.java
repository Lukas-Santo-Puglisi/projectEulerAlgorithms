
// Subclassing thread is using polymorphism and 

public class EmployeeThread extends Thread{
    public void run(){
        this.executeSomeOtherThreadCode()
    }

}


public class Employee implements Runnable{
    private double salary;

    public void run(){
        this.executeSomeThreadCode()
    }

    public static void main(String [args]){
        Runnable myEmployyee = new Empleyee();
        Thread myEmployethread = new Thread(new EmployeeThread());
        myEmployee.run();
        myEmployehtread.start();

    }

