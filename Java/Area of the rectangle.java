import java.util.Scanner;

public class area_rectangle{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the height of the rectangle: ");
        double height=input.nextDouble();
        System.out.print("Enter the width of the rectangle: ");
        double width =input.nextDouble();

        double area = height*width;

        System.out.println("Area of the rectangle is "+area+" cm²");
    }
}







