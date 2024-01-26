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
from functools import partial
from diagrams import Diagram, Edge

fs="20"
Edge = partial(Edge, labelloc="t", fontsize=fs)
Custom = partial(Custom, labelloc="b", fontsize=fs)


with Diagram("", show=False):
    mqtt = IotMqtt("mqtt",  fontsize=fs)
    cloud = Cloudtrail("cloud" ,fontsize=fs)
    sms = SMS("SMS alert",  fontsize=fs)
    email = SimpleEmailServiceSesEmail("email ", fontsize=fs)

    solar = Custom("solar panel", "solar-panel.png")
    water = Custom("micro turbine", "hydro-power.png")

    with Cluster("remote site with embedded system"):
        cap = IotAlexaEnabledDevice("microcontroler", fontsize=fs)
        sensor = IotGreengrassConnector("infrared sensor", fontsize=fs)
        pilote = IotRule("driver", fontsize=fs)
        sd = IotAnalyticsDataStore("CF card", fontsize=fs)
        gsm = IotOverTheAirUpdate("GSM network", fontsize=fs)
        batterie = Custom("batterie", "battery-70.png")

        embedded = [gsm]

    with Cluster("technical support center"):
        soft = InternetAlt1("software frontend", fontsize=fs)
        db = GenericDatabase("database", fontsize=fs)
        comp = Client("workstation", fontsize=fs)
        user = User("resource manager", fontsize=fs)
        rap = Analytics("report", fontsize=fs)

        mairie = [soft]

    with Cluster("supervisor"):
        su = User("service personel", fontsize=fs)
        mobile = MobileClient("portable", fontsize=fs)

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
