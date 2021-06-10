package net.airqo;

import com.google.gson.Gson;
import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;
import com.google.gson.reflect.TypeToken;
import net.airqo.models.TransformedMeasurement;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Serializable;
import java.lang.reflect.Type;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Properties;

public class Calibrate {

    private static final Logger logger = LoggerFactory.getLogger(Calibrate.class);


    public static class CalibrateResponse implements Serializable {

        @SerializedName("device_id")
        @Expose
        String device;

        @SerializedName("calibrated_value")
        @Expose
        Object calibratedValue;

        public CalibrateResponse() {
        }

        public String getDevice() {
            return device;
        }

        public void setDevice(String device) {
            this.device = device;
        }

        public Object getCalibratedValue() {
            return calibratedValue;
        }

        public void setCalibratedValue(Object calibratedValue) {
            this.calibratedValue = calibratedValue;
        }
    }

    public static class CalibratedBody {
        String datetime;
        HashMap<String, Object> raw_values;


        public CalibratedBody(TransformedMeasurement transformedMeasurement) {
            datetime = transformedMeasurement.getTime();
            raw_values = new HashMap<String, Object>(){{
                put("device_id", transformedMeasurement.getDevice());
                put("pm2.5", transformedMeasurement.getPm2_5());
                put("pm10", transformedMeasurement.getPm10());
                put("temperature", transformedMeasurement.getInternalTemperature());
                put("humidity", transformedMeasurement.getInternalHumidity());
            }};
        }
    }

    public static Object getCalibratedValue(TransformedMeasurement transformedMeasurement, String propertiesUrlFile) throws IOException {

        if(transformedMeasurement == null)
            throw new IOException("Invalid Measurements");

        if(propertiesUrlFile == null || propertiesUrlFile.equals(""))
            propertiesUrlFile = "application.properties";

        List<CalibrateResponse> calibrateResponseList = new ArrayList<>();

        CalibratedBody body = new CalibratedBody(transformedMeasurement);

        Properties props = Utils.loadPropertiesFile(propertiesUrlFile);

        if(!props.containsKey("calibrate.url"))
            throw new IOException("calibrate.url is missing in " + propertiesUrlFile + " file");

        String urlString = props.getProperty("calibrate.url");

        URL url = new URL(urlString);

        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Accept", "application/json");

        conn.connect();

        logger.error(conn.getResponseMessage());

        int responseCode = conn.getResponseCode();


        if(responseCode == 200){

            BufferedReader in = new BufferedReader(
                    new InputStreamReader(conn.getInputStream()));

            StringBuilder sb = new StringBuilder();
            String line;

            while ((line = in.readLine()) != null) {
                sb.append(line);
            }

            calibrateResponseList = stringToObjectList(sb.toString());

        }

        conn.disconnect();

        return calibrateResponseList.isEmpty() ? "null" : calibrateResponseList.get(0).getCalibratedValue();
    }

    public static List<CalibrateResponse> stringToObjectList(String s){

        Type listType = new TypeToken<List<CalibrateResponse>>() {}.getType();

        return new Gson().fromJson(s, listType);
    }
}
