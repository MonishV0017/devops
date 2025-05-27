
package lab4_gradle;

import java.awt.Desktop;
import java.net.URI;

public class App2 {
    public static void main(String[] args) {
        String url = "https://www.google.com";
        try {
            if (Desktop.isDesktopSupported()) {
                Desktop.getDesktop().browse(new URI(url));
            } else {
                System.out.println("Desktop is not supported");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
