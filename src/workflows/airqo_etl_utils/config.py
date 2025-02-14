import os
from pathlib import Path

import pymongo as pm
import tweepy
import urllib3
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

urllib3.disable_warnings()


class Config:
    # Kcca
    CLARITY_API_KEY = os.getenv("CLARITY_API_KEY")
    CLARITY_API_BASE_URL = os.getenv("CLARITY_API_BASE_URL")

    # Thingspeak
    THINGSPEAK_API_KEY = os.getenv("THINGSPEAK_API_KEY")
    THINGSPEAK_CHANNEL_URL = os.getenv("THINGSPEAK_CHANNEL_URL")

    # Aggregated data
    BIGQUERY_HOURLY_EVENTS_TABLE = os.getenv("BIGQUERY_HOURLY_EVENTS_TABLE")
    BIGQUERY_HOURLY_EVENTS_TABLE_PROD = os.getenv("BIGQUERY_PROD_HOURLY_EVENTS_TABLE")
    BIGQUERY_DAILY_EVENTS_TABLE = os.getenv("BIGQUERY_DAILY_EVENTS_TABLE")
    BIGQUERY_HOURLY_FORECAST_EVENTS_TABLE = os.getenv(
        "BIGQUERY_HOURLY_FORECAST_EVENTS_TABLE"
    )
    BIGQUERY_DAILY_FORECAST_EVENTS_TABLE = os.getenv(
        "BIGQUERY_DAILY_FORECAST_EVENTS_TABLE"
    )
    BIGQUERY_HOURLY_WEATHER_TABLE = os.getenv("BIGQUERY_HOURLY_WEATHER_TABLE")
    BIGQUERY_OPENWEATHERMAP_TABLE = os.getenv("BIGQUERY_OPENWEATHERMAP_TABLE")
    BIGQUERY_ANALYTICS_TABLE = os.getenv("BIGQUERY_ANALYTICS_TABLE")
    BIGQUERY_SATELLITE_DATA_TABLE = os.getenv("BIGQUERY_SATELLITE_DATA_TABLE")

    # Bam data
    BIGQUERY_RAW_BAM_DATA_TABLE = os.getenv("BIGQUERY_RAW_BAM_DATA_TABLE")
    BIGQUERY_BAM_EVENTS_TABLE = os.getenv("BIGQUERY_BAM_EVENTS_TABLE")

    # Raw data
    BIGQUERY_AIRQO_MOBILE_EVENTS_TABLE = os.getenv("BIGQUERY_AIRQO_MOBILE_EVENTS_TABLE")
    BIGQUERY_RAW_EVENTS_TABLE = os.getenv("BIGQUERY_RAW_EVENTS_TABLE")
    BIGQUERY_LATEST_EVENTS_TABLE = os.getenv("BIGQUERY_LATEST_EVENTS_TABLE")
    BIGQUERY_CLEAN_RAW_MOBILE_EVENTS_TABLE = os.getenv(
        "BIGQUERY_CLEAN_RAW_MOBILE_EVENTS_TABLE"
    )
    BIGQUERY_UNCLEAN_RAW_MOBILE_EVENTS_TABLE = os.getenv(
        "BIGQUERY_UNCLEAN_RAW_MOBILE_EVENTS_TABLE"
    )
    BIGQUERY_DEVICES_SUMMARY_TABLE = os.getenv("BIGQUERY_DEVICES_SUMMARY_TABLE")
    BIGQUERY_RAW_WEATHER_TABLE = os.getenv("BIGQUERY_RAW_WEATHER_TABLE")
    SENSOR_POSITIONS_TABLE = os.getenv("SENSOR_POSITIONS_TABLE")

    # Meta data
    BIGQUERY_DEVICES_TABLE = os.getenv("BIGQUERY_DEVICES_TABLE")
    BIGQUERY_DEVICES_DATA_TABLE = os.getenv("BIGQUERY_DEVICES_DATA_TABLE")
    BIGQUERY_SITES_TABLE = os.getenv("BIGQUERY_SITES_TABLE")
    BIGQUERY_SITES_META_DATA_TABLE = os.getenv("BIGQUERY_SITES_META_DATA_TABLE")
    BIGQUERY_AIRQLOUDS_TABLE = os.getenv("BIGQUERY_AIRQLOUDS_TABLE")
    BIGQUERY_AIRQLOUDS_SITES_TABLE = os.getenv("BIGQUERY_AIRQLOUDS_SITES_TABLE")
    BIGQUERY_GRIDS_TABLE = os.getenv("BIGQUERY_GRIDS_TABLE")
    BIGQUERY_COHORTS_TABLE = os.getenv("BIGQUERY_COHORTS_TABLE")
    BIGQUERY_GRIDS_SITES_TABLE = os.getenv("BIGQUERY_GRIDS_SITES_TABLE")
    BIGQUERY_COHORTS_DEVICES_TABLE = os.getenv("BIGQUERY_COHORTS_DEVICES_TABLE")

    # Data Checks
    BIGQUERY_GX_RESULTS_TABLE = os.getenv("BIGQUERY_GX_RESULTS_TABLE")

    # AirQo
    POST_EVENTS_BODY_SIZE = os.getenv("POST_EVENTS_BODY_SIZE", 10)
    POST_WEATHER_BODY_SIZE = os.getenv("POST_EVENTS_BODY_SIZE", 10)
    CALIBRATION_BASE_URL = os.getenv("CALIBRATION_BASE_URL")
    AIRQO_BASE_URL_V2 = os.getenv("AIRQO_BASE_URL_V2")
    AIRQO_API_KEY = os.getenv("AIRQO_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    GOOGLE_CLOUD_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
    AIRQO_API_TOKEN = os.getenv("AIRQO_API_TOKEN")

    # Tahmo
    TAHMO_BASE_URL = os.getenv("TAHMO_API_BASE_URL")
    TAHMO_API_MAX_PERIOD = os.getenv("TAHMO_API_MAX_PERIOD")
    TAHMO_API_KEY = os.getenv("TAHMO_API_CREDENTIALS_USERNAME")
    TAHMO_API_SECRET = os.getenv("TAHMO_API_CREDENTIALS_PASSWORD")

    # OpenWeather
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    OPENWEATHER_BASE_URL = os.getenv("OPENWEATHER_BASE_URL")
    OPENWEATHER_DATA_BATCH_SIZE = os.getenv("OPENWEATHER_DATA_BATCH_SIZE")
    # Kafka
    BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
    TOPIC_PARTITIONS = os.getenv("TOPIC_PARTITIONS", "1,2,3,4").split(",")
    SCHEMA_REGISTRY_URL = os.getenv("SCHEMA_REGISTRY_URL")

    # Kafka Topics
    WEATHER_MEASUREMENTS_TOPIC = os.getenv("WEATHER_MEASUREMENTS_TOPIC")
    INSIGHTS_MEASUREMENTS_TOPIC = os.getenv("INSIGHTS_MEASUREMENTS_TOPIC")
    HOURLY_MEASUREMENTS_TOPIC = os.getenv("HOURLY_MEASUREMENTS_TOPIC")
    BAM_MEASUREMENTS_TOPIC = os.getenv("BAM_MEASUREMENTS_TOPIC")
    DEVICES_TOPIC = os.getenv("DEVICES_TOPIC")

    # Airnow
    AIRNOW_BASE_URL = os.getenv("AIRNOW_BASE_URL")
    AIRNOW_API_KEY = os.getenv("AIRNOW_API_KEY")
    AIRNOW_COUNTRIES_METADATA_JSON_FILE = os.getenv(
        "AIRNOW_COUNTRIES_METADATA_JSON_FILE"
    )

    # US Embassy
    US_EMBASSY_API_KEY = os.getenv("US_EMBASSY_API_KEY")

    # FIREBASE
    FIREBASE_AIR_QUALITY_READINGS_COLLECTION = os.getenv(
        "FIREBASE_AIR_QUALITY_READINGS_COLLECTION"
    )
    APP_USERS_DATABASE = os.getenv("APP_USERS_DATABASE")
    FIREBASE_USERS_COLLECTION = os.getenv("FIREBASE_USERS_COLLECTION")
    APP_NOTIFICATION_TEMPLATES_DATABASE = os.getenv(
        "APP_NOTIFICATION_TEMPLATES_DATABASE"
    )
    FIREBASE_TYPE = os.getenv("FIREBASE_TYPE")
    FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
    FIREBASE_PRIVATE_KEY_ID = os.getenv("FIREBASE_PRIVATE_KEY_ID")
    FIREBASE_PRIVATE_KEY = os.getenv("FIREBASE_PRIVATE_KEY")
    FIREBASE_CLIENT_EMAIL = os.getenv("FIREBASE_CLIENT_EMAIL")
    FIREBASE_CLIENT_ID = os.getenv("FIREBASE_CLIENT_ID")
    FIREBASE_AUTH_URI = os.getenv("FIREBASE_AUTH_URI")
    FIREBASE_TOKEN_URI = os.getenv("FIREBASE_TOKEN_URI")
    FIREBASE_AUTH_PROVIDER_X509_CERT_URL = os.getenv(
        "FIREBASE_AUTH_PROVIDER_X509_CERT_URL"
    )
    FIREBASE_CLIENT_X509_CERT_URL = os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
    FIREBASE_UNIVERSE_DOMAIN = os.getenv("FIREBASE_UNIVERSE_DOMAIN")
    FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")

    # Plume labs
    PLUME_LABS_BASE_URL = os.getenv("PLUME_LABS_BASE_URL")
    PLUME_LABS_ORGANISATIONS_CRED = os.getenv("PLUME_LABS_ORGANISATIONS_CRED")

    # Air Beam
    AIR_BEAM_USERNAMES = os.getenv("AIR_BEAM_USERNAMES")
    AIR_BEAM_BASE_URL = os.getenv("AIR_BEAM_BASE_URL")

    # Purple Air
    PURPLE_AIR_BASE_URL = os.getenv("PURPLE_AIR_BASE_URL")
    PURPLE_AIR_API_KEY = os.getenv("PURPLE_AIR_API_KEY")

    AIRQO_BAM_CONFIG = {
        0: "timestamp",
        1: "realtime_conc",
        2: "hourly_conc",
        3: "short_time_conc",
        4: "air_flow",
        5: "wind_speed",
        6: "wind_direction",
        7: "temperature",
        8: "humidity",
        9: "barometric_pressure",
        10: "filter_temperature",
        11: "filter_humidity",
        12: "status",
    }

    AIRQO_BAM_MAPPING = {
        "hourly_conc": "pm2_5",
    }
    # 1st 6 values are from the gps
    AIRQO_LOW_COST_CONFIG = {
        0: "latitude",
        1: "longitude",
        2: "altitude",
        3: "wind_speed",  # For mobile devices (Velocity)
        4: "satellites",  # Number of satelites tracked
        5: "hdop",  # For mobile devices
        6: "device_temperature",  # Internal
        7: "device_humidity",  # Internal
        8: "temperature",  # Internal
        9: "humidity",
        10: "vapor_pressure",
    }

    AIRQO_LOW_COST_GAS_CONFIG = {
        0: "latitude",
        1: "longitude",
        2: "altitude",
        3: "wind_speed",
        4: "satellites",
        5: "hdop",
        6: "device_temperature",
        7: "device_humidity",
        8: "temperature",
        9: "humidity",
        10: "vapor_pressure",
    }
    AIRQO_DATA_COLUMN_NAME_MAPPING = {
        "pm2_5": "pm2_5",
        "s1_pm2_5": "pm2_5",
        "s2_pm2_5": "pm2_5",
        "pm2_5_pi": "pm2_5",
        "pm2_5_raw_value": "pm2_5",
        "pm2_5_calibrated_value": "pm2_5",
        "pm10": "pm10",
        "s1_pm10": "pm10",
        "s2_pm10": "pm10",
        "pm10_pi": "pm10",
        "pm10_raw_value": "pm10",
        "pm10_calibrated_value": "pm10",
        "device_humidity": "humidity",
        "humidity": "humidity",
        "device_temperature": "temperature",
        "temperature": "temperature",
        "no2": "no2",
        "no2_raw_value": "no2",
        "no2_calibrated_value": "no2",
        "pm1": "pm1",
        "pm1_raw_value": "pm1",
        "pm1_pi": "pm1",
    }

    # Schema files mapping
    SCHEMA_FILE_MAPPING = {
        BIGQUERY_HOURLY_EVENTS_TABLE: "measurements.json",
        BIGQUERY_DAILY_EVENTS_TABLE: "measurements.json",
        BIGQUERY_RAW_EVENTS_TABLE: "raw_measurements.json",
        BIGQUERY_HOURLY_WEATHER_TABLE: "weather_data.json",
        BIGQUERY_RAW_WEATHER_TABLE: "weather_data.json",
        BIGQUERY_LATEST_EVENTS_TABLE: "latest_measurements.json",
        BIGQUERY_ANALYTICS_TABLE: "data_warehouse.json",
        BIGQUERY_AIRQLOUDS_TABLE: "airqlouds.json",
        BIGQUERY_AIRQLOUDS_SITES_TABLE: "airqlouds_sites.json",
        BIGQUERY_GRIDS_TABLE: "grids.json",
        BIGQUERY_COHORTS_TABLE: "cohorts.json",
        BIGQUERY_GRIDS_SITES_TABLE: "grids_sites.json",
        BIGQUERY_COHORTS_DEVICES_TABLE: "cohorts_devices.json",
        BIGQUERY_SITES_TABLE: "sites.json",
        BIGQUERY_SITES_META_DATA_TABLE: "sites_meta_data.json",
        SENSOR_POSITIONS_TABLE: "sensor_positions.json",
        BIGQUERY_DEVICES_TABLE: "devices.json",
        BIGQUERY_CLEAN_RAW_MOBILE_EVENTS_TABLE: "mobile_measurements.json",
        BIGQUERY_UNCLEAN_RAW_MOBILE_EVENTS_TABLE: "mobile_measurements.json",
        BIGQUERY_AIRQO_MOBILE_EVENTS_TABLE: "airqo_mobile_measurements.json",
        BIGQUERY_BAM_EVENTS_TABLE: "bam_measurements.json",
        BIGQUERY_RAW_BAM_DATA_TABLE: "bam_raw_measurements.json",
        "all": None,
    }

    # Data unit tests
    BUCKET_NAME_AIRQO = os.getenv("BUCKET_NAME")
    FILE_PATH_AIRQO = os.getenv("FILE_PATH_AIRQO")

    # Forecast job
    HOURLY_FORECAST_TRAINING_JOB_SCOPE = os.getenv("HOURLY_FORECAST_TRAINING_JOB_SCOPE")
    DAILY_FORECAST_TRAINING_JOB_SCOPE = os.getenv("DAILY_FORECAST_TRAINING_JOB_SCOPE")
    HOURLY_FORECAST_PREDICTION_JOB_SCOPE = os.getenv(
        "HOURLY_FORECAST_PREDICTION_JOB_SCOPE"
    )
    DAILY_FORECAST_PREDICTION_JOB_SCOPE = os.getenv(
        "DAILY_FORECAST_PREDICTION_JOB_SCOPE"
    )
    HOURLY_FORECAST_HORIZON = os.getenv("HOURLY_FORECAST_HORIZON")
    DAILY_FORECAST_HORIZON = os.getenv("DAILY_FORECAST_HORIZON")
    SATELLITE_TRAINING_SCOPE = os.getenv("SATELLITE_TRAINING_SCOPE")
    MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
    FORECAST_MODELS_BUCKET = os.getenv("FORECAST_MODELS_BUCKET")
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "airqo_db")
    ENVIRONMENT = os.getenv("ENVIRONMENT")

    # Twitter bot
    TWITTER_BOT_API_KEY = os.getenv("TWITTER_BOT_API_KEY")
    TWITTER_BOT_API_KEY_SECRET = os.getenv("TWITTER_BOT_API_KEY_SECRET")
    TWITTER_BOT_BEARER_TOKEN = os.getenv("TWITTER_BOT_BEARER_TOKEN")
    TWITTER_BOT_ACCESS_TOKEN = os.getenv("TWITTER_BOT_ACCESS_TOKEN")
    TWITTER_BOT_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_BOT_ACCESS_TOKEN_SECRET")

    # Email
    MAIL_USER = os.getenv("MAIL_USER")
    MAIL_PASS = os.getenv("MAIL_PASS")

    def unsubscribe_url(self, email, user_id):
        print(os.getenv("UNSUBSCRIBE_URL"))
        return f"{os.getenv('UNSUBSCRIBE_URL')}?email={email}&user_id={user_id}"


configuration = Config()

# MONGO_DB
client = pm.MongoClient(configuration.MONGO_URI)
db = client[configuration.MONGO_DATABASE_NAME]

# Twitter
twitter_client = tweepy.Client(
    bearer_token=configuration.TWITTER_BOT_BEARER_TOKEN,
    access_token=configuration.TWITTER_BOT_ACCESS_TOKEN,
    access_token_secret=configuration.TWITTER_BOT_ACCESS_TOKEN_SECRET,
    consumer_key=configuration.TWITTER_BOT_API_KEY,
    consumer_secret=configuration.TWITTER_BOT_API_KEY_SECRET,
)
twitter_auth = tweepy.OAuthHandler(
    access_token=configuration.TWITTER_BOT_ACCESS_TOKEN,
    access_token_secret=configuration.TWITTER_BOT_ACCESS_TOKEN_SECRET,
    consumer_key=configuration.TWITTER_BOT_API_KEY,
    consumer_secret=configuration.TWITTER_BOT_API_KEY_SECRET,
)
