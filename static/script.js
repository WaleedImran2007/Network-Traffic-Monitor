let interval = null

function fetchData() {
    let protocol = document.getElementById('protocols').value;
    let src_ip = document.getElementById('src_ip').value;
    let dest_ip = document.getElementById('dest_ip').value;

    let url = `/data?protocol=${protocol}&src_ip=${src_ip}&dest_ip=${dest_ip}`;

    let lastIndex = 0

    fetch(url)
    .then(response => response.json())
    .then(result => {
        let data = result.packets
        let stats = result.stats
        let emptyState = document.getElementById('no-data');

        let table = document.getElementById('tableBody')
        table.innerHTML = ""

        let total_packets = document.querySelector('.total-packets');
        let tcp_packets = document.querySelector('.tcp-packets');
        let udp_packets = document.querySelector('.udp-packets');
        let icmp_packets = document.querySelector('.icmp-packets');
        let avg_size = document.querySelector('.avg-size');
        let total_bytes = document.querySelector('.total-bytes');

        total_packets.textContent = stats.total_packets;
        tcp_packets.textContent = stats.tcp;
        udp_packets.textContent = stats.udp;
        icmp_packets.textContent = stats.icmp;
        avg_size.textContent = stats.avg_size;
        total_bytes.textContent = stats.total_bytes;

        if(data.length == 0) {
            emptyState.classList.remove('hidden')
            table.innerHTML = ""
            return;
        } else {
            emptyState.classList.add('hidden')
        }

        data.forEach(row => {
            table.innerHTML += `
                <tr>
                    <td>${row.Time}</td>
                    <td>${row["Source IP"]}</td>
                    <td>${row["Destination IP"]}</td>
                    <td>${row.Protocol}</td>
                    <td>${row["Packet Size"]}</td>
                    <td>${row["Source Port"]}</td>
                    <td>${row["Destination Port"]}</td>
                    <td>${row["Service"]}</td>
                </tr>
            `
        });
    })
}

function startMonitoring() {
    alert('Started Monitoring')
    if(!interval) {
        fetch('/start')
        fetchData()
        interval = setInterval(fetchData, 3000)
    }
}

function stopMonitoring() {
    alert('Stopped Monitoring')
    fetch('/stop')
    clearInterval(interval)
    interval = null
}

function clearData() {
    alert('Cleared Data')

    document.getElementById('tableBody').innerHTML = ""

    document.querySelector('.total-packets').textContent = 0;
    document.querySelector('.tcp-packets').textContent = 0;
    document.querySelector('.udp-packets').textContent = 0;
    document.querySelector('.icmp-packets').textContent = 0;
    document.querySelector('.avg-size').textContent = 0;
    document.querySelector('.total-bytes').textContent = 0;

    document.getElementById('no-data').classList.remove('hidden');

    fetch('/clear')
}

function applyFilter() {
    fetchData();
}

function resetFilter() {
    document.getElementById('protocols').value = "";
    document.getElementById('src_ip').value = "";
    document.getElementById('dest_ip').value = "";
    fetchData();
}