import javax.swing.JOptionPane;

public class MemoriaEstatica {
    public static void main(String[] args) {
        int calificaciones[] = new int[5];

        for(int i = 0; i < 5; i++) {
            calificaciones[i] = Integer.parseInt(JOptionPane.showInputDialog(null, "Captura la calificación:"));
        }
        
        for(int i = 0; i < 5; i++) {
            System.out.println("Calificación " + (i + 1) + ": " + calificaciones[i]);
        }
    }
}
