import java.util.Scanner;

public class MainTester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Grander myCar = new Grander(50000000, 1772, "IG");
		myCar.printOut();
		myCar.moveCar();
		
	}

}

 class Grander extends Car {
	private int price;
	private String modelName;
	
	public Grander(int price, int carNumber, String model){
		super(carNumber);
		this.price = price;
		this.modelName = model;
		
	}
	
	public Grander() {
		// TODO Auto-generated constructor stub
	}
	public void setInformation(int price, int carNumber, int modelName) {
		
	}
	
	public void printOut() {
		System.out.println("myCar Price: " + price + " car Number is :" + carNumber);
	}
	
}
 
 class Car {
	protected int carNumber;
	private String carType;
	
	public Car() {
		
	}
	
	public Car(int carNumber){
		this.carNumber = carNumber;
	}
	
	public void moveCar() {
		System.out.println("car is moved");
	}
}