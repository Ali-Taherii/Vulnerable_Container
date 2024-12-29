import subprocess
import argparse

def run_snmpwalk(ip, community, oid):
    """Run snmpwalk command."""
    try:
        command = ["snmpwalk", "-v2c", "-c", community, ip, oid]
        result = subprocess.check_output(command, stderr=subprocess.DEVNULL, text=True)
        if result:
            print(f"[+] Community: {community} | OID: {oid}")
            print(result)
    except subprocess.CalledProcessError:
        pass

def enumerate_snmp(ip, community_strings, oids):
    """Enumerate SNMP information."""
    print(f"Starting SNMP enumeration on {ip}...")
    for community in community_strings:
        print(f"Trying community: {community}")
        for oid in oids:
            run_snmpwalk(ip, community, oid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SNMP Enumeration Script")
    parser.add_argument("target_ip", help="Target IP address to enumerate")
    args = parser.parse_args()

    # Common community strings and OIDs
    community_strings = ["public", "private", "snmp", "default"]  # Common community strings
    oids = [
        "1.3.6.1.2.1.1",  # System Information
        "1.3.6.1.2.1.2",  # Network Interfaces
        "1.3.6.1.2.1.25.1",  # Host Resources
    ]

    # Start enumeration
    enumerate_snmp(args.target_ip, community_strings, oids)