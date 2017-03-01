
package practica2;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author luislocon
 */
public class Conexion {
    
    
    
    public static OkHttpClient webClient = new OkHttpClient();
    
    
    public static String getString(String metodo, RequestBody formBody) throws IOException{
        
        try {
            URL url = new URL("http://localhost:5000/"+metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
            return response_string;
        } catch (MalformedURLException ex) {
            Logger.getLogger(Practica2.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
