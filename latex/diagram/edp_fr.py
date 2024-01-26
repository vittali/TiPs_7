from diagrams import Diagram, Cluster
from diagrams.aws.compute import *
from diagrams.aws.management import *
from diagrams.aws.database import *
from diagrams.aws.network import *
from diagrams.aws.iot import *
from diagrams.aws.general import *
from diagrams.aws.migration import *
from diagrams.aws.analytics import *
from diagrams.aws.engagement import *
from diagrams.custom import Custom

with Diagram("transmission et stockage des données de captage", show=False):
    mqtt = IotMqtt("mqtt protocole de transmission")
    cloud = Cloudtrail("cloud")
    sms = SMS("alerte SMS")
    email = SimpleEmailServiceSesEmail("alerte courriel")

    solar = Custom("panneau solaire", "solar-panel.png")
    water = Custom("micro turbine", "hydro-power.png")

    with Cluster("EauDuPuid - object connecté"):
        cap = IotAlexaEnabledDevice("microcontrôleur")
        sensor = IotGreengrassConnector("capteur infrarouge")
        pilote = IotRule("pilote")
        sd = IotAnalyticsDataStore("carte CF")
        gsm = IotOverTheAirUpdate("réseau GSM")
        batterie = Custom("batterie", "battery-70.png")

        embedded = [gsm]

    with Cluster("mairie"):
        soft = InternetAlt1("EauDuPuid - logiciel")
        db = GenericDatabase("base de donnees")
        comp = Client("ordinateur")
        user = User("mairie")
        rap = Analytics("rapport")

        mairie = [soft]

    with Cluster("superviseur"):
        su = User("service technique")
        mobile = MobileClient("portable")

        supervisor = [mobile]

    sensor >> cap
    pilote >> cap
    sd >> cap
    gsm >> cap
    batterie >> cap
    solar >> batterie
    water >> batterie
    embedded >> mqtt >> cloud >> mairie
    soft >> db >> comp
    user >> comp
    user >> rap
    cloud >> sms
    cloud >> email
    sms >> supervisor
    supervisor >> mobile
