from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
from threading import Thread, Lock
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
MAX_PACKETS = 300

lock = Lock()

packets = []
sniffing_active = False
sniffer_thread = None

def get_service(port):
    port = int(port)

    if(port == 80):
        return "HTTP"
    elif(port == 443):
        return "HTTPS"
    elif(port == 53):
        return "DNS"
    elif(port == 21):
        return "FTP"
    elif(port == 22):
        return "SSH"
    else:
        return "UNKNOWN"


# SNIFFER

def process_packet(packet):
    if not sniffing_active:
        return
    
    if IP not in packet:
        return

    if IP in packet:
        data = {}

        data["Time"] = datetime.now().strftime("%H:%M:%S")

        # IPs
        data["Source IP"] = packet[IP].src
        data["Destination IP"] = packet[IP].dst

        # Packet Size
        data["Packet Size"] = len(packet)

        # Protocol, Source Port, Destination Port
        data["Protocol"] = "OTHER"
        data["Source Port"] = "-"
        data["Destination Port"] = "-"

        # For TCP
        if TCP in packet:
            data["Protocol"] = "TCP"
            data["Source Port"] = packet[TCP].sport
            data["Destination Port"] = packet[TCP].dport

        # For UDP
        elif UDP in packet:
            data["Protocol"] = "UDP"
            data["Source Port"] = packet[UDP].sport
            data["Destination Port"] = packet[UDP].dport

        # For ICMP
        elif ICMP in packet:
            data["Protocol"] = "ICMP"

        if(data["Destination Port"] != "-" and data["Destination Port"] != ""):
            data["Service"] = get_service(data["Destination Port"])
        else:
            data["Service"] = "N/A"

        with lock:
            if len(packets) >= MAX_PACKETS:
                packets.pop(0)

            packets.append(data)

def start_sniffing():
    sniff(prn=process_packet, store=False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    global sniffing_active, sniffer_thread

    if sniffer_thread is None or not sniffer_thread.is_alive():
        sniffer_thread = Thread(target=start_sniffing, daemon=True)
        sniffer_thread.start()

    sniffing_active = True

    with lock:
        packets.clear()

    return {"status" : "started"}

@app.route('/stop')
def stop():
    global sniffing_active
    sniffing_active = False

    return {"status" : "stopped"}

@app.route('/clear')
def clear():
    global sniffing_active
    sniffing_active = False

    global packets
    with lock:
        packets.clear()

    return {"status" : "cleared"}

@app.route('/data')
def data():
    with lock:
        filtered = list(packets)

    # DATA FILTERING

    protocol = request.args.get('protocol')
    src_ip = request.args.get('src_ip')
    dest_ip = request.args.get('dest_ip')

    if(protocol):
        new_data = []
        for d in filtered:
            if(d['Protocol'].lower() == protocol.lower()):
                new_data.append(d)
        filtered = new_data

    if(src_ip):
        new_data = []
        for d in filtered:
            if(src_ip in d["Source IP"]):
                new_data.append(d)
        filtered = new_data

    if(dest_ip):
        new_data = []
        for d in filtered:
            if(dest_ip in d["Destination IP"]):
                new_data.append(d)
        filtered = new_data

    # STATISTICS

    total_packets = len(filtered)

    tcp = 0
    udp = 0
    icmp = 0
    total_size = 0

    for d in filtered:
        if(d['Protocol'] == "TCP"):
            tcp += 1
        elif(d["Protocol"] == "UDP"):
             udp += 1
        elif(d["Protocol"] == "ICMP"):
             icmp += 1

        try:
            total_size += int(d["Packet Size"])
        except:
            pass

    avg_size = round(total_size/total_packets, 2) if total_packets > 0 else 0

    return jsonify({
        "packets":filtered,
        "stats": {
            "total_packets" : total_packets,
            "tcp" : tcp,
            "udp" : udp,
            "icmp" : icmp,
            "avg_size" : avg_size,
            "total_bytes" : total_size
        }
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)